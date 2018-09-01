import io
import cv2
import face_recognition
import numpy as np
from PIL import Image
from flask import Flask, request, Response
from flask_restful import Resource, Api

face_locations = []
known_face_encodings = []
known_face_names = []
i = 0

def generate_name():
    global i
    i += 1
    return "Person_" + str(i)

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
    <form enctype="multipart/form-data" method="post">
        <input name="image" type="file" />
        <input type="submit" />
    </form>
</body>
</html> """
        return Response(html, mimetype='text/html')

    def post(self):
        stream = request.files['image'].stream
        image = Image.open(stream)
        frame = np.array(image.convert('RGB'))
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
            else:
                name = generate_name()
                known_face_encodings.append(face_encodings[0])
                known_face_names.append(name)
            face_names.append(name)

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 15), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_PLAIN
            cv2.putText(frame, name, (left + 6, bottom - 3), font, 1.0, (255, 255, 255), 1)

        new_image = Image.fromarray(frame)

        with io.BytesIO() as output:
            new_image.save(output, 'png')
            data = output.getvalue()
        return Response(data, mimetype='image/jpeg')

api.add_resource(Test, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')