# Ges-co : Gestión de Compras

## ¿Qué es Ges-co?

Gesco es una aplicación web desarrollada en Python gracias  gracias a Google App Engine, el cual te permite crear backends web y movil utilizando los lenguajes de programación dentro de la infraestrucutra de Google.  

El objetivo de la aplicación es realizar un pequeño proyecto para la asignatura de ALS (Aplicaciones con Lenguajes de Script) de 4º curso de la ESEI.  

## Sobre la aplicación

La aplicación se puede probar en el siguiente enlace: https://als-project-gesco.appspot.com/  

## Información sobre la configuración:

En el archivo `app.yaml` se ha eliminado lineas que según la documentación de Google App Engine, como puede ser `application` y `version`.  

Si añadimos alguna nueva entidad, es necesario hacer un update de los indexes. Para ello debemos ejecutar `gcloud datastore create-indexes index.yaml` o de lo contrario nuestra aplicación **no funcionará correctamente**. Tras realizarlo es necesario esperar un rato a que Google realice el update correctamente.

## Documentación

*  Configuring your App with app.yaml: https://cloud.google.com/appengine/docs/flexible/python/configuring-your-app-with-app-yaml
*  Testing and Deploying your Application: https://cloud.google.com/appengine/docs/flexible/python/testing-and-deploying-your-app
*  Index Configuration : https://cloud.google.com/datastore/docs/tools/indexconfig?hl=es
*  Configuring Datastore Indexes : https://cloud.google.com/appengine/docs/standard/python/config/indexconfig
