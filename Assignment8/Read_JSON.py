from psychopy import core, event, visual, monitors
import numpy as np
import csv
import os
import json as json
import pandas as pd


mon = monitors.Monitor('myMonitor', width=38.1, distance=60)
mon.setSizePix([1440,900])
win = visual.Window(monitor=mon)

filename = 'savejson_Assignment8'
main_dir = os.getcwd()
data_dir = os.path.join(main_dir,filename)
#
#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists for responses
sub_resp = [[-1]*nTrials]*nBlocks
sub_acc = [[-1]*nTrials]*nBlocks
prob = [[-1]*nTrials]*nBlocks
corr_resp = [[-1]*nTrials]*nBlocks
resp_time = [[-1]*nTrials]*nBlocks
blocks = [[0, 0, 0, 0], [1, 1, 1, 1]] 
trials = [[0, 1, 2, 3], [0, 1, 2, 3]] 



#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

for block in range(nBlocks):
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 0 #arbitrary number for inaccurate response 
                                    #(should be something other than -1 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', prob[block][trial], 'correct response=', 
              corr_resp[block][trial], 'subject response=',sub_resp[block][trial], 
              'subject accuracy=',sub_acc[block][trial], 'reaction time=',
              resp_time[block][trial])

win.close()

data_as_list = [prob, corr_resp, sub_resp, sub_acc, resp_time]
print(data_as_list)

with open(data_dir, 'w') as sub_data:
    fieldnames = ['block', 'trial', 'problem','corr_resp','sub_resp','sub_acc', 'resp_time']
    data_writer = csv.DictWriter(sub_data, fieldnames=fieldnames)
    data_writer.writeheader()

    for block in range(nBlocks):
        data_as_dict = []
        for a,b,c,d,e,f,g in zip(blocks[block], trials[block], prob[block], corr_resp[block], sub_resp[block], sub_acc[block], resp_time[block]):
            data_as_dict.append({'block':a, 'trial':b, 'problem':c,'corr_resp':d,'sub_resp':e,'sub_acc':f, 'resp_time':g})
        print(data_as_dict)
        for iTrial in range(nTrials):
            data_writer.writerow(data_as_dict[iTrial])

df = pd.read_csv('savejson_Assignment8')
print(df)

acc_trials = df.loc[df['sub_acc'] == 1] 
print(acc_trials)
print(len(acc_trials)/len(df['sub_acc']))

without_respones = df.loc[df['sub_resp'] == -1] 
print(without_respones)
print(len(without_respones)/len(df['sub_resp']))
