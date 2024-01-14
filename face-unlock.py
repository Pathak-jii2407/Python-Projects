import cv2
import face_recognition

def face():
    known_faces = {
        "Saurav": face_recognition.load_image_file("F:\\FRIDAY\\pics\\1.jpg"),        
    }

    known_encodings = {}

    for name, img in known_faces.items():
        face_encoding_list = face_recognition.face_encodings(img)
        if face_encoding_list:
            known_encodings[name] = face_encoding_list[0]
        else:
            print(f"No face found in the image for {name}")

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()

        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for current_face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(list(known_encodings.values()), current_face_encoding)

            name = "unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = list(known_encodings.keys())[first_match_index]
                

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

face()