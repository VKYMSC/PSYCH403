'''
INTRODUCTION
Name: Ruihan Weng
Student ID: 1575866

The experiment is designed to find the different between culture attention to the given events according to my Psych 341 class based on Dr. Chua et al. (2005)'s finding .
And I'm aimed to find how Westerners or Easterner's culture background effect participant's focus to the main object or the surroundings (whether they see on the object first or the surroundings first)
Accoding to Chua et al.(2005), The Easterner’s will pay more attention to the surroundings and Westerners will pay more attention to the main object.

'''

#=====================
#IMPORT MODULES
#=====================
from psychopy import visual, monitors, core, event
import os
from psychopy import gui
import pandas as pd
import numpy as np

#=====================
#PATH SETTINGS
#=====================
directory = os.getcwd()
path = os.path.join(directory)
data = os.path.join(directory, 'dataFile')
if not os.path.exists(data):
    os.makedirs(data)
image_dir = os.path.join(directory,'image')

#=====================
#COLLECT PARTICIPANT INFO
#=====================
exp_info = {'Subject Number':'', 
            'Gender':('Female', 'Male', 'Others'),
            'Age': '',
            'Which type of culture background can be most closely describe where you were raised?':('Western','Eastern')}

myDlg = gui.DlgFromDict(dictionary=exp_info) 
filename = (str(exp_info['Subject Number']) + "_" +(str(exp_info['Which type of culture background can be most closely describe where you were raised?'])) + '_outputFile.csv')

# check the dialog box
if exp_info['Age'].isdigit() == False: # enther an invalid age
    # create another dialog box showing an error message
    err_dlg = gui.Dlg(title='Error Message') 
    # error message
    err_dlg.addText('Please enter a valid number.') 
    # show the dialog box
    err_dlg.show() 
    # quit the experiment
    core.quit() 

if int(exp_info['Age']) > 120: # enter an impossible age
    # create another dialog box showing an error message
    err_dlg = gui.Dlg(title='error message')
    err_dlg.addText('%d year olds is not a valid age' % int((exp_info['Age'])))
    #show the dialog box
    err_dlg.show()
    # quit the experiment
    core.quit()
    
if exp_info['Subject Number'].isdigit() == False: # enther an invalid subject number
    # create another dialog box showing an error message
    err_dlg = gui.Dlg(title='Error Message') 
    # error message
    err_dlg.addText('Please enter a valid subject number.') 
    # show the dialog box
    err_dlg.show() 
    # quit the experiment
    core.quit() 

#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
# prepare the list to store the data for futher use
final_list = []
Subject_Number = exp_info['Subject Number']
block_num_list = []
response_list = []
reaction_time_list = []

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
mon = monitors.Monitor('myMonitor', width=38.1, distance=60) 
mon.setSizePix([1440,900])
win = visual.Window(monitor=mon,size = (900,600) )
my_image = visual.ImageStim(win, units='pix', size = (900,600))

stims = ['sky01.jpg','sky02.jpg','sky03.jpg','sky04.jpg', 'sky05.jpg','sky06.jpg']
nTrials = 6
nBlocks = 5

trial_timer = core.Clock()
#=====================
#START EXPERIMENT
#=====================
# present the start message and the first step insrruction message
start_message = visual.TextStim (win,"Welcome to the experiment! \n Press any keys to continue.")
start_message.draw()
win.flip()
event.waitKeys()

instructText = visual.TextStim (win, 'Please indicate the first item you see according the instruction showed after the short video.\n  Press any keys to continue.')
instructText.draw()
win.flip()
event.waitKeys()

#=====================
#BLOCK SEQUENCE
#=====================
# begain the trail for each block
for block in range(nBlocks):
    instructText.text = "Press any key to begin Block " + str(block+1)
    instructText.draw()
    win.flip()
    event.waitKeys()
    #shuffle the stims
    np.random.shuffle(stims)
    
    #=====================
    #TRIAL SEQUENCE AND START TRIAL
    #===================== 
    for trial in range(nTrials): 
        #=====================
        #START TRIAL
        #===================== 
        #-set stimuli and stimulus properties for the current trial
        my_image.image = os.path.join(image_dir,stims[trial])
        # draw the image from the file and let the image automaticlly show, to make the trials combined and worked as a short video
        my_image.draw() 
        win.flip()
        core.wait(0.3) #make the wait time shorter to make the combination of the trials more likely to a video
        
    # block number
    block_num = block + 1
    #print('block_num',block_num)
    
    # show the instruction messgae for the participant about how to response to what they saw
    fix_text = visual.TextStim(win,text= "Press 'B' if you notice the bird first during the video \n 'S' if you see sky first \n 'A' if you see Bird and Sky at the same time")
    fix_text.draw()
    win.flip()
    # reset the timer for each block  
    trial_timer.reset()
    # collect participant's input
    key = event.waitKeys(keyList=['b', 's', 'a'])
    if key[0] == 'b':
        response = "Bird"
    elif key[0] == 's':
        response = "Sky"
    else:
        response = "See Bird and Sky at the same time"
    # find the reaction time after the participant indicatio what they saw after each block
    reaction_time = trial_timer.getTime()
    #print(reaction_time)
    
    result = {'block_num':block_num, 'response': response, 'reaction_time': reaction_time}
    final_list.append(result)

#print(final_list)

# append the result to the final list
for result in final_list:
    block_num_list.append(result["block_num"])
    response_list.append(result["response"])
    reaction_time_list.append(result["reaction_time"])

df = pd.DataFrame(data={"Subject Number": Subject_Number, "Main Object": "Bird", "block_num":block_num_list, "response":response_list, "reaction_time":reaction_time_list})
# creat csv file for each paticipant and save each participants data into a file
df.to_csv(os.path.join(data, filename), sep=',', index=False)

#======================
# END OF EXPERIMENT
#======================  
win.close()


