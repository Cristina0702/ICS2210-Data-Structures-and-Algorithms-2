#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct states states_t;
typedef states_t *states_ptr;

typedef struct states{
    char state;
    int a; //outgoing transition 
    int b; //outgoing transition
    bool accepting; // = false;
}*states_ptr;

typedef struct dfa{
    states_ptr *states; //= {0}; //K  //size n
    char *alphabet; //= {0}; //T
    //char *transitions;
    int initial;
    int *final; //F
} *dfa_ptr;

dfa_ptr init(int n){
    if(n >= 16 && n <= 64){
        //if n is between 16 and 64
        dfa_ptr dfa = malloc(sizeof())
    }else{
        return NULL;
    }
}

void main(){
    dfa_ptr dfa;
    
    int n = rand() % 49 + 16; //random number between 16 and 64
    printf("%d \n", n);

    //dfa->states = NULL;
    //dfa->alphabet = NULL;
    //dfa->final = NULL;
    //dfa->initial = 0;
    
    for (int i = 0; i < n; i++){
        int coin = rand() % 2; //random number between 0 and 1
        if (coin == 0){
            dfa->states[i]->accepting = true;
            printf("State %d is accepting\n", i);
        }else if(coin == 1){
            dfa->states[i]->accepting = false;
            printf("State %d is not accepting\n", i);
        }
    }
    

}