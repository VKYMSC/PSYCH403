from psychopy import gui
from psychopy import core
import os
from psychopy import visual, monitors, event
import numpy as np

mon = monitors.Monitor('myMonitor', width=38.1, distance=60)
mon.setSizePix([1440,900])
win = visual.Window(monitor=mon)
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

fix_text = visual.TextStim(win, text='+')
start_msg = "Welcome to the experiment!"
block_msg = "Please wait until next image showed up!"
end_trial_msg = "End of trial."

stims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg', 'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']
my_image = visual.ImageStim(win)
nTrials = 3

waitTimer = core.Clock()
stimTimer = core.Clock()

fixTime = .5
stimTime = 1.0

refresh = 1.0/60.0

fixFrames = int(fixTime / refresh) 
stimFrames = int(stimTime / refresh) 

totalFrames = int(fixFrames + stimFrames + fixFrames)

start_text = visual.TextStim(win, text=start_msg)
start_text.draw()
win.flip()
core.wait(3)

nBlocks=2
nTrials=3

for block in range(nBlocks):
    block_text = visual.TextStim(win, text=block_msg)
    block_text.draw()
    win.flip()
    core.wait(1)

    for trial in range(nTrials):
        my_image.image = os.path.join(image_dir,stims[trial])
        win.flip()
        core.wait(1)
        #-draw fixation
        for nFrames in range(totalFrames):
            if 0 <= nFrames <= fixFrames:
                fix_text.draw()
            #-flip window
                win.flip()
            #-wait time (stimulus duration)

        #-draw image
            if fixFrames < nFrames <= (fixFrames+stimFrames):  
                if nFrames == fixFrames + 1:
                    imgStartime = waitTimer.getTime()
                my_image.draw()
        #-flip window
                win.flip()
        #-wait time (stimulus duration)
        
            if (fixFrames+stimFrames) < nFrames < totalFrames:  
                if nFrames == fixFrames + stimFrames + 1:
                    imgEndtime = waitTimer.getTime()
        #-draw end trial text
                endtrial_text = visual.TextStim(win, text=end_trial_msg)
                endtrial_text.draw()
        #-flip window
                win.flip()

    print("Image duration was {} seconds.".format(imgEndtime - imgStartime))
win.close()
