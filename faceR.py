import face_recognition

# Load the jpg files into numpy arrays
a_img = face_recognition.load_image_file("a.jpg")
b_img = face_recognition.load_image_file("b.jpg")
c_img = face_recognition.load_image_file("c.jpg")
d_img = face_recognition.load_image_file("d.jpg")
e_img = face_recognition.load_image_file("e.jpg")
unknown_image = face_recognition.load_image_file("unknown.jpg")

# known images are stored in 

known_images= ['A','B','C','D','E']

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
try:
    a_face_encoding = face_recognition.face_encodings(a_img)[0]
    b_face_encoding = face_recognition.face_encodings(b_img)[0]
    c_face_encoding = face_recognition.face_encodings(c_img)[0]
    d_img_encording = face_recognition.face_encodings(d_img)[0]
    e_img_encording = face_recognition.face_encodings(e_img)[0]


    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

known_faces = [
    a_face_encoding,
    b_face_encoding,
    c_face_encoding,
    d_img_encording,
    e_img_encording
]

# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

#Printing the result 

flag=0
i = results.index(True)
if(i>-1):
    print("The unknown image  given is detected as ",known_images[i])
    flag=1
if flag == 0:
    print("The image cant dectected because it is not matched anybody in our database")

