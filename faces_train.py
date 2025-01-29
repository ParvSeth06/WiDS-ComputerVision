import cv2 as cv
import numpy as np
import os

people = ['arijit', 'diljit', 'srk']
DIR = r"D:\WiDS'24\train_photos"
# if i dont wasnt to type out the list manually then use this method
# p=[]
# for i in os.listdir(r"D:\WiDS'24\train_photos") :
#     p.append(i)
# print(p)


haar_cascade =cv.CascadeClassifier('haar_face.xml')
features = []
labels = []


def create_train() :
    for person in  people :
        path = os.path.join(DIR,person)
        label = people.index(person)
        for img in os.listdir(path) :
            img_path = os.path.join(path,img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)

            for (x,y,w,h) in faces_rect :
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print("training done ----------------")

# print(f'length of features list = {len(features)}')
# print(f'length of labels list = {len(labels)}')
# now the training set is ready , so we can use the lists to train our model.

features = np.array(features, dtype='object')
labels =np.array(labels)
face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save("features.npy", features)
np.save("labels.npy", labels)




# we can save this model , and use it for other dataset



