import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from sklearn.neighbors import KNeighborsClassifier


video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# Load pre-trained KNN model
with open('data/names.pkl', 'rb') as f:
    LABELS = pickle.load(f)

with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

# Load background image
img_background = cv2.imread("background.png")

# Define CSV header
column_names = ['NAMES', 'TIME']

# Create Attendance directory if it doesn't exist
if not os.path.exists("Attendance"):
    os.makedirs("Attendance")

while True:
    ret, frame = video.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    attendance_records = []

    for (x, y, w, h) in faces:
        crop_img = frame[y : y + h, x : x + w, :]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
        output = knn.predict(resized_img)

        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        current_time = datetime.fromtimestamp(ts).strftime("%H:%M:%S")
        attendance_records.append([str(output[0]), current_time])

        # Draw label and rectangle on detected face
        cv2.putText(frame, str(output[0]), (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)

    # Show the output frame
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)

    if k == ord('o'):
        filename = f"Attendance/Attendance_{date}.csv"
        file_exists = os.path.isfile(filename)

        with open(filename, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(column_names)
            writer.writerows(attendance_records)

    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
