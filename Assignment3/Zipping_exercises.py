#Zipping exercises
first_order=[]
second_order=[]

faces=['face1.png','face2.png','face3.png','face4.png','face5.png']*5
houses=['house1.png','house2.png','house3.png','house4.png','house5.png']*5

first_order.extend(faces)
first_order.extend(houses)
first_order.extend(faces)
first_order.extend(houses)


face_s=['face1.png','face2.png','face3.png','face4.png','face5.png']*5
house_s=['house1.png','house2.png','house3.png','house4.png','house5.png']*5

second_order.extend(house_s)
second_order.extend(face_s)
second_order.extend(house_s)
second_order.extend(face_s)


post_cues=['cue1']*50+['cue2']*50
face_house = list(zip(first_order,second_order,post_cues))

np.random.shuffle(face_house)
print(face_house)
print(len(face_house))
