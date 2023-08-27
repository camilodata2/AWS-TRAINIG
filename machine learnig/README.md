# Machine larning en AWS
Entender los Conceptos Básicos:
Antes de comenzar, asegúrate de comprender los conceptos fundamentales del machine learning, incluyendo algoritmos, tipos de modelos y evaluación de modelos.

Elegir un Enfoque:
AWS ofrece varios enfoques y servicios para realizar machine learning:
Amazon SageMaker: Es un servicio integral que simplifica la creación, entrenamiento y implementación de modelos de machine learning.
Deep Learning AMIs: Son imágenes preconfiguradas de máquinas virtuales con herramientas y bibliotecas de aprendizaje profundo.
Frameworks de Aprendizaje Profundo: Puedes utilizar frameworks populares como TensorFlow y PyTorch en instancias EC2.

Crear y Entrenar Modelos:
Con Amazon SageMaker, puedes utilizar cuadernos (notebooks) para desarrollar, entrenar y ajustar tus modelos.
Si estás usando instancias EC2 y frameworks, instala los frameworks necesarios, carga tus datos y crea y entrena tus modelos.

Almacenamiento de Datos:
Utiliza Amazon S3 para almacenar y acceder a tus datos de entrenamiento y conjuntos de datos.

Implementación y Despliegue:
En Amazon SageMaker, puedes crear puntos de enlace (endpoints) para implementar tus modelos entrenados y hacer predicciones en tiempo real.
Si estás utilizando instancias EC2, puedes implementar tus modelos en una aplicación web o en servicios de backend.

Monitoreo y Optimización:
Monitorea el rendimiento de tus modelos en producción y utiliza métricas para mejorar su precisión con el tiempo.

Automatización:
Utiliza AWS Lambda y AWS Step Functions para automatizar tareas como el entrenamiento de modelos en respuesta a eventos.

Costos y Seguridad:
Comprende la estructura de precios de AWS relacionada con machine learning y configura los permisos de seguridad adecuados.

Aprendizaje Continuo:
Mantente actualizado con las últimas tendencias y avances en el campo del machine learning.

## Servicios de machine learing en AWS
AWS ofrece una variedad de servicios de inteligencia artificial (IA) y aprendizaje automático que te permiten desarrollar, entrenar e implementar modelos de IA en la nube. Aquí tienes una lista de algunos de los principales servicios de IA en AWS:

Amazon SageMaker:
Amazon SageMaker es un servicio integral para el desarrollo y despliegue de modelos de aprendizaje automático. Proporciona cuadernos (notebooks) para desarrollo, entornos de entrenamiento escalables, y puntos de enlace (endpoints) para implementar modelos en producción.

Amazon Rekognition:
 Un servicio de visión por computadora que permite analizar imágenes y videos para detectar objetos, rostros, texto y contenido inapropiado. Es útil para aplicaciones de análisis de medios y automatización.

Amazon Polly:
Polly es un servicio de síntesis de voz que convierte texto en habla realista en varios idiomas y voces. Puedes usarlo para crear aplicaciones de lectura de texto, asistentes virtuales y más.

Amazon Lex:
Lex es un servicio de creación de chatbots y asistentes virtuales basados en tecnología de procesamiento del lenguaje natural (NLP). Puedes integrarlo en aplicaciones web y móviles.

Amazon Comprehend:
Comprehend utiliza procesamiento del lenguaje natural para analizar texto y extraer información relevante, como sentimiento, entidades y temas.

Amazon Translate:
Un servicio de traducción automática que permite traducir texto entre diferentes idiomas.

Amazon Transcribe:
Transcribe convierte audio en texto de manera automatizada, lo que es útil para transcripciones de grabaciones de voz.

Amazon Forecast:
Forecast es un servicio para la predicción de series temporales. Puedes usarlo para predecir la demanda de productos, el tráfico del sitio web y más.

Amazon Personalize:
Personalize permite crear recomendaciones personalizadas para los usuarios, como sistemas de recomendación para productos y contenidos.

Deep Learning AMIs:
Amazon ofrece imágenes preconfiguradas de máquinas virtuales con frameworks de aprendizaje profundo como TensorFlow y PyTorch, lo que facilita el desarrollo de modelos de IA.

### AWS sagemaker

