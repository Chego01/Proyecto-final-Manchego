Tercera pre entrega Proyecto Python Coderhouse:
Objetivos generales:

    * Desarrollar una WEB Django con patrón MVT subida a Github.
Se debe entregar:

Link de GitHub con el proyecto totalmente subido a la plataforma.
Proyecto Web Django con patrón MVT que incluya:
    * Herencia de HTML.
    * Por lo menos 3 clases en models.
    * Un formulario para insertar datos a todas las clases de tu models.
    * Un formulario para buscar algo en la BD
    * Readme que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades.

Herencia HTML:
El archivo padre de la página web que desarrolle se llama "herencia.html" de la cual se generaron dos bloques diferentes para manipularlos
de la mejor manera entre las diferentes vistas.

Models:
Se genero el archivo models.py en el que se encuentra los modelos llamados "Articulo, Empleado y Cliente"

Users:
Genere un superuser con el usuario: tutorcoder con su contraseña: tutor12
para que pueda verificar los objetos creados en cada modelo.

Formulario:

Funcionalidad de los formularios:

Para poder ver los formularios creados para cada modelo que en total son tres. Nos dirigimos a los siguientes botones:
    - El boton "Clientes" nos muestra el formulario para poder agregar a personas que cumplan con este rol. 
      Esto gracias a la view creada como "cliente_formulario" que redirecciona a la plantilla "cliente_formulario.html" en donde se 
      genero el armado del formulario.

    - El boton "Actualizar prendas" hace referencia al modelo articulo. En este formulario se agregaran las prendas a la base de datos.
      Esto gracias a la view creada como "articulo_formulario" que redirecciona a la plantilla "articulo_formulario.html" en donde se 
      genero el armado del formulario.

    - Por último, el boton "Agregar empleado" se encuentra el formulario que cumple la funcion a la cual hace enfásis.
      Esto gracias a la view creada como "empleados_formulario" que redirecciona a la plantilla "empleados_formulario.html" en donde se 
      genero el armado del formulario.

Visualización de los listados:

Para ver las listas de los objetos agregados a cada modelo, se ve en los siguientes botones:
    - Para ver el listado del modelo cliente nos tenemos que dirigir al botón "Ver Clientes".
      Con la view definida como "listar_clientes" que refirecciona a la plantilla "listar_clientes.html" en donde se ve el listado
      de los clientes agregados a la base de datos.

    - En cuanto el listado del modelo articulo se encuentra en el botón "Catálogo"
      Con la view definida como "listar_articulos" que refirecciona a la plantilla "listar_articulos.html" en donde se ve el listado
      de los articulos agregados a la base de datos.
      
    - El listado del modelo empleado está en el botón "Empleados"
      Con la view definida como "listar_empleados" que refirecciona a la plantilla "empleados.html" en donde se ve el listado
      de los empleados agregados a la base de datos.

Formulario de búsqueda:

Se definio con la view llamada "Buscar" la funcionalidad requerida redirigiendo a la plantilla "resultados.html" en donde aparecera un mensaje de 
acuerdo a la existencia de la prenda dentro del catalogo

En el caso del formulario de búsqueda este se encuentra en el botón "Buscar" y a este formulario se le asigno la búsqueda de prendas para verificar si se encuentra en el catálogo. Para la visualizacion del formulario de busqueda se definio en la view llamada "busqueda_articulo" que nos redirecciona a la plantilla "buscar_articulos.html" que es lo que vemos al entrar al botón "Buscar"



