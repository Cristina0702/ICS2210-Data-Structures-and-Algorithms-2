#pragma once

#define MAX_STATES 64

typedef struct states{
    int content;
    int a; //outgoing transition 
    int b; //outgoing transition
    bool accepting; // = false;
} states_ptr;

typedef struct dfa{
    states_ptr *states[MAX_STATES]; //= {0}; //K  //size n
    int count;
    char *alphabet; //= {0}; //T
    //char *transitions;
    int initial;
    int current;
    int *final; //F
}dfa_ptr;