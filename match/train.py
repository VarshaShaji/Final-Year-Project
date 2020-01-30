import face_recognition
import glob
import pickle
import time
flag=0
i=1
j='k'
photos=[]
known=[]
mylist = [f for f in glob.glob("../uploads/*.jpg")]
print(mylist)
while (flag==0):
 j='../uploads/'+j+str(i)+'.jpg'
 if j in mylist:
  time.sleep(2)
  print(j)
  photos.append(face_recognition.load_image_file(j))
  j='k'
  known.append(face_recognition.face_encodings(photos[i-1])[0])
  i=i+1
  with open('dataset_faces.dat', 'wb') as f:
    pickle.dump(known, f)
 else:
     j='k'
     mylist = [f for f in glob.glob("../uploads/*.jpg")]
     
  
