import face_recognition
import pickle
with open('dataset_faces.dat', 'rb') as f:
	known = pickle.load(f)
uencode=known[len(known)-1]
for i in range(0,len(known)-1):
 r=face_recognition.compare_faces([known[i]],uencode)
 if r[0]:
    print('HIT:'+'k'+str(i+1))
