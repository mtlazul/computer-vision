# Implementación del algoritmo KAZE

El siguiente ejemplo muestra cómo utilizar la librería disponible en la Open-CV, KAZE para detectar puntos de interes y extraer descriptores. La aplicación encuentra los puntos de interés en un par de imágenes junto con una matríz homográfica, las empareja y cuenta el número de correspondencias que coinciden con la homografía dada (*inliers*). De la misma forma, se ha modificado dicha aplicación, con el fin que ejecute el procesamiento asociado con la captura de video.

Referencia:
* [KAZE class reference](https://docs.opencv.org/trunk/d3/d61/classcv_1_1KAZE.html)

