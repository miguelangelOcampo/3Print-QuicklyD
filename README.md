## 3Print QuicklyD
### Proyecto orientador para practicar uso de CRUD y diseno de software

#### Estructuracion del proyecto en Arquitectura por capas - Separacion de responsabilidades

Se opto por desarollar el programa con el fin de aprender y practicar la estructuracion de un CRUD convencional utilizando Python + FastAPI con Bootstrap y PostrgreSQL como motor de bases de datos. Ademas se utilizara Docker, Git y Argon2-JWT para el empaquetamiento (Api, Bases de datos, volumenes), control de versiones y hasheo de contraseñas-autenticacion de usuario respectivamente.

### Estructura general del proyecto

- **app**: Contiene el codigo fuente de la aplicacion.
- **uploads**: Almacena archivos que suben los usuarios.
- **requeriments.txt**: Define las dependencias nececarias para trabajar con Python.
- **Compose.yaml**: Configuracion y administracion de los contenedores.
- **.gitignore**: Define que archivos no se incluiran al repositorio.
- **README.md**: Documentacion del proyecto.

### Estructura por capas

- **routers**: Rutas y endpoints, tendran las responsabilidades por funcionalidades separadas.
- **models**: Modelo de los datos, es donde se difine la estructura que representan las entidades **de la base de datos**(Como tipo de variable, si es una llave primaria, etc) se hace uso de sqlalchemy.
- **schemas**: Contiene la estructura o representacion logica de las entidades a nivel funcional o **de la aplicacion** como comportamientos y metodos.
- **services**: Reglas de negocio de la aplicacion, comprobacion de condiciones, forma en que se guardan y se prepara la informacion para ser guardada.
- **static**: Carpeta contiene archivos que utilizamos para darle apariencia y comportamiento a nuestra aplicación, como estilos en css, scripts js, imagenes. Es el comportamiento estatico de la app para controlar solamente la apariencia general.
- **templates**: Plantillas o vistas desarolladas en HTML con jinja2 y Bootstrap.
- **core**: Centraliza la configuracion y variables del entorno.

## Descripcion del proyecto

 3Print QuicklyD s una aplicación web orientada a la gestión de pedidos y servicios de impresión 3D. Su objetivo es ofrecer una plataforma donde los usuarios puedan explorar un catálogo de modelos disponibles, consultar sus características, precios y tiempos estimados de impresión, así como solicitar cotizaciones para la fabricación de diseños personalizados.

La plataforma permitirá a los clientes registrarse e iniciar sesión para gestionar sus solicitudes, adjuntar archivos de referencia y consultar el estado de sus pedidos.

### El sistema contempla dos modalidades de servicio:

* Catálogo de productos: visualización de modelos disponibles para impresión, incluyendo imágenes, descripciones, materiales, precios y tiempos estimados de fabricación.

* Impresiones personalizadas: formulario de solicitud de cotización donde los usuarios podrán describir sus requerimientos, especificar dimensiones, cantidades, materiales y colores, además de adjuntar archivos de referencia en formatos como SVG, PNG, JPG, STL, OBJ y 3MF.

Las solicitudes serán recibidas por un administrador, quien podrá revisar los requerimientos, establecer cotizaciones y actualizar el estado de los pedidos.

### Objetivos

Desarrollar una aplicación web para la gestión de servicios de impresión 3D.

Implementar un sistema de registro y autenticación de usuarios.

Construir un catálogo de productos con información sobre precios y tiempos de impresión.

Permitir la creación y administración de solicitudes de impresión personalizadas.

Implementar la carga y almacenamiento de archivos adjuntos.

Gestionar el seguimiento y los estados de los pedidos.

Aplicar buenas prácticas de desarrollo mediante una arquitectura modular y separación de responsabilidades.

Implementar Docker para facilitar la configuración y ejecución del entorno de desarrollo.

### Alcance inicial

La primera versión contempla:

1. Registro e inicio de sesión de usuarios.

2. Catálogo de productos de impresión 3D.

3. Gestión de productos.

4. Solicitudes de cotización personalizada.

5. Carga de archivos de referencia.

6. Administración y seguimiento de pedidos.

7. Persistencia de información en PostgreSQL.

8. Ejecución del entorno mediante Docker Compose.