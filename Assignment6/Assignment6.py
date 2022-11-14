from psychopy import gui
from psychopy import core
from datetime import datetime
import os
from psychopy import visual, monitors, event
import numpy as np

## Dialog box exercises
## Part 1
exp_info = {'subject_nr':'', 
            'age':'',
            'handedness':('right','left','ambi'), 
            'gender':'',
            'session':1}

print(exp_info)

## Part 2
#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
print("All variables have been created! Now ready to show the dialog box!")
my_dlg = gui.DlgFromDict(dictionary=exp_info,
                        title="subject info",
                        fixed=['session'],
                        order = ['session','subject_nr', 'age', 'gender', 'handedness'])

#check the correctness of the entered data
#if exp_info['subject_nr'] ==0: #nothing entered
#    err_dlg = gui.Dlg(title='error message') 
#    err_dlg.addText('Enter a valid subject number!') #Error message
#    err_dlg.show() #show the dlg
#    core.quit() #quit the experiment
#if exp_info['age'] < 18: #age is below 18
#    err_dlg = gui.Dlg(title='error message')
#    err_dlg.addText('%d year olds cannot give consent!' % (exp_info['age'])) #Error message
#    err_dlg.show() #show the dlg
#    core.quit() #quit the experiment

#get date and time
date = datetime.now() 
print(date)
exp_info['date'] = str(date.hour)+ '-'+ str(date.day) + '-'+ str(date.month) + '-'+ str(date.year)
print(exp_info['date'])

#create a filename for the data
filename = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'
print(filename)

#define where to store the data
main_dir = os.getcwd() 
sub_dir = os.path.join(main_dir,'sub_info',filename)


## Monitor and window exercises

#Question 1: How does changing "units" affect how you define your window size?
#Change the uniit can affect the window size.abs
#We can use various units through Psychypy. The choice of the unit can be deterimined by devices and conditions you use.
#For example, when doing the demo, we usually use ‘norm’ and ‘height’ for units.
#Since these units can naturally change when adjusting the window size.
#Consider the experiment could be done in various devices (e.g. smart phone), using the height unit means
#the experiment window can be changde relativedly with participants'devices' screen.

#Question 2: How does changing colorSpace affect how you define the color of your window? Can you define colors by name?
#Changing the colorSpace can change the color of the window. You can access various colour using PsychoPy Builder.
#And explore the value of color in different colorSpaces.
#We can use colorSpace: RGB, DKL, HSV, LMS. But the HSV colorSpace is device specific.
#The colors can be defined by names using strings. You can set the colour
#through the words, hex value.

#Question 3:
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=38.1, distance=60) 
mon.setSizePix([1440,900])
mon.save()
#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon,
                    size=(800,800),
                    color=[-1,-1,-1],
                    units='pix',
                    fullscr=True)
                    

## Stimulus exercises

#Question 1

my_image = visual.ImageStim(win, units='pix', size = (400,400))

main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

stims = ['face01.jpg','face02.jpg','face03.jpg']
nTrials=3 

for trial in range(nTrials): 
    my_image.image = os.path.join(image_dir,stims[trial])
    my_image.draw() 
    win.flip()
    event.waitKeys()
    
win.close()

#Question2
mon = monitors.Monitor('myMonitor', width=38.1, distance=60) 
mon.setSizePix([1440,900])
mon.save()
thisSize = mon.getSizePix()
thisWidth = thisSize[0]
thisHeight = thisSize[1]

win = visual.Window(monitor = mon, fullscr = True)

fix_text = visual.TextStim(win, text = '+')
my_image = visual.ImageStim(win, units='pix', size = (400,400)) #the size of the pic will be 400*400 in unit of pixel
nTrials = 4
image_dir = os.path.join(main_dir, 'images')
stims = ['face01.jpg', 'face02.jpg', 'face03.jpg','face04.jpg']

horizMult = [-1, 1, 1, -1]
verMult = [1, 1, -1, -1]

for trial in range(nTrials):
    my_image.image = os.path.join(image_dir, stims[trial])
    #divided the width and height by 4 to calculate window locations
    my_image.pos = (horizMult[trial] * thisWidth/4, verMult[trial] * thisHeight/4)
    my_image.draw()
    fix_text.draw()
    win.flip()
    event.waitKeys()

win.close()
 
#Question 3
fix_text = visual.TextStim(win, text='+')

#Question 4
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
mon = monitors.Monitor('myMonitor', width=38.1, distance=60) 
mon.setSizePix([1440,900])
mon.save()

main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')
my_image = visual.ImageStim(win, units='pix', size = (400,400))


#-define experiment start text unsing psychopy functions
start_msg = "Welcome to my experiment!"

#-define block (start)/end text using psychopy functions
block_msg = "Press any key to continue to the next block."
end_trial_msg = "End of trial"

#-define stimuli using psychopy functions (images, fixation cross)
stims = ['face01.jpg', 'face02.jpg', 'face03.jpg','face04.jpg']
fix_text = visual.TextStim(win,text='+')

#=====================
#START EXPERIMENT
#=====================
#-present start message text
start_text = visual.TextStim(win, text=start_msg)
start_text.draw()
win.flip()

#-allow participant to begin experiment with button press
event.waitKeys()
#=====================
#BLOCK SEQUENCE
#=====================
nBlocks=2
nTrials=3

#-for loop for nBlocks
for block in range(nBlocks):
    #-present block start message
    block_text = visual.TextStim(win, text=block_msg)
    block_text.draw()
    win.flip()
    event.waitKeys()
    #-randomize order of trials here
    np.random.shuffle(stims)
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        my_image.image = os.path.join(image_dir, stims[trial])
        #=====================
        #START TRIAL
        #=====================  
        #-draw fixation
        fix_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        event.waitKeys()
        
        #-draw image
        my_image.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        event.waitKeys()
        
        #-draw end trial text
        endtrial_text = visual.TextStim(win, text=end_trial_msg)
        endtrial_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        event.waitKeys()
        
#======================
# END OF EXPERIMENT
#======================        
#-close window
win.close()

