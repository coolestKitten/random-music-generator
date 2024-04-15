import pysine as snd
import numpy as np

## Frequenciy of each note in Hz
note1 = 440.0
note2 = 660.0
note3 = 990.0
note4 = 1485.0
note5 = 2227.5
note6 = 3341.25
note7 = 5011.875

## Control variables for movement 
curr = 0
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

while (tempControl <= 21):
    if curr == 0:
        next = np.random.choice(7, replace=True, p=TransitionMatrix[curr])
        if next == 0:
            snd.sine(frequency=note1, duration=0.3) 
            pass
        if next == 1:
            snd.sine(frequency=note2, duration=0.3) 
            curr = next
        if next == 2:
            snd.sine(frequency=note3, duration=0.3) 
            curr = next
        if next == 3:
            snd.sine(frequency=note4, duration=0.3) 
            curr = next
        if next == 4:
            snd.sine(frequency=note5, duration=0.3) 
            curr = next
        if next == 5:
            snd.sine(frequency=note6, duration=0.3) 
            curr = next
        if next == 6:
            snd.sine(frequency=note7, duration=0.3) 
            curr = next
        
    elif curr == 1:
        next = np.random.choice(7, replace=True, p=TransitionMatrix[curr])
        if next == 0:
            snd.sine(frequency=note1, duration=0.3) 
            curr = next
        if next == 1:
            snd.sine(frequency=note2, duration=0.3) 
            pass
        if next == 2:
            snd.sine(frequency=note3, duration=0.3) 
            curr = next
        if next == 3:
            snd.sine(frequency=note4, duration=0.3) 
            curr = next
        if next == 4:
            snd.sine(frequency=note5, duration=0.3) 
            curr = next
        if next == 5:
            snd.sine(frequency=note6, duration=0.3) 
            curr = next
        if next == 6:
            snd.sine(frequency=note7, duration=0.3) 
            curr = next
        
    elif curr == 2:
        next = np.random.choice(7, replace=True, p=TransitionMatrix[curr])
        if next == 0:
            snd.sine(frequency=note1, duration=0.3) 
            curr = next
        if next == 1:
            snd.sine(frequency=note2, duration=0.3) 
            curr = next
        if next == 2:
            snd.sine(frequency=note3, duration=0.3) 
            pass
        if next == 3:
            snd.sine(frequency=note4, duration=0.3) 
            curr = next
        if next == 4:
            snd.sine(frequency=note5, duration=0.3) 
            curr = next
        if next == 5:
            snd.sine(frequency=note6, duration=0.3) 
            curr = next
        if next == 6:
            snd.sine(frequency=note7, duration=0.3) 
            curr = next
        
    elif curr == 3:
        next = np.random.choice(7, replace=True, p=TransitionMatrix[curr])
        if next == 0:
            snd.sine(frequency=note1, duration=0.3) 
            curr = next
        if next == 1:
            snd.sine(frequency=note2, duration=0.3) 
            curr = next
        if next == 2:
            snd.sine(frequency=note3, duration=0.3) 
            curr = next
        if next == 3:
            snd.sine(frequency=note4, duration=0.3) 
            pass
        if next == 4:
            snd.sine(frequency=note5, duration=0.3) 
            curr = next
        if next == 5:
            snd.sine(frequency=note6, duration=0.3) 
            curr = next
        if next == 6:
            snd.sine(frequency=note7, duration=0.3) 
            curr = next
                 
    elif curr == 4:
        next = np.random.choice(7, replace=True, p=TransitionMatrix[curr])
        if next == 0:
            snd.sine(frequency=note1, duration=0.3) 
            curr = next
        if next == 1:
            snd.sine(frequency=note2, duration=0.3) 
            curr = next
        if next == 2:
            snd.sine(frequency=note3, duration=0.3) 
            curr = next
        if next == 3:
            snd.sine(frequency=note4, duration=0.3) 
            curr = next
        if next == 4:
            snd.sine(frequency=note5, duration=0.3) 
            pass
        if next == 5:
            snd.sine(frequency=note6, duration=0.3) 
            curr = next
        if next == 6:
            snd.sine(frequency=note7, duration=0.3) 
            curr = next
          
    elif curr == 5:
        next = np.random.choice(7, replace=True, p=TransitionMatrix[curr])
        if next == 0:
            snd.sine(frequency=note1, duration=0.3) 
            curr = next
        if next == 1:
            snd.sine(frequency=note2, duration=0.3) 
            curr = next
        if next == 2:
            snd.sine(frequency=note3, duration=0.3) 
            curr = next
        if next == 3:
            snd.sine(frequency=note4, duration=0.3) 
            curr = next
        if next == 4:
            snd.sine(frequency=note5, duration=0.3) 
            curr = next
        if next == 5:
            snd.sine(frequency=note6, duration=0.3) 
            pass
        if next == 6:
            snd.sine(frequency=note7, duration=0.3) 
            curr = next
            
    elif curr == 6:
        next = np.random.choice(7, replace=True, p=TransitionMatrix[curr])
        if next == 0:
            snd.sine(frequency=note1, duration=0.3) 
            curr = next
        if next == 1:
            snd.sine(frequency=note2, duration=0.3) 
            curr = next
        if next == 2:
            snd.sine(frequency=note3, duration=0.3) 
            curr = next
        if next == 3:
            snd.sine(frequency=note4, duration=0.3) 
            curr = next
        if next == 4:
            snd.sine(frequency=note5, duration=0.3) 
            curr = next
        if next == 5:
            snd.sine(frequency=note6, duration=0.3) 
            curr = next
        if next == 6:
            snd.sine(frequency=note7, duration=0.3) 
            pass
         
    tempControl += 1
