import pysine as snd
import random as rnd
import numpy as np

## Frequenciy of each note in Hz
notes = [440.0, 660.0, 990.0, 1485.0, 2227.5, 3341.25, 5011.875]

## Control variables for movement 
curr = rnd.randint(0,6) ## Initializes current node as a random integer between 1 and 6
next = 0

## Controls how many times the loop will occur
tempControl = 0

## Transition matrix. Determines what is the probability of moving from one node to the next
TransitionMatrix = [
    [0.2, 0.1, 0.1, 0.3, 0.1, 0.1, 0.1], 
    [0.1, 0.1, 0.3, 0.1, 0.1, 0.2, 0.1],
    [0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3],
    [0.1, 0.3, 0.1, 0.1, 0.2, 0.1, 0.1],
    [0.1, 0.2, 0.1, 0.3, 0.1, 0.1, 0.1],
    [0.3, 0.1, 0.1, 0.1, 0.2, 0.1, 0.1],
    [0.1, 0.1, 0.2, 0.1, 0.1, 0.3, 0.1]
]   
    
while(tempControl <= 21):
    ## Chooses an element from the current node's transition array based on the 
    next = np.random.choice(7, replace=True, p=TransitionMatrix[curr]) 
    ## Plays a sound corresponding to the current note
    snd.sine(frequency=notes[curr], duration=0.3)
    ## If the note transition corresponds to itself, do nothing
    ## If the transition is to a different note, set the current note's index to the next one
    if curr == next:
        pass
    else:
        curr = next
    
    ## Increase the counter cycle
    tempControl += 1
        
         
        
    
