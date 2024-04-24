import cv2


# Definiamo i path necessari
image_path = 'img/tshirt02.jpg'
haarcasc_path = 'haarcascade_frontalface_default.xml'


# Creiamo la haar cascade
face_cascade_class = cv2.CascadeClassifier(haarcasc_path)
# Leggiamo l’immagine
test_image = cv2.imread(image_path)
gray_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

# Riconosciamo i volti nelle immagini
checked_faces = face_cascade_class.detectMultiScale(
    gray_image,
    scaleFactor=1.2,
    minNeighbors=3,
    minSize=(10, 10)
)

# Tracciamo un rettangolo intorno ai volti
for (x, y, w, h) in checked_faces:
    cv2.rectangle(test_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Faces found", test_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Face_EM_final.jpg',test_image)