import face_recognition
import cv2

face_locations = []

frame = face_recognition.load_image_file("eyeglasses.jpg")
face_locations = face_recognition.face_locations(frame)
#face_encodings = face_recognition.face_encodings(frame, face_locations)

for top, right, bottom, left in face_locations:
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    #cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    #font = cv2.FONT_HERSHEY_DUPLEX
    #cv2.putText(frame, "face", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

cv2.imshow('Photo', frame[:,:,::-1])
cv2.waitKey()

cv2.destroyAllWindows()