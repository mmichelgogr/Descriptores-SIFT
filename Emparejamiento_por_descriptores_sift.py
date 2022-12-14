'''EQUIPO:
Karla González,
Jorge Chávez,
Mariana Gómez'''

!pip uninstall opencv-python -y
!pip install opencv-contrib-python==3.4.2.17 --force-reinstall


import cv2
import matplotlib.pyplot as plt
import numpy as np
from google.colab.patches import cv2_imshow

fotos = []
f1 = cv2.imread("0001.jpg", 0)
fotos.append(f1)
f2 = cv2.imread("0002.jpg", 0)
fotos.append(f2)
f3 = cv2.imread("0003.jpg", 0)
fotos.append(f3)
f4 = cv2.imread("0004.jpg", 0)
fotos.append(f4)
f5 = cv2.imread("0005.jpg", 0)
fotos.append(f5)
f6 = cv2.imread("0006.jpg", 0)
fotos.append(f6)
f7 = cv2.imread("0007.jpg", 0)
fotos.append(f7)
f8 = cv2.imread("0008.jpg", 0)
fotos.append(f8)
f9 = cv2.imread("0009.jpg", 0)
fotos.append(f9)
f10 = cv2.imread("0010.jpg", 0)
fotos.append(f10)
f11 = cv2.imread("0011.jpg", 0)
fotos.append(f11)
f12 = cv2.imread("0012.jpg", 0)
fotos.append(f12)
f13 = cv2.imread("0013.jpg", 0)
fotos.append(f13)
print(len(fotos))

parejas = []
def sift_matches(img1, img2):
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    matches = cv2.BFMatcher().knnMatch(des1, des2, k=2)

    good = [[m] for m, n in matches if m.distance < 0.8*n.distance]
    img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, matchesMask=None)

    if len(good) > 35:
      print("Emparejameinto | Puntos en común: " + str(len(good)))
      parejas.append(img3)
      cv2_imshow(img3)
    else:
      print("x Emparejameinto | Puntos en común: " + str(len(good)))

for i in range(0, 13):
  for j in range(i+1,13):
    sift_matches(fotos[i], fotos[j])
  for k in range(0, i):
    sift_matches(fotos[i], fotos[k])
  print("_____________________________________")

print(len(parejas))

lineas_horizontales = 0
for imagen in parejas:
  edges = cv2.Canny(imagen,50,150,apertureSize = 3)
  lines = cv2.HoughLines(edges,1,np.pi/180,200)
  for coord in lines:
    for i in range(0, len(coord)):
      if coord[i][1] > 2.61799 or coord[i][0] < 3.66519:
        #print(str(coord[0][1]))
        lineas_horizontales += 1

  if(lineas_horizontales > 80):
    print(str(lineas_horizontales))
    cv2_imshow(imagen)
    print("__________________________________")
