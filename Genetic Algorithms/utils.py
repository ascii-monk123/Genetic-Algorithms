import numpy as np
from numpy.random import randint
from numpy.random import rand

def tourney_selection(pop, scores, k=3):
    #select one individual randomly
    selection_idx = randint(len(pop))
    #choose k-1 random members
    for idx in randint(0, len(pop), k-1):
        if scores[idx] > scores[selection_idx]:
            selection_idx = idx
    #return the tournament winner
    return pop[selection_idx]
        


def crossover(p1, p2, cross):
    #make children the copies of parents by default
    c1, c2 = p1.copy(), p2.copy()
    #random number to decide whether to perform crossover or not
    if rand() < cross:
        #select a cross over point
        c_pt = randint(1, len(p1) - 2)
        #crossover
        c1 = p1[:c_pt] + p2[c_pt:]
        c2 = p2[:c_pt] + p1[c_pt:]

    #return the children
    return [c1, c2]
        
        

def mutation(indv, n_mut):
    for i in range(len(indv)):
        #check whether to mutate or not
        if rand() < n_mut:
            #flip the bit
            indv[i] = 1 - indv[i]
    #return the mutated individual
    return indv
    


