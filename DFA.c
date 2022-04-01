#include "DFA.h"

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

states_ptr *create_states(dfa_ptr *dfa, int n, int i){

    states_ptr *new_state = (states_ptr*)malloc(sizeof(states_ptr)*(n+1));
    new_state->content = i;
    new_state->accepting = flip_coin();

    int temp = rand() % n; //random number between 0 and n
    while(dfa->states[temp]->accepting == false){
        //looping until an accepting state is found
        temp = rand() % n;
    }
    new_state->a = temp;
    
    //making sure that a and b are different states
    while ((temp == new_state->a) || (dfa->states[temp]->accepting == false)){
        //looping until an accepting state is found which is a different state from a
        temp = rand() % n;
    }
    new_state->b = temp;
    
	return new_state;
}

bool flip_coin(){
    int coin = rand() % 2; //either 1 or 0
    if (coin == 0){
        return true;
    }else if(coin == 1){
        return false;
    }
}

dfa_ptr* init(int n){
    if(n >= 16 && n <= 64){
        //if n is between 16 and 64
        dfa_ptr *dfa = (dfa_ptr*)malloc(sizeof(dfa_ptr));
        dfa->count = 0;
        dfa->initial = rand() % n; //selecting a random state
        //dfa->current = -1;

        for(int i=0; i<n; i ++){
            dfa->states[i] = create_states(dfa, n, i);
        }

        return dfa;
    }else{
        return NULL;
    }
}

void destroy(dfa_ptr *dfa, int n){
    if (dfa != NULL){
        //to remove the memory allocations
        for (int i = 0; i < n; i++){
            if(dfa->states[i] != NULL){
                free(dfa->states[i]);
                dfa->states[i] = NULL;
            }
        }
        free(dfa->states);
        free(dfa);
        dfa = NULL;
    }
}

void main(){
    dfa_ptr *dfa;
    
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