from psychopy import event, visual, monitors
from psychopy import core

mon = monitors.Monitor('myMonitor', width=38.1, distance=60)
mon.setSizePix([1440,900])
win = visual.Window(monitor=mon)

nTrials = 1

for trial in range(nTrials):
    core.wait(2)
    keys=event.getKeys()
    if keys:
        sub_resp = keys[0] #check the first response of press key
    print("the first response is", sub_resp)
#    print(keys)
    
win.close()
