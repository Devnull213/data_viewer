# Data Viewer

App diseñada para realizar toma de datos en instalaciónes con  equipos de respaldo de energía y visualización de los datos obtenidos por parte del cliente.

## Pre-requisitos 📋
```
Python3
Postgresql
```

## Instalación 🔧

1. Clona este repositorio localmente
```
git clone https://github.com/Guerra-Defranchi/data_viewer.git
```
2. Crea un entorno virtual y activalo 
```
python3 -m venv venv
source  /venv/bin/activate
```
3. Instala las dependencias necesarias
```
pip install -r requirements.txt
```
4. Crea una base de datos en Postgresql
```
CREATE DATABASE data_viewer;
```
5. Modificar credenciales en data_viewer/settings.py 
```
'NAME': 'data_viewer',
'USER': 'tu usuario postgresql',
'PASSWORD': 'tu contraseña postgresql',
```
6. Accede a la aplicación mediante 
```
http://localhost:8000
```
## Construido con 🛠️
* [Django](https://www.djangoproject.com/)
* [Jquery](https://jquery.com/)
* [Chart.js](https://www.chartjs.org/)

## Imagenes 

<img src="/assets/img/data_viewer_landingpage.png" width="900" height="500">

<img src="/assets/img/data_viewer_admin_main.png" width="900" height="500">

<img src="/assets/img/data_viewer_roof.png" width="900" height="500">

<img src="/assets/img/data_viewer_tech_view.png" width="900" height="500">


