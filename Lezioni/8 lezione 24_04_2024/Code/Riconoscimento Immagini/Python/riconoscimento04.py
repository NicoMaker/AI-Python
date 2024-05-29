
import cv2
f_cascade = cv2.CascadeClassifier("../XML/haarcascade_frontalface_default.xml")
e_cascade = cv2.CascadeClassifier("../XML/haarcascade_eye.xml")
image = cv2.imread("../img/elodie2.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
"""gray: Questo è l'input dell'immagine in scala di grigi su cui verrà eseguito il rilevamento. 
Prima di rilevare i volti, è una pratica comune convertire l'immagine a scala di grigi poiché semplifica 
il processo di rilevamento dei bordi e di altre caratteristiche.
1.3: Questo parametro specifica il fattore di scala. Il fattore di scala controlla 
quanto l'immagine viene ridimensionata ad ogni livello della piramide dell'immagine durante 
il processo di rilevamento. Un valore più piccolo consente di rilevare oggetti più piccoli,
ma aumenta anche il tempo di calcolo. Un valore tipico è compreso tra 1.1 e 1.5.

5: Questo parametro specifica il numero minimo di vicini richiesti per considerare un'area come volto.
 Questo parametro influenza la sensibilità del rilevatore: un valore più alto 
 riduce il numero di falsi positivi, ma potrebbe far perdere anche alcuni volti. Un valore tipico
   è compreso tra 3 e 6."""

faces = f_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    image2 = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image2[y:y+h, x:x+w]
    eyes = e_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('img',image2)
cv2.waitKey(0)
cv2.destroyAllWindows()