from DFSA import DFSA
import random 
    
def main():

    #choosing a random number of states
    n = random.randint(16,64) #random number between 16 and 64 inclusive
    
    print("DFSA A: ")
    A = DFSA(15)
    DFSA.print_details(A)
    DFSA.calculate_depth(A)

    print("\nDFSA M: ")
    M = DFSA.minimise(A)
    DFSA.print_details(M)
    DFSA.calculate_depth(M)

    #print("\nSCCs of A: ")
    #DFSA.get_SCCs(A)

    print("\nSCCs of M: ")
    DFSA.get_SCCs(M)

main()