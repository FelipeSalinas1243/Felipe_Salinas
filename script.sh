#!/bin/bash

# Mostrar los archivos del directorio y su detalle
ls -l

# Mostrar la ruta del directorio actual
echo "Estamos ubicados en: $(pwd)"

# Cambiar los permisos del archivo a root
sudo chown root script.sh
