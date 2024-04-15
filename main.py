import pysine as snd
import random as rm

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





# snd.sine(frequency=440.0, duration=0.3) 
# snd.sine(frequency=660.0, duration=0.3) 
# snd.sine(frequency=990.0, duration=0.3)  
# snd.sine(frequency=1485.0, duration=0.3) 
# snd.sine(frequency=2227.5, duration=0.3) 
# snd.sine(frequency=3341.25, duration=0.3) 
# snd.sine(frequency=5011.875, duration=0.3) 