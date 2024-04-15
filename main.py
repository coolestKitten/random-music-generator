import pysine as snd
import random as rm

note1 = 440.0
note2 = 660.0
note3 = 990.0
note4 = 1485.0
note5 = 2227.5
note6 = 3341.25
note7 = 5011.875


## Transition matrix. Determines what is the probability of making a certain transition
TransitionMatrix = [[0.5, 0.2, 0.3],[0.4, 0.2, 0.4],[0.2, 0.6, 0.2]]



# snd.sine(frequency=440.0, duration=0.3) 
# snd.sine(frequency=660.0, duration=0.3) 
# snd.sine(frequency=990.0, duration=0.3)  
# snd.sine(frequency=1485.0, duration=0.3) 
# snd.sine(frequency=2227.5, duration=0.3) 
# snd.sine(frequency=3341.25, duration=0.3) 
# snd.sine(frequency=5011.875, duration=0.3) 