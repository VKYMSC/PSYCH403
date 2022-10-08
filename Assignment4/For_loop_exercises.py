##For loop exercises
#Question1

letters = ['R','U','I','H','A','N']

for letter in letters:
    print(letter)

myname = "Ruihan"
for letter in myname:
    print(letter)
    
    
#Question2    
letters = ['R','U','I','H','A','N']
count = -1
for letter in letters:
    count = count + 1
    print(letter)
    print(count)

#Question3
names = ["Amy","Rory","River"]
for name in names:
    print(name)
    for letter in name:
        print(letter)

#Question4
names = ["Amy","Rory","River"]
for name in names:
    print(name)
    count = -1
    for letter in name:
        count = count + 1
        print(letter)
        print(count)