Amazon SageMaker es un servicio de Amazon Web Services (AWS) que facilita la creación, el entrenamiento y la implementación de modelos de machine learning de manera rápida y escalable. Ofrece una plataforma completa para desarrolladores y científicos de datos, que abarca desde la preparación de datos hasta la implementación en producción de modelos, sin requerir una gestión compleja de infraestructura.

Las principales características y componentes de Amazon SageMaker son:

Notebooks Jupyter Integrados: SageMaker proporciona entornos de cuadernos Jupyter totalmente administrados y escalables para desarrollar y experimentar con modelos de machine learning.

Preparación de Datos: Incluye herramientas para explorar, limpiar y transformar los datos de entrenamiento antes de utilizarlos para entrenar modelos.

Entrenamiento de Modelos: Ofrece un entorno para entrenar modelos de machine learning utilizando una variedad de algoritmos y marcos de trabajo, como TensorFlow, PyTorch, XGBoost y más.

Optimización de Modelos: SageMaker puede ayudar a optimizar automáticamente los hiperparámetros del modelo utilizando técnicas de búsqueda automática, lo que mejora la precisión del modelo.

Implementación y Despliegue: Permite crear endpoints de inferencia para implementar modelos entrenados y hacer predicciones en tiempo real. También admite la implementación de modelos en lotes para procesar grandes volúmenes de datos.

Automatización y Escalabilidad: Facilita la automatización de flujos de trabajo de machine learning mediante la creación de pipelines y la programación de tareas.

Seguridad y Control: Proporciona capacidades de autenticación, autorización y cifrado para garantizar la seguridad de los datos y los modelos.

Gestión de Versiones: Permite la gestión y el seguimiento de diferentes versiones de modelos y conjuntos de datos.

Interoperabilidad: Puede integrarse con otros servicios de AWS y herramientas de terceros para obtener un flujo de trabajo más completo.

#### ejemplo
Vamos a realizar un pequeño ejemplo de como usar AWS sagemaker con el algoritmo de randomforest, lo primero sera crear un bucket en S3 donde este tendra la data con la que vamos a limentar el modelos, ademas usaremos una vscode y nos conectaremos con boto3 desde nuestra consola, otra forma de hacerlo es realizar todo el proceso desde la misma consola de aws(con una SDK)

##### Descripcion del ejemplo

Preparación de Datos:
Prepara un conjunto de datos que incluya características médicas de los pacientes y etiquetas que indiquen si tienen cáncer o no.

Creación de un Cuaderno de Jupyter en SageMaker:
Crea un cuaderno de Jupyter en SageMaker para desarrollar y ejecutar el flujo de trabajo.

Exploración y Preprocesamiento de Datos:
En el cuaderno, explora los datos y realiza cualquier preprocesamiento necesario, como la normalización de características.

División de Datos:

Divide los datos en conjuntos de entrenamiento y prueba utilizando la función train_test_split de Scikit-Learn.

Construcción del Modelo:
Utiliza un algoritmo de machine learning, como Random Forest, para construir el modelo de clasificación. Puedes usar el paquete sagemaker.sklearn para integrar el modelo con SageMaker.

Entrenamiento del Modelo:
Utiliza SageMaker para entrenar el modelo utilizando el conjunto de entrenamiento. Esto implica definir un Estimator, que es una configuración del entorno de entrenamiento, y luego llamar al método fit en el Estimator.

Despliegue del Modelo:
        Despliega el modelo entrenado en un punto de enlace (endpoint) utilizando SageMaker. Esto te permitirá realizar predicciones en tiempo real.

Realización de Predicciones:
Utiliza el punto de enlace para realizar predicciones sobre el conjunto de prueba y evaluar el rendimiento del modelo.

Limpieza:
 No olvides cerrar el punto de enlace y liberar los recursos de SageMaker cuando hayas terminado.

Este es un resumen general del flujo de trabajo utilizando SageMaker para clasificar pacientes con cáncer. Sin embargo, ten en cuenta que en la práctica, necesitarás dedicar tiempo a la exploración de datos, ajuste de hiperparámetros y validación del modelo para asegurarte de obtener resultados precisos y confiables. Además, la manipulación de datos médicos debe realizarse con cuidado y respetando las regulaciones de privacidad y seguridad.
