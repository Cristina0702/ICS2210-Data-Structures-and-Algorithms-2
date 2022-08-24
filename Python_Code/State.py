import random

class State:

    def __init__(self, s_id, accepting = None):
        #setting the state details
        self.id = s_id
        if accepting == None:
            #fliping a coin to randomly decide whether state is accepting or not
            self.accepting = self.flip_coin()
        else:
            self.accepting = accepting
        #setting transitions to initially be -1
        self.transitions = {'a': -1, 'b': -1}
        self.partition_states = []
    
    def set_transitions(self, a, b):
        #setting the state transitions
        self.transitions = {'a': a, 'b': b} #a and b are state ids
    
    def set_partition_states(self, states_ids):
        #setting the partition states
        self.partition_states = states_ids
    
    def flip_coin(self):
        #simulating flipping a coin
        coin =  bool(random.getrandbits(1)) #either True or False
        return coin
    
    def print_details(self):
        #printing the state details
        print("State ID: ", self.id)
        print("Transition A: state ", self.transitions['a'])
        print("Transition B: state ", self.transitions['b'])
        print("Is accepting: ", self.accepting)
        if self.partition_states:
            print("Partition States: ", self.partition_states)
        print()
