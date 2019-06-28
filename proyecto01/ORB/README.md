# Implementación del algoritmo ORB

El siguiente ejemplo muestra cómo utilizar la librería ORB (*Oriented FAST and Rotated BRIEF*), la cual básicamente es una fusión de detector de puntos de interés FAST y el descriptor BRIEF junto con múltiples modificaciones, con el objetivo de mejorar el rendimiento. Igualmente, se actualizó el código para que este fuera capaz de emparejar descriptores de puntos de interés entre *frames* consecutivos, tal y como lo sugiere la segunda referencia.

Referencias:
* [ORB (Oriented FAST and Rotated BRIEF)](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_orb/py_orb.html)

* [Brute-Force Matching with ORB Descriptors](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_matcher/py_matcher.html)
