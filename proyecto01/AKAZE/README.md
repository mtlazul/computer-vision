# Implementación del algoritmo A-KAZE

El siguiente ejemplo muestra cómo utilizar la librería disponible en la Open-CV, A-KAZE para detectar y corresponder puntos de interés en dos imágenes. La aplicación encuentra los puntos de interés en un par de imágenes junto con una matríz homográfica, las empareja y cuenta el número de correspondencias que coinciden con la homografía dada (*inliers*). Posteriormente, se efectuaron las modificaciones necesarias con el objeto de realizar la tarea descrita, pero considerando capturas de video, tal y como se ha implementado a lo largo de las distintas librerías.

Referencia: [AKAZE local features matching](https://docs.opencv.org/3.4/db/d70/tutorial_akaze_matching.html)
