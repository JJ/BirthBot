# BirthBot
### Autor: Jorge Gutiérrez Segovia

---

### Descripción

Repositorio sobre la asignatura de Infraestructuras Virtuales en el que voy a implementar un servicio web que recuerda los `Cumpleaños` almacenados en una Base de datos.

---

### Desarrollo del proyecto:

* **Descripción de la clase** 

  He creado una clase `birthbot`, situada en la carpeta `travistest`, la cual permite crear un objeto *birthday* a partir de los atributos: *birth_date* y *name*, los cuales describen la fecha de cumpleaños y el nombre respectivamente.

  Las pruebas realizadas hasta el momento se encuentran en `test_birthbot.py` , situado en la carpeta `test` .

* **Instalación**

  Para la instalación debemos clonar el repositorio del proyecto, usando el siguiente comando:

  `git clone https://github.com/Saytes/BirthBot.git`

* **Testeo**

  Para testearlo debemos instalar pytest, usando el siguiente comando:

  `pip install pytest`

  Una vez hecho esto, en la raiz del proyecto, ejecutamos el comando `pytest`.

* **Travis**

  Este proyecto está sincronizado con [Travis](https://travis-ci.org/).

  Tras haber hecho pytest, el resultado obtenido es: [![Build Status](https://travis-ci.org/Saytes/BirthBot.svg?branch=master)](https://travis-ci.org/Saytes/BirthBot)

* **Despliegue en Heroku**
  - Despliegue en [Heroku](https://birthbot.herokuapp.com/)
  - Json [adicional](https://birthbot.herokuapp.com/status) al despliegue
  - [Documentación](./docs/despliegue.md) del despliegue de mi aplicación en Heroku

* **Despliegue en Docker**[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://docker-iv.herokuapp.com/status)**

  * Despligue en [Docker](https://docker-iv.herokuapp.com/)
  * [Documentación](./docs/despliegue_docker.md) del despliegue de mi aplicación en Docker.

