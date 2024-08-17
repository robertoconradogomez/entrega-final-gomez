<h1 align="center">Hola 👋 me llamo Roberto C. Gomez</h1>
<h3 align="center">Esta es la entrega final y estoy usando "GitHub Profile README Generator" para dejar más prolijo el README.</h3>

<h3 align="left">Tecnologías utilizadas:</h3>
<p align="left"> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>



<h3 align="left">🔭 Estructura del sitio</h3>

      inicio.html es una landing page, con acceso al repositorio y los casos de prueba  

      La idea era crear una web para una institución educativa, que le permita gestionar sus cursos, mostrarlos, editarlos y borrarlos Ademas de gestionar sus usuarios, respetando la idea de "blog" propuestas   
      para esto, en la página donde se listan los cursos, se puede ingresar en "ver" y ver los detalles completos de los mismos.   

      - Realiza CRUD   
      - Gestiona Usuarios de forma completa   
      - Gestiona cursos y sus detalles de forma completa   

      app1/   

      Es la web completa, donde se puede ver un listado de cursos, about, acceso a los detalles de cada curso, y acceso a la appuser para gestionar los usuarios.   


      appuser/

      gestiona todo lo referente a los usuarios, creación, modificación, avatares, etc.   

      hay tres tipos de usuario:   
      
      "sin usuario" | solo tiene acceso a ver los cursos cargados y sus detalles, inicio y about.
      "usuario genérico" | mismos permisos que el anterior, ademas puede gestionar su usuario, cambiar sus datos y el avatar.
      "staff" | los mismo accesos que el anterior, pero puede editar los cursos cargados.
      "Admin" | Todos los permisos, ademas de poder crear cursos nuevos y borrar los existentes desde la misma web.
      

<p align="left">

---------------------------

Se cambiaron cosas como el manejo de avatares, ahora al crear cualquier usaurio, el formulario agrega un avatar por defecto alojado en media/avatares.   
Se cambiaron algunas cosas esteticas como botones y navBar.

---------------------------

Lista de usuarios para probar:   

- Admin   
Usuario: rgomez   
Pass: Rober33832011$ 

- Staff   
Usuario: staffuser   
Pass: Viernes2024   

</p>