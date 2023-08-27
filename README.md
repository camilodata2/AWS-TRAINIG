# cloudfront
AWS CloudFormation es un servicio de infraestructura como código (IaC) proporcionado por Amazon Web Services (AWS). Permite a los usuarios describir y provisionar recursos de infraestructura en la nube de AWS de manera automatizada y repetible, utilizando plantillas declarativas.

En lugar de crear y configurar manualmente cada recurso en AWS, como instancias EC2, grupos de seguridad, bases de datos y más, puedes definir tu infraestructura en forma de plantillas. Estas plantillas se escriben en formato YAML o JSON y describen los recursos que deseas crear, así como las propiedades y relaciones entre ellos.

Algunas características clave de AWS CloudFormation incluyen:

Automatización y Consistencia: CloudFormation automatiza el proceso de creación, actualización y eliminación de recursos. Esto garantiza que tu infraestructura sea coherente en diferentes entornos y a lo largo del tiempo.

Gestión de Dependencias: CloudFormation administra las relaciones y dependencias entre los recursos. Si un recurso depende de otro, CloudFormation se encargará de crearlos en el orden adecuado.
 
Control de Versiones: Las plantillas de CloudFormation se pueden almacenar en sistemas de control de versiones, lo que permite un seguimiento de los cambios y la reversión a versiones anteriores si es necesario.
 
Cambios Controlados: Cuando necesitas realizar cambios en tu infraestructura, puedes modificar la plantilla y actualizar los recursos existentes de manera controlada. CloudFormation se encargará de aplicar los cambios de forma segura.

Reusabilidad: Puedes utilizar parámetros y variables en tus plantillas para hacerlas más flexibles y reutilizables en diferentes contextos.

Implementaciones Apiladas: Puedes crear implementaciones apiladas, donde una plantilla puede llamar a otras plantillas. Esto es útil para separar diferentes componentes de tu infraestructura.

Soporte para Diversos Servicios: CloudFormation admite una amplia gama de servicios de AWS, lo que te permite definir una infraestructura completa que abarca desde redes hasta aplicaciones.

En resumen, AWS CloudFormation es una herramienta poderosa para definir, implementar y gestionar la infraestructura en la nube de AWS de manera automatizada y eficiente, lo que facilita la administración y la escalabilidad de las aplicaciones y servicios en la nube.

## Descripcion de los parametros del template

"AWSTemplateFormatVersion": Define la versión de la plantilla de CloudFormation que se está utilizando. En este caso, se utiliza la versión "2023-08-26"

"Description": Proporciona una descripción de la plantilla para ayudar a comprender su propósito y contenido.

"Resources": Esta sección es donde defines los recursos que deseas crear utilizando esta plantilla. Los recursos pueden ser instancias EC2, grupos de seguridad, bases de datos, colas de mensajes, etc.

"MySecurityGroup": Este es el nombre que le das al recurso que estás creando. En este caso, es un grupo de seguridad de EC2.

"Type": Indica el tipo de recurso que estás creando. En este caso, es "AWS::EC2::SecurityGroup", lo que representa un grupo de seguridad de EC2.

"Properties": Aquí se definen las propiedades específicas del recurso que estás creando. En este ejemplo, estamos configurando las propiedades de un grupo de seguridad.

"GroupDescription": Esta propiedad establece la descripción del grupo de seguridad que estás creando.

"SecurityGroupIngress": Esta propiedad define las reglas de seguridad entrantes para el grupo de seguridad.

"IpProtocol": Especifica el protocolo IP que se permitirá. En este caso, es "tcp" para el protocolo TCP.

"FromPort": Indica el puerto desde el que se permitirá el tráfico entrante. Aquí, es el puerto 80.

"ToPort": Indica el puerto hasta el cual se permitirá el tráfico entrante. Aquí, también es el puerto 80.

"CidrIp": Es la dirección IP o rango de direcciones IP desde las cuales se permitirá el tráfico entrante. En este caso, "0.0.0.0/0" permite el tráfico desde cualquier dirección IP.

Estos son los elementos clave en esta plantilla de ejemplo. Puedes personalizar estos parámetros según tus necesidades para crear diferentes recursos y definir relaciones entre ellos.

### Creando un stack
ara crear un stack (pila) utilizando una plantilla de CloudFormation, puedes seguir estos pasos utilizando la AWS Management Console:

Inicia sesión en tu cuenta de AWS.

Ve al servicio "CloudFormation" en la consola de AWS.

Haz clic en el botón "Crear pila" (Create stack).

Selecciona "Con plantillas preparadas" (With templates ready) y elige "Subir un archivo de plantilla" (Upload a template file).

Sube la plantilla JSON o YAML que hayas creado previamente.

Define los detalles de la pila:
Ingresa un nombre para la pila en el campo "Nombre de la pila" (Stack name).
Puedes proporcionar parámetros si tu plantilla los requiere. Los parámetros son valores que personalizan la creación del stack.
Puedes establecer etiquetas opcionales para la pila.

Haz clic en "Siguiente" (Next).

Configura las opciones de configuración:
Puedes configurar roles de IAM si es necesario.
Puedes establecer opciones avanzadas, como notificaciones por correo electrónico.

Haz clic en "Siguiente" (Next).

Revisa la configuración de la pila y, si todo parece correcto, haz clic en "Crear pila" (Create stack).

<img serc="https://static.platzi.com/media/articlases/Images/Screenshot%20at%202022-06-03%2016-10-52.png" alt="texto alternativo" width="300">

Le damos clic a siguiente y, a continuación, escogemos un nombre para el stack o pila. En este caso, 
la llamamos cfnlab, y le damos a siguiente.Opcionalmente, podemos añadir etiquetas para identificar la pila, y un rol de IAM.Dejamos el resto de configuraciones por defecto y le damos a siguiente. Entonces nos llevará a revisar las configuraciones, y le damos a “Crear pila”.Podremos ver el proceso de creación de la pila, los eventos y los recursos que fueron creados. Si te fijas en el nombre del bucket creado, verás que este está compuesto por el nombre de la pila, el nombre que le asignamos al bucket en la plantilla, y una cadena de texto aleatoria. Esto es para evitar crear recursos con nombre duplicados.

#### Actualizando stack

Para autilizar el stack tomaremos lo que hicimos en el primer stack, y valga la redundancia lo autilizaremos,añadimos algo nuevo para verlo puedes ver donde dice updatestack.json

Para cargar el stack actualizado seguimos los pasos anteriormente mensionado, pero con la pequeña diferencia que anexamos el updatestack.json

##### Eliminando stack

Es crucial eliminar de manera constante los recursos que ya no necesitemos utilizar. Esta práctica es fundamental para evitar cargos indebidos. Para verificar que no tengamos ninguna instancia activa en AWS, podemos acceder a la sección de 'Facturación' (BILLS), donde tendremos una vista detallada de los servicios que estamos empleando