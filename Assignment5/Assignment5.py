#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
import numpy as np
#-import psychopy functions
from psychopy import core, gui, visual, event
#-import file save functions
import json
#-(import other functions as necessary: os...)
import os

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
# print (os.getcwd())
main_dir = os.getcwd()

#-define the directory where you will save your data
data_dir = os.path.join(main_dir, 'data')

#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir, 'images')

#-check that these directories exist
os.path.isdir(image_dir)
if not os.path.isdir(main_dir):
    raise Exception("Could not find the path!")
if not os.path.isdir(image_dir):
    raise Exception("Could not find the path!")
if not os.path.isdir(data_dir):
    raise Exception("Could not find the path!")

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
#get date and time
#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
nTrails = 10
nBlocks = 2

#-stimulus names (and stimulus extensions, if images) *
cats = ['faces']*10 
imgs = ['im1.png', 'im2.png', 'im3.png', 'im4.png', 'im5.png','im6.png','im7',
'im8','im9','im10']

#-stimulus properties like size, orientation, location, duration *
stimSize = [200,200]
stimDur = 1
stimOrient = [10]

#-start message text *
startMessgae = "Welcome to the experiment, press any key to start"

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
#pics = ['face01.jpg','face02.jpg','face03.jpg','face04.jpg',
#'face05.jpg','face06.jpg','face07.jpg','face08.jpg','face09.jpg','face10.jpg']
#'face' + str(number) + '.jpg'
pics = []
for i in range(1,11):
    if i != 10:  
        pics.append('face' + '0' + str(i) + '.jpg')
    elif i == 10:
            pics.append('face' + str(i) + '.jpg')
#print(pics)

ims_in_dir = sorted(os.listdir(image_dir))
#os.listdir(image_dir)
for pic in pics:
    if pics == ims_in_dir:
        print(pic + ' was found!')
if not pics == ims_in_dir:
    raise Exception("The image lists do not match up!")

#-create counterbalanced list of all conditions *
catimgs = list(zip(cats,imgs))

#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is correct") *
corrResp = []
corrResp = np.zeros(20)

#-create an empty list for participant responses (e.g., "on this trial, response was a X") *
partResp = []
partResp = np.zeros(20)

#-create an empty list for response accuracy collection (e.g., "was participant correct?") *
accuResp = []
accuResp = np.zeros(20)

#-create an empty list for response time collection *
RespTime = []
RespTime = np.zeros(20)

#-create an empty list for recording the order of stimulus identities *
stiId = []
stiId = np.zeros(20)

#-create an empty list for recording the order of stimulus properties *
stiPro = []
stiPro = np.zeros(20)

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for block in range(nBlocks):
    #-present block start message
    print('Welcome to Block' + str(block+1))
    #-randomize order of trials here *
    np.random.shuffle(catimgs)
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for trail in range(nTrails):
        print ('Trail Number' , str(trail+1))
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
#-quit experiment
