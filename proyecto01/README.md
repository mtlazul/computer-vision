# Proyecto 1 - Pareo de puntos de interés

En este repositorio se implementa un programa que puede aplicar algoritmos de pareo de puntos de interes en dos entradasque pueden ser imágenes, videos o un stream de cámara

## Dependencias

Para instalar las dependencias se pueden ejecutar los siguientes comandos:

    sudo apt install python3 python3-pip
    sudo pip3 install opencv-python opencv-contrib-python

## Uso

     keypoints.py [-h] [--akaze] [--brisk] [--kaze] [--orb] [--sift] [--surf] [--in1 IN1] [--in2 IN2]

Hay que seleccionar algún algoritmo para que el programa tenga una salida, sino solo se despliega la ayuda:

  -h, --help  show this help message and exit
  --akaze     Apply A-KAZE algorithm for feature matching
  --brisk     Apply BRISK algorithm for feature matching
  --kaze      Apply KAZE algorithm for feature matching
  --orb       Apply ORB algorithm for feature matching
  --sift      Apply SIFT algorithm for feature matching
  --surf      Apply SURF algorithm for feature matching
  --in1 IN1   First input of the feature matching algorithm. Can be a video
              device, image or video file
  --in2 IN2   Second input of the feature matching algorithm. Can be a video
              device, image or video file

El valor por defecto de in1 e in2 es el dispositivo de video
`/dev/video0`
Otros dispositivos se pueden pasar por linea de comandos:
`./keypoints.py --orb --in1 /dev/video0 --in2 /dev/video1`
También se puede pasar la ruta de un archivo de video o imagen como entrada:
`./keypoints.py --orb --in1 /dev/video0 --in2 serway_book.jpg`

Las referencias de los algoritmos utilizados se encuentran en el arkdown dentro de la carpeta de cada algoritmo
