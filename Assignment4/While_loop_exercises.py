#Question1
iteration = 0

while iteration < 20:
    iteration = iteration + 1
    if iteration < 10:
        print('%i, image1.png' %iteration)
        
    elif iteration < 20:
        print('%i, image2.png' %iteration)

#Question2
response = ""

while response != '1' and response != '2':
   print("Showing an image")
   if response == '1' and response == '2':
       break
           
#Question3
response = ""
failsafe = -1

while response != '1' and response != '2':
   failsafe = failsafe + 1
   if failsafe == 5:
       break
   print(failsafe)
   if response == '1' and response == '2':
        respone = True
        break

      
