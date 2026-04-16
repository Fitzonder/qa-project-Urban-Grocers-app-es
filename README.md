Urban.Grocers API Testing Project

Descripción

Proyecto de practica para el titulo de QA Ingineer el cual se centra en la automatización de pruebas para la API de Urban.Grocers.

Objetivos del Proyecto

\- Verificar la correcta creación de kits 

\- Verificar la integridad del correcto recibo y envío de datos. 

\- Validar las respuestas de la API para diferentes escenarios de prueba.

Tecnologías Utilizadas

\- Python 3.x y dependencias instaladas (pytest, requests).

\- *Framework de Pruebas:\*\* Pytest

\- *Herramientas Adicionales:\*\* Git, GitHub

Estructura del Proyecto

\- `Configuration.py`: Archivos de configuración y variables de entorno.

\- `data.py`: Funciones y utilidades comunes para las pruebas.

\- `sender\_stand\_request.py`: Pruebas para la creación de kits.

\- `create\_kit\_name\_kit\_test.py`: Contiene todos los archivos de prueba.

Cómo Ejecutar las Pruebas

1\. Clonar el repositorio:

&nbsp;  ```bash

&nbsp;  git clone git@github.com:Fitzonder/qa-project-Urban-Grocers-app-es.git

Navegar al directorio del proyecto:

cd urban-grocers-api-testing

Instalar las dependencias:

pip install -r requirements.txt

Ejecutar las pruebas:

pytest
