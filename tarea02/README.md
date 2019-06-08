# Tarea 2 - Segmentación a nivel de imagen

En este repositorio se implementa un programa que realiza captura de la cámara con OpenCV y realiza uno de tres algoritmos de segmentación a nivel de imágen.


## Dependencias

Para instalar las dependencias se pueden ejecutar los siguientes comandos:

    sudo apt install python3 python3-pip
    sudo pip3 install opencv-python opencv-contrib-python scikit-image

## Uso

     ./segmentation.py [-h] [--ms] [--ws] [--slic]

Por defecto solo se despliega la cámara. Para aplicar algún algoritmo utilice alguna de las siguientes opciones:

      -h, --help  Mostrar el mensage de ayuda y salir
      --ms        Aplicar el algoritmo de mean shift al stream de la cámara
      --ws        Aplicar el algoritmo de watershed al stream de la cámara
      --slic      Aplicar el algoritmo de simple linear iterative clustering al stream de la cámara
