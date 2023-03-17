from syntacts import *
from time import sleep
import time 
from numpy import random as rnd
import pandas as pd 

session = Session()
session.open(18)   
sin = Sine(100)      # 100 Hz Sine wave
asr = ASR(0.0025, 0.02, 0.0025)

sig1 = sin * asr  # duration is infinite

# Inter stimulus intervals 
isi = [0.1,0.08,0.06,0.04,0.02]
response = []
channel_first = []
trial = []
participanID = 'Ptx_' + str(rnd.randint(0,10))+ str(rnd.randint(0,10))+ str(rnd.randint(0,10))

### Play signals 
# Do not need to stop sig2 because it is finite
# Loop through a few trials 
maxNumbTrials = 40
for idx in range(maxNumbTrials):

    print('Trial: ' + str(idx) + ' out of: ' + str(maxNumbTrials))

    # later make channel random
     
    chan1 = rnd.randint(0,2)
    channel_first.append(chan1)
    session.play(chan1, sig1) # plays sig 1 on channel 0
    sleep(sig1.length)  

    # Later make this random 
    if idx < 2:
        sleep(0.5)
        print('ISI: ' + str(0.5))
    elif idx > 2 and idx < 5:
        sleep(0.2)
        print('ISI: ' + str(0.2))
    else:
        i = rnd.randint(0,4)
        sleep(isi[i])
        print('ISI: ' + str(isi[i]) + ' chan: ' + str(chan1))


    # later make channel random 
    if chan1 == 0:
        chan2 = 1
    else:
        chan2 = 0

    session.play(chan2, sig1) # plays sig1 on channel 1
    sleep(sig1.length)    # sig2 plays for its length of 0.3 seconds

    # wait for keypress then continue
    resp = input("Press Enter to continue...")
    if resp == chan1:
        response.append(1)
    else:
        response.append(0)

session.close()  

# Save data 
data_in_dict = {'ParticipantID' : participanID,
                'Trial' : trial,
                'FirstChannel' : channel_first,
                'Response' : response,}

df = pd.DataFrame(data_in_dict)
df.to_csv(participanID + str(time.time())[0:5] + '.csv')