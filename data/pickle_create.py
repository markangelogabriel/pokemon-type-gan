import os
import random
all_image = []
train = ['(lp0']
test = ['(lp0']
ii = 1
for file in os.listdir(os.getcwd()+'/pokemon_jpg'):

    all_image.append((os.path.join("aS'pokemon_jpg", file[:-4])+str("'")))
#all_image.append('p'+str(1))
#i+1
random.seed(10)
while len(train) <= len(all_image) *0.8:
    train.append(random.choice(all_image))
    train.append('p'+str(ii))
    ii += 1
remaining = list(set(all_image)-set(train))
ii = 1
for image in remaining:
    test.append(image)
    test.append('p'+str(ii))
    ii += 1
#the 1st is S not as
train[1] = train[1][1:]
test[1] = test[1][1:]
train.append('a.')
test.append('a.')

export_train = '\n'.join(train)
export_test = '\n'.join(test)
trian_output = open('filenames.pickle','w')
trian_output.write(export_train)
trian_output.close

test_output = open('filenames(test).pickle','w')
#need to change the name before place into the test folder
test_output.write(export_train)
test_output.close
#both pickle files need to remove space between ( and lp0
