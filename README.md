# Generador de Certificados Autofirmados

Este repositorio incluye un script de Python que facilita la generación de certificados autofirmados y claves privadas utilizando la biblioteca OpenSSL.

## *Descripción*

El archivo `generate_certificate.py` es un script que brinda una interfaz CLI (Interfaz de Línea de Comandos) para generar pares de claves RSA de 4096 bits y un certificado X.509 autofirmado con un período de validez de 1 año. Los certificados y claves generados se almacenan en archivos PEM.

## *Características*

* Generación de clave RSA de 4096 bits.
* Creación de certificado X.509 autofirmado.
* Validez del certificado de 1 año.
* Almacenamiento de claves y certificados en formato PEM.

## *Requisitos*

Para ejecutar este script necesitas:

* Python 3
* PyOpenSSL

Puedes instalar PyOpenSSL usando pip:

pip install pyopenssl
