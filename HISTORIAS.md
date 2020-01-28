# hms_sys_app
	El sistema-nivel del repositorio para el projecto hms_sys_app, de 'Hands on software engineering with Python.'
## configuracion inicial del proyecto con nvim y venv(ambiente virtual python).

# Iteración de gestión del código y estructura  del proyecto: 
# Objetivos:
1. Repositorio maestro, almacenado en un servidor Git o servicio(GitHub), que contendra la estructura inicial completa del proyecto.

2. Un componente proyecto para cada clase de biblioteca desplegable o aplicación en el sistema.

3. Un conjunto de pruebas unitarias que se puedan ejecutar, y cuya ejecución sea aprobada para cada proyecto componente del sistema.

4. Un proceso de compilación para cada componente del proyecto -- también ejecutable -- que da como resultado un paquete desplegable, incluso si el paquete comienza con algo esencialmente inutil.

#Historias & tareas:
# Historia 1
Como desarrollador, necesito saber: 
h1. .. como se administra el código  fuente del sístema y control de version, para poder conservar/almacenar el codigo que yo escribo.
# Tareas:
h1. t1. Crear un repositorio en blanco para el sistema -- hm_sys_app (hand make stuff system application). 
h1. t2. Rellenar el repositorio con la información de referencia y la documentación para el uso continuo.
h1. t3. Establecer y distribuir las credenciales necesarias para que puedan acceder al repositorio los miembros del equipo.

# Historia 2
h2. .. como se ve la estructura completa, al menos en nivel alto, para que pueda escribir código que se ajuste a la estructura.
# Tareas:
Esto implica:
h2. t1. Analizar los casos de uso y la arquitectura física y lógica, para definir los componentes del proyecto necesarios y su estructura.
h2. t2. Desarrollar puntos de partida estandar para cada componente del protyecto identificado.
h2· t3. Implementar un setup.py mínimo para cada componente del proyecto que complete una compilación del paquete fuente.
h2. t4. Determinar si usar o no entornos virtuales Python para los componentes del proyecto, implementar estos, y documentar como se los puede reproducir.

# Historia 3
h3. .. como y donde escribir pruebas unitarias para el codigo base, para que pueda escribir pruebas unitarias despues de escribir el código. También asegurar que el ćodigo sea testeado a fondo.
# Tareas:
h3. t1. Definir los estandares/requisitos de las pruebas unitarias (covertura, valores estandar por tipo, etc.).
h3. t2. Implementar un mecanismo para hacer cumplir esas normas (h3. t1.).
h3. t3. Definir donde recidirá ese código de prueba en la estructura de un componente del proyecto.
h3. t4. Implementar una prueba básica del nivel-superior para cada componente de proyecto que se ejecute sin fallas.

# Historia 4
h4. .. como integrar pruebas unitarias de un componente dentro el proceso de compilación para que el proyecto tambien este pueda automaticamente ejecutar las pruebas unitarias.
# Tareas:
h4. t1. Determinar como integrar las pruebas unitarias en el proceso de compilación.
h4. t2. Determinar como lidiar con la integración compilación/testeo en diferentes ambientes(de desarrollo).


# Iteración libreria clase hms_core. 
#Objetivos:
1. Paquete/Libreria hms_core.
2. Testeado unitario.
3. Capaz de ser construido como paquete independiente.
4. Proporcionar base inicial de representación de las clases:
	Artesanos, Clientes, Pedidos y productos. 

# Historia 5
h5. .. una definición comun y estructura funcional para representar las direcciones en el sistema, de modo que pueda incorporarlas en las partes del sistema que las necesitan:
# Tareas
para la Clase Abstracta Base(ABC) BaseAdress:
h5. t1. .. definir.
h5. t2. .. implementar.
h5. t2. .. pruebas de unidad.

# Historia 6
h6. .. una definición comun y estructura funcional para representar los artesanos en el sistema, de modo que pueda incorporarlas en las partes del sistema que las necesitan:
# Tareas
para la Clase Abstracta Base(ABC) BaseArtisans:
h6. t1. .. definir.
h6. t2. .. implementar.
h6. t2. .. pruebas de unidad.

# Historia 7
h7. .. una definición comun y estructura funcional para representar los clientes en el sistema, de modo que pueda incorporarlas en las partes del sistema que las necesitan:
# Tareas
para la Clase Abstracta Base(ABC) BaseCustomers:
h7. t1. .. definir.
h7. t2. .. implementar.
h7. t2. .. pruebas de unidad.

# Historia 8
h8. .. una definición comun y estructura funcional para representar las pedidos en el sistema, de modo que pueda incorporarlas en las partes del sistema que las necesitan:
# Tareas
para la Clase Abstracta Base(ABC) BaseOrders:
h8. t1. .. definir.
h8. t2. .. implementar.
h8. t2. .. pruebas de unidad.

# Historia 9
h9. .. una definición comun y estructura funcional para representar las productos en el sistema, de modo que pueda incorporarlas en las partes del sistema que las necesitan:
# Tareas
para la Clase Abstracta Base(ABC) BaseProducts:
h9. t1. .. definir.
h9. t2. .. implementar.
h9. t2. .. pruebas de unidad.

# Historia 10
h10. Como un artesano, yo necesito la libreria de objetos del negocio a ser instalada con mi aplicación, ademas que funcione como sea necesario  sin instalar componentes de dependencias para este:
#Tareas 
h10. t1. Determinar si el empaquetado basado en setup.py puede incluir paquetes desde fuera de la estructura del proyecto local, y si se puede implementarlo.
h10. t2. Caso contrario, implementar Makefile basado en el proceso para incluirlo en hms_core dentro de los proceso de empaquetado de otros proyectos.

# Historia 11
h11. Como usuario de la  oficina central, yo necesito la libreria de objetos del negocio a ser instalada con mi aplicación tal que la aplicación trabaje con lo necesario sin la necesidad de instalar componenetes de dependencias para este:
# Tareas
h11. t1. Verificar que el proceso de empaquetado/instalación de Artisan también trabaje para la instalación de la oficina central.

# Historia 12
h11. Como administrador de la  oficina central, yo necesito la libreria de objetos del negocio a ser instalada con mi aplicación tal que la aplicación trabaje con lo necesario sin la necesidad de instalar componenetes de dependencias para este:
# Tareas
h11. t1. Verificar que el proceso de empaquetado/instalación de Artisan también trabaje para la instalación de la oficina central.


h10. t
