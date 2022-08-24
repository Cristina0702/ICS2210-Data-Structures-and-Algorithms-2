from State import State
import random
# deterministic finite state automaton
class DFSA:

    #https://www.tutorialspoint.com/automata_theory/deterministic_finite_automaton.htm
    #I. Bondin. (2021). Formal Languages and Automata [PowerPoint Slides]. Available: https://www.um.edu.mt/vle/pluginfile.php/937526/mod_resource/content/2/Slide%20Deck%20%2825112021%29%20-%20Formalisation%20of%20DFA.pdf
    def __init__(self, n, auto_fill = True, initial = None, final = None, not_final = None, states = None):
        #setting the dfsa details
        self.n = n
        self.alphabet = ['a','b']
        self.visited = [] #list of state ids
        
        #for finding scc:
        self.scc_state = -1
        self.scc = []
        
        if auto_fill == True:
            #randomising the initial state
            self.initial = random.randint(0, n-1) #choosing a random state as the initial state
            self.final = [] #list of state ids
            self.not_final = [] #list of state ids
            self.states = [] #list of states
            
            for i in range(n):
                #creating states and appending them to the states array
                state = State(s_id=i)
                self.states.append(state)
                #appending the state ids to either the final or not final arrays
                if state.accepting == True:
                    self.final.append(i)
                elif state.accepting == False:
                    self.not_final.append(i)
        
            #sorting the final and not final arrays
            self.final.sort()
            self.not_final.sort()
            
            #randomly setting the state transitions
            for i in range(n):
                a = random.randint(0,n-1) #choosing random states for transition a
                b = random.randint(0,n-1) #choosing random states for transition b
                self.states[i].set_transitions(a=a,b=b)
                
        elif auto_fill == False:
            #filling the dfsa with the given details
            self.initial = initial
            self.final = final
            self.not_final = not_final
            self.states = states
        
    def print_details(self):
        #printing the dfsa details
        print()
        print("Number of states: ", self.n)
        print("Alphabet: ", self.alphabet)
        print("Initial state id: ", self.initial)
        print("Final states array: ", self.final)
        print("Not final states array: ",self.not_final)
        print()
        for state in self.states:
            state.print_details()

    #https://medium.com/geekculture/breadth-first-search-in-python-822fb97e0775 
    #https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
    #https://favtutor.com/blogs/breadth-first-search-python
    #https://www.geeksforgeeks.org/program-to-calculate-height-and-depth-of-a-node-in-a-binary-tree/ 
    def breadth_first_search(self):
        max_depth = 0
        visited = [False] * (len(self.states))
        queue = []
        
        #storing the depth of each node from initial state 
        depth = {i: 0 for i in range(self.n)}
        #setting the depth for the initial state to be 0
        depth [0] = 0
        
        #starting from the initial state
        #adding initial state to queue
        queue.append(self.initial)
        visited[self.initial] = True
        
        #looping whilst queue isn't empty
        while queue:
            #popping the value from the queue
            current = queue.pop(0)
            #getting the state ids stored as the transitions of the current state
            for s_id in self.states[current].transitions.values():
                #if state has not already been seen
                if visited[s_id] == False:
                    #appending the transition state id to the queue and to the visited array
                    queue.append(s_id)
                    print("Current: ", current, "\nPushed: ",s_id, "\n")
                    visited[s_id] = True 
                    #setting the depth of the state by taking the depth of its parent state and increasing it by 1
                    depth[s_id] = depth[current] + 1
        
        #appended the visited states to the visited array
        for i in range(len(visited)):
            if visited[i] == True:
                self.visited.append(self.states[i].id)
        
        #displaying the visited array
        print("Visited array:",self.visited)
        #getting the maximum depth from the depth array 
        max_depth = max(depth.values())
        #returning the maximum depth
        return max_depth
    
    def calculate_depth(self):
        #calling the breadth first search function to get the depth
        depth = self.breadth_first_search()
        #displaying the depth
        print("Depth: ", depth, "\n")
    
    #https://stackoverflow.com/questions/13549662/dfa-minimization-by-hopcroft-algorithm
    #https://en.wikipedia.org/wiki/DFA_minimization#Hopcroft.27s_algorithm
    #https://stackoverflow.com/questions/26727766/hopcrofts-algorithm-dfa-minimization
    #https://swaminathanj.github.io/fsm/dfaminimization.html
    #https://m.riunet.upv.es/bitstream/handle/10251/27623/partial%20rev%20determ.pdf
    #https://www.geeksforgeeks.org/minimization-of-dfa/
    def hopcrofts_algorithm(self):

        final_states = []
        not_final_states = []
        
        #looping through the final and visited arrays
        for state in self.final:
            if state in self.visited:
                #adding only the reachable final states
                final_states.append(state)
        
        #looping through the not final and visited arrays
        for state in self.not_final:
            if state in self.visited:
                #adding only the reachable final states
                not_final_states.append(state)
        
        #setting the partition to contain the final reachable states and not final reachable states
        P = [final_states, not_final_states]
        #setting the waitlist to contain the final reachable states and not final reachable states
        W = [final_states, not_final_states]  
        
        while len(W) != 0:
            A = W.pop(0)
            for c in self.alphabet:
                X = []
                for s_id in self.visited: 
                    if (self.states[s_id].transitions[c] in A) and (self.states[s_id].transitions[c] not in X):
                            #appending entire state into X
                            X.append(self.states[s_id]) 

                for Y in P:                        
                    #computing the intersection and difference
                    inter = list(set(X).intersection(Y))
                    diff = list(set(Y).difference(X))
                    
                    #if intersection and difference are not empty
                    if inter and diff:
                        #removing the current part from the partitions and adding the intersection and difference
                        P.remove(Y)
                        P.append(inter)
                        P.append(diff)
                        if Y in W:
                            #removing the current part from the waitlist and adding the intersection and difference
                            W.remove(Y)
                            W.append(inter)
                            W.append(diff)
                        #otherwise, either the intersection or the difference will be appended to the waitlist
                        elif len(inter) <= len(diff):
                            W.append(inter)
                        else:
                            W.append(diff)
        
        #returning the partitions
        return P

    def minimise(self):
        #calling the hopcrofts algorithm function to get the partitions
        P = self.hopcrofts_algorithm()
        
        new_states = []
        new_final = []
        new_not_final = []
        new_initial = -1
        
        #looping through the partitions
        for i in range(len(P)):
            #taking the first state of each partition to check the transitions and if it is a final state or not
            state_id = P[i][0]
            state = self.states[state_id]
            #setting the partition as a state
            new_partition_state = State(s_id=i, accepting = state.accepting)
            
            #looping through the alphabet to set the transitions of the partition
            for letter in self.alphabet:
                s_id = state.transitions[letter]
                #looping through all the partitions values
                for x in range(len(P)):
                    #if state id is stored in partitions, then it will be set to the transitions
                    if s_id in P[x]:
                        new_partition_state.transitions[letter] = x

            if self.initial in P[i]:
                #setting the partition which contains the initial state as the initial
                initial = i 
            
            #adding the new partition as a state in the states array
            new_states.append(new_partition_state)
            
            #adding the partition id to either the final or not final array
            if new_partition_state.accepting == True:
                new_final.append(i)
            elif new_partition_state.accepting == False:
                new_not_final.append(i)
            
            #storing the partition states in the parition 
            new_partition_state.set_partition_states(P[i])
            
        #getting the number of partitions
        new_n = len(P)
        
        #just in case the initial state hasnt been set
        if new_initial == -1:
            new_initial = random.randint(0, new_n-1) #choosing a random state as the initial state
        
        #creating the new dfsa with the partitions 
        new_dfsa = DFSA(n = new_n, auto_fill = False, initial = new_initial, final = new_final, not_final = new_not_final, states = new_states)

        return new_dfsa
    
    #https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/
    #https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
    #https://www.topcoder.com/thrive/articles/tarjans-algorithm-for-strongly-connected-components
    #https://www.thealgorists.com/Algo/GraphTheory/Tarjan/SCC
    def get_SCCs(self):
        #making sure that scc_state is -1 and scc is empty
        self.scc_state = -1
        self.scc = []
        
        #to store the discovered states
        disc_states = []
        #setting all the elements in the discovered states id array and low values array to be all -1
        disc_ids = [-1] * (self.n)
        low_values = [-1] * (self.n)
        #setting all the values in the current stack array to be False
        current_stack = [False] * (self.n)
    
        #looping through the number of states in the dfsa
        for s_id in range(self.n):
            #if state hasn't been discovered yet
            if disc_ids[s_id] == -1:
                #tarjan algorithm will be called with the state id
                self.tarjan_algo(s_id, disc_ids, disc_states, low_values, current_stack)

        self.print_SCCs()

    def tarjan_algo(self, s_id, disc_ids, disc_states, low_values, current_stack):
        #increasing the number of scc_states
        self.scc_state = self.scc_state + 1
        #setting the ids to be according to the number of scc_states
        disc_ids[s_id] = self.scc_state
        low_values[s_id] = self.scc_state

        current_stack[s_id] = True
        disc_states.append(s_id)
        
        #looping through all child nodes for the given state
        for c_id in self.states[s_id].transitions.values():
            #if the child state is not discovered
            if disc_ids[c_id] == -1:
                #calling the tarjan_algo function for the undiscovered child state
                self.tarjan_algo(c_id, disc_ids, disc_states, low_values, current_stack)
                #setting the low value of the state to be the minimum value
                low_values[s_id] = min(low_values[s_id], low_values[c_id])
            #if the child node is on the current stack
            elif current_stack[c_id] == True:
                #setting the low value of the state to be the minimum value
                low_values[s_id] = min(low_values[s_id], disc_ids[c_id])
        
        #setting current to be -1
        current = -1
        #if the head node is found
        if low_values[s_id] == disc_ids[s_id]:
            #setting the current_SCCs array to be empty
            current_SCCs = []
            while current != s_id:
                #poping the stack of discovered states 
                current = disc_states.pop()
                #setting the popped state to be false in the current stack array
                current_stack[current] = False
                #appending the current state in the current_SCCs array
                current_SCCs.append(current)
            #appending the entire current_SCCs array to the scc array
            self.scc.append(current_SCCs)

    def print_SCCs(self):
        #printing the len if the scc array to show the number of scc
        print("Number of strongly connected components: ", len(self.scc))
        
        print("Size of largest SCC: ", len(max(self.scc, key=len)))
        print("Size of smallest SCC: ", len(min(self.scc, key=len)))