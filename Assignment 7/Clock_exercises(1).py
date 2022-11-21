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
nTrials = 4

start_text = visual.TextStim(win, text=start_msg)
start_text.draw()
win.flip()
core.wait(3)

wait_timer = core.Clock() #define a clock
wait_timer.getTime() #get time on the clock

for trial in range(nTrials):
    my_image.image = os.path.join(image_dir,stims[trial])

### Wait exercises
#=====================
#START TRIAL
#===================== 
    block_text = visual.TextStim(win, text=block_msg)
    block_text.draw()
    win.flip()
    core.wait(1)
    #-draw fixation
    fix_text.draw()
    #-flip window
    win.flip()
    #-wait time (stimulus duration)
    core.wait(.5)

    #-draw image
    my_image.draw() 
    #-flip window
    win.flip() 
    imgStartTime = wait_timer.getTime()
    #-wait time (stimulus duration)
    core.wait(2)
    imgEndTime = wait_timer.getTime()
        
    #-draw end trial text
    endtrial_text = visual.TextStim(win, text=end_trial_msg)
    endtrial_text.draw()
    #-flip window
    win.flip()
    #-wait time (stimulus duration)
    core.wait(1)
    
    print(" Image Duration was {} seconds".format(imgEndTime - imgStartTime))
    
win.close()
