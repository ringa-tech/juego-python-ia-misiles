# **Misiles**
[![example](https://cdn.pixabay.com/photo/2014/09/11/12/45/spacecraft-441708_960_720.jpg)](https://www.ringa-tech.com/)

---
## **Información general**
Este repositorio contiene el código para el  juego de Misiles controlado por la cara usando [Facemesh](https://google.github.io/mediapipe/solutions/face_mesh.html), como fue creado en mi canal de Youtube:
[Ringa-Tech](https://youtu.be/_BjL6W71mWY)

---

## **Información Adicional:**

Este juego no puede ser ejecutado en terminales de subsistemas Linux. Cómo WSL, WSL2, Termux, entre otros. Debido a que hay problemas con los triggers. 
Se puede ejecutar pero es una tarea demasiado complicada. Te comparto está información de [Stackoverflow](https://stackoverflow.com/questions/65939167/problem-using-opencv-in-wsl-when-opening-windows) en caso de que lo quieras intentar.

---
## **Configuración**
El proyecto lo hice con Python 3.7.9

Pero mediaPipe acepta versiones desde 3.6, hasta 3.10.

<details><summary><b>Instalar en WINDOWS:</b></summary>

### ***Sigue los siguentes pasos:***

Revisar versión de Python:
```
python --version
```
Crear un ambiente virtual:
```
python3 -m virtualenv venv
```
Activar ambiente virtual:
```
.\venv\Scripts\activate
```
Actualizar pip:
```
python.exe -m pip install --upgrade pip
```
Para instalar las dependencias es necesario ejecutar
```
pip install -r requirements.txt
```
</details>

---

<details><summary><b>Instalar en LINUX:</b></summary>

### ***Sigue los siguentes pasos:***

Revisar versión de Python:
```
python --version
```
Crear un ambiente virtual:
```
python3 -m venv venv
```
Activar ambiente virtual:
```
source venv/bin/activate
```
Actualizar pip:
```
pip install --upgrade pip
```
Para instalar las dependencias es necesario ejecutar
```
pip install -r requirements.txt
```

</details>

---

## **Para Ejecutar:**

El siguiente comando para ejecutar el juego:

**WINDOWS**
```
python .\app.py
```
**LINUX**
```
python ./app
```
Si no te funciona, prueba usando "python3" o "py" en lugar de "python" en el comando anterior.

---

## **¿Problemas?**
En ese caso por favor levanta un [**issue** aquí en Github](), con el mayor detalle que puedas (versión de python, de paquetes, mensaje completo de error, etc).
Si eres ninja y lo solucionas, [¡levanta un Pull Request!](https://github.com/ringa-tech/juego-python-ia-misiles/pulls)

---

## Imágenes utilizadas
- [Iconos de cohetes creados por Freepik - Flaticon](https://www.flaticon.com/free-icons/rocket)
- [Iconos de misiles creados por Freepik - Flaticon](https://www.flaticon.com/free-icons/rocket-launch)
- [Fondo creado por Screaming Brain Studios - OpenGameArt](https://opengameart.org/content/seamless-space-backgrounds)

[![logo-Ringa-tech](https://www.ringa-tech.com/LogotipoV2-Simple.png)](https://www.ringa-tech.com/)
