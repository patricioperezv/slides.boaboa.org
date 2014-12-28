% Workshop Laravel 4
% Patricio Pérez <patricio.perez@ceinf.cl>
% Primer semestre 2015

# Que aprenderemos (Intentaremos?)

## Como no hacerlo enojar ...

![Profesor Salazar](images/jirafales.jpg)

. . .

Es un \_poco\_ cascarrabias ...

## Para ello usaremos

----

![Github](images/github.jpg)

. . .

Control de versiones distribuido

----

![Laravel](images/laravel.png)

. . .

Framework PHP para buenos tipos!

----

![PostgreSQL](images/postgresql.jpg)

----

![Ubuntu](images/ubuntu.png)

. . .

Sistema operativo "_de verdad_"

# Que quedó fuera de este workshop

## Contenidos que no veremos (aún?)

Hay herramientas que se me quedaron en el tintero, pero creo que serían bien útiles para cualquier developer que se respete:

- Pruebas unitarias
- Integración continua (Tambien conocido como CI o Continuous Integration)

# Contenidos

## Contenidos

- Buenas (y malas) prácticas en el ramo (A.K.A Tratando de no hacer rabiar al profe)
- Instalacion del entorno de desarrollo (*Ubuntu + DB + IDE + Git + Framework*)
    - Uso básico de linux (Línea de comandos + git(*hub*))
    - Uso de manejador de dependencias de PHP: *Composer*
- Introducción rápida al patrón MVC (*Model View Controller*)
- Migraciones de db (*Generación del modelo en DB*)
- ORM (*Object Relational Mapping*): *Eloquent*

---

## Contenidos

- Rutas en el framework, verbos HTTP y controladores resourceful
- Vistas: Templates *Blade*
- Probando código en la terminal: *Tinker*
- Rutas avanzadas (Anidación de recursos, filtros)
- Integración con un servicio REST
- Ejecución de tareas programadas (Mezclando CRON con laravel)
- Deployment en producción (Ubuntu + Apache 2 + PostgreSQL)

# Convenciones

## Convenciones

Estas serán nuestras herramientas a lo largo del workshop (A.K.A Ayudantia):

- Sistema operativo: Linux (*Ubuntu 14.04*)
- Control de versiones: *Git*
- Motor de base de datos: *PostgreSQL*
- IDE: *Eclipse* (O alguno de su gusto)
- Framework **MVC**: *Laravel 4.2*

# Buenas (y malas) prácticas

## Buenas prácticas

<div class="notes">
- Hay que tener en cuenta que ya estamos viejitos
- No se ustedes, pero hay varias cosas sobre las que no tengo ni p*ta idea.
- Esto más que frustrar al profe (Creanme que lo hará), los frustrará a ustedes.
- Ya que les costará hacer cosas relativamente sencillas, perdiendo mucho tiempo, tiempo en el que podrían estar carreteando por ejemplo.
</div>

![](images/no_idea_dog.jpg)

## Sobre la realización del trabajo

A lo largo de la asignatura verán un monton de conceptos (DRY, YAGNI, metodologías ágiles, PMBOK, etc).

---

<div class="notes">
- Los estándares estan hechos para que no se odien entre los mismos miembros del team
- La planificación esta pensada para estructurarlos un poco, distribuyan bien el tiempo, y al final le digan al profe que trabajaron bien (Y que eso no sea una falazzììa)
</div>

El resumen corto de todo eso (En mi opinión bien vaga) es que mientras esten construyendo el proyecto tengan esto en cuenta:

- Traten de ir mostrando constantemente su trabajo, ya que el cliente puede ser algo especial (A.K.A Los puede mandar a la punta del cerro si hay cosas que no le agraden)
- Planificación (No hagan todo a última hora)
- Estándares (Quizas no los de industrias, ISO, IEEE, sino estándares fijados por ustedes)
- No usen las herramientas porque se las esten imponiendo, no se resistan ლ(´ڡ`ლ) realmente intenten entenderlas y usarlas a futuro!
- Ya dije que deberian preguntar mucho? El feedback es fundamental en el desarrollo de un proyecto, solo traten de que sus preguntas no sean tan ...

## DRY

. . .

- Si están realizando dos secciones de código (Por ejemplo dos partes de un html) y estan difieren muuuuy poco o nada, estan haciendo código de más.
- Este es complicado de mantener (Si cambio uno TENGO que cambiar el otro) y es una pesadilla a medida que crece el proyecto.
- Aprovechen de que el framework les entrega herramientas para combatir esto (Para las vistas html tienen herencia y composición por ejemplo)

## Indentación

A lo largo de la asignatura, probablemente esten mostrando mucho código al profe, al ayudante, o a sus mismos compañeros, nada se agradece más que un buen indentado del código.

. . .

Así que haganse el tiempo, o ...

## Dejen que el IDE lo haga!

![IDE! Trabaja por mi pls](images/auto_format.png)

## Uso de git

<div class="notes">
- Salazar sapea el git
- Implica que puede ver desempeño de cada miembro del equipo
- O todas las tonteras que escriben en el log de commits
</div>

- Trabajen en sus cuentas individualmente, no todos en un solo usuario
- Llenen correctamente sus perfiles en github (Si ponen fotito mejor)
- Configuren correctamente su correo y nombre en la instalación de git local (Así se pueden distinguir en la rama de commits)
- Que sus commits indiquen (o traten de indicar) que cambio realizaron en el código
- Idealmente usen branches (ramas) al desarrollar, cuando la funcionalidad que agregaron este "lista" hacen merge a su branch principal (e.g: master)

## Perfil

![Mi perfil en github](images/github_profile.png)

## Config git

![Config git](images/git_config.png)

## Log de commits

![Commit log](images/commit_tree.png)

# Instalando el entorno de desarrollo

## Ubuntu

<div class="notes">
> Yo mismo: **Mismo, recuerda!!**
> Hay que ver que día nos juntamos en la sala de info a ver comandos linux por lo bajo
</div>

Me imagino que ya sabrán como instalar Ubuntu, pero si tienen dudas podemos organizar una pequeña jornada de instalación en la sala de info ツ
Recuerden, para que no tengamos atados, usaremos la versión 14.04 (Tiene soporte para 5 años más, creo que estamos cubiertos!)

---

De hecho, juntemonos en la sala igual, lleven sus notebooks, y veremos los comandos básicos para la línea de comandos de Linux

## Torpedo básico de comandos UNIX

- Usar **TAB** para completar comandos, nombres de ficheros, siempre que se pueda!
- `cd directorio` Ingresa a un directorio
- `cat fichero.txt` Muestra en pantalla el contenido de un fichero
- Cuando se trabajan directorios `.` se refiere al directorio actual, `..` se refiere al padre del directorio actual, de hecho `../..` entraria al padre del padre del directorio actual (abuelo??)
- Nuestro home (Donde se guardan todas nuestras leseras) es por defecto `/home/usuario`, un atajo es `~` (ej: ´~/Descargas´ equivale a ´/home/usuario/Descargas´)

----

- Usar apt para manejar paquetes es super sencillo:
    * `apt-get install paquete otropaquete` Instalar
    * `apt-get remove paquete otropaquete` Desinstalar
    * `apt-cache search palabra buscar php` Buscar paquetes, en descripción etc, pueden ser muchas palabras
    * `apt-get update` Actualiza la base de datos de paquetes
    * `apt-get dist-upgrade` Actualiza todos los paquetes del sistema
- Usar `sudo` antes de cualquier comando que necesite permisos de administrador (ej: instalar paquetes con apt, modificar ficheros en `/etc`, etc)

## Instalando el framework y la base de datos

En mi blog ([http://alumnos.informatica.utem.cl/~pperez](http://alumnos.informatica.utem.cl/~pperez)) tengo un tutorial que los dejará listos para desarrollar con laravel, incluye la instalación del motor de base de datos, instalar php, composer, y la cachá de la espada. Lo haremos ahora, preparense!

## Git

Aquí ya empiezo a explicars

## Que es git

![Git](images/git_scm.png)

Git es un sistema de control de versiones (Conocido como SCM), sus características son:

----

### Controlar las versiones de nuestros ficheros

Cuantas veces les ha ocurrido esto?

![Por favor no me hagan esto!](images/versiones_artesa.png)

----

[Git](http://git-scm.com/) (O cualquier SCM que se respete) les permite ver revisiones de sus ficheros, en la mayoria estas revisiones son representadas por "commits"

----

![Commits](images/commit_tree.png)

----

![Mirar un diff](images/git_diff.png)

## Es distribuido

<div class="notes">
- CVCS: "Centralized Version Control System" (ej: SVN, CVS)
- DVCS: "Distributed Version Control System" (ej: Git, Mercual, Bazaar)
</div>

![CVCS vs DVCS](images/cvcs_vs_dvcs.png)

Si se cae el servidor de github (Repositorio central en la imagen), aún pueden trabajar, hacer commits, consultar el log, crear branches, y otras operaciones locales.

----

(Ojo! [Github](http://github.com) no es el único proveedor de git, esta [bitbucket](http://bitbucket.org) y otros, incluso pueden alojarlo en un servidor propio)

## Y bueno, al ataque

- El primer paso sería entrar a [github](http://github.com) y crearnos una cuenta
- Ahora debemos crear una llave ssh (Abran sus terminales y tipeen):
- `git config --global user.name "Patricio Pérez"`
- `git config --globa user.email pperez@boaboa.org`
- `git config --global color.ui auto`
- `ssh-keygen -t rsa -C pperez@badgerbook`
- Ver el contenido de `.ssh/id_rsa.pub` y agregarla a Github (En la web 'Settings → SSH keys → Add SSH key')

---

<iframe src="http://showterm.io/3eb31771d1635f586f6c4#slow" width="800" height="520"></iframe>

---

![Agregar llave SSH](images/github_add_ssh_key.png)

---

- Crear el repositorio ('Create new... → New repository')

. . .

![Agregar repositorio](images/github_new_repository.png)

- Puntos extras si saben como licenciar su proyecto!

----

Ahora a clonar el repositorio!
Vamos a la pagina del repositorio y copiamos la URL de clonado SSH (Parte inferior derecha), luego en la terminal:

- `cd ~`
- `mkdir code`
- `git clone git@github.com:pperez/app_evaluaciones_ingsw.git`

## Ta-Dah!

![](images/repo_clonado.png)

Su repositorio esta en `~/code/app_evaluaciones_ingsw`

## Comandos git

<div class="notes">
- `git checkout -b nueva_rama` (Hace una nueva rama basada en la actual)
- `git commit -m "mensaje"` (Hace un commit con el mensaje especificado en el -m)
- `git checkout master` cambia a la branch que queramos
- `git merge otrarama` hace un merge de la otra rama, cuidado con los problemas de merge!
</div>

![](images/comandos_git.png)

---

<div class="notes">
- El push requiere conexión al server (en este caso github)
- Hay que tener cuidado con los merge y como manejarlos
</div>

![](images/comandos_git_2.png)

---

Eso sería lo básico, donde encontrar más:

. . .

Github tiene una buena sección de recursos ([https://help.github.com/articles/good-resources-for-learning-git-and-github/](https://help.github.com/articles/good-resources-for-learning-git-and-github/))

Selección personal:

- Cheatsheet (Torpedo) de git en español ([https://training.github.com/kit/downloads/es/github-git-cheat-sheet.pdf](https://training.github.com/kit/downloads/es/github-git-cheat-sheet.pdf))
- Pro Git ([http://progit.org](http://progit.org))
- Github Guides ([https://guides.github.com/](https://guides.github.com/))

## Instalar el IDE

Como mencioné anteriormente, usaremos [Eclipse](http://eclipse.org) con *PDT* (PHP Development Tools), los pasos:

-  `sudo apt-get install axel`
-  `axel -n50 http://carroll.aset.psu.edu/pub/eclipse/technology/epp/downloads/release/luna/SR1/eclipse-php-luna-SR1-linux-gtk-x86_64.tar.gz`
-  `sudo tar xzvf eclipse-php-luna-SR1-linux-gtk-x86_64.tar.gz -C /opt`
-  `sudo ln -s /opt/eclipse/eclipse /usr/local/bin`
-  `sudo wget http://git.io/VhjClg -O /usr/share/applications/eclipse.desktop`
-  `rm eclipse-php-luna-SR1-linux-gtk-x86_64.tar.gz`

---

<iframe src="http://showterm.io/a8fa8b6ec4d10ef0b342f#slow" width="800" height="520"></iframe>

---

![Eclipse](images/eclipse_icon.png)

## Configurar el IDE contra el directorio del proyecto

Placeholder ;)

# Introducción al patrón MVC

## Que es un patrón de diseño arquitectónico

<div class="notes">
- Modelo: Objetos del mundo real, del dominio del problema, maneja datos, lógica y reglas de la app (ej: Usuario, Estudiante)
- Vista: Representación de salida al usuario (ej: HTML, JSON, XML, etc)
- Controlador: Lógica de interacción con el usuario, recibe, convierte datos e interactua con modelos y vistas
</div>

Es una solución reconocida (connotada) a un problema recurrente de diseño (Como estructuramos nuestra aplicación).

## MVC

El patrón que utilizaremos será *MVC* o *M*odel *V*iew *C*ontroller, este separa la aplicación en 3 capas:

- Modelos
- Vistas
- Controladores

## Modelos

<div class="notes">
Blog: (Modelos: Entradas, Usuarios, Comentarios)
Controladores: EntradasController, UsersController, ComentariosController

/entradas/\{id\}/comentarios
/usuarios/
</div>

Los modelos se refiere al conjunto de clases que representa nuestro dominio del problema (Relación con el paradigma orientado a objetos).

## Modelos

*Laravel* nos da una herramienta llamada *Eloquent* para manejar los modelos, estos tienen relación directa con nuestra base de datos (*Eloquent* es un ORM, este mapea objetos a filas de base de datos), el ORM automáticamente construira consultas para la base de datos.

## Modelos

El ORM permite trabajar los objetos, por ejemplo, `Modelo::all()` nos entregará una lista con todos los objetos de esa clase, `Modelo::find(5)` entregará el objeto cuya llave primaria sea igual a 5. Se pueden pedir otras cosas al ORM, como condiciones `where` o consultar relaciones `1/n`.

. . .

En fin, si quiere más información, lo veremos prontamente, por este mismo horario, mismo canal.

## URIs, requests, verbos HTTP (Paréntesis)

Un *URI* es un identificador único de un recurso (`http://tequila.com/perros/5`).
Un request es una petición realizada a un recurso mediante su *URI*, la petición debe indicar un verbo http, el que dice si estamos pidiendo, actualizando o enviando información (Aquí enviamos información al servidor).
Un request debe tener una respuesta, la que es entregada al usuario, esta puede tener un código de respuesta (i.e: 500, 200, el infame error 404, etc), 

## URIs, requests, verbos HTTP

Los verbos HTTP más utilizados son:

- `GET`
- `HEAD`
- `POST`
- `PUT`
- `DELETE`
- `PATCH`

## GET

Pide la representación de un recurso específico, el fin es obtener información, no debe haber otro efecto adverso.

## Head

Pide una respuesta

## Controladores

Los controladores son la forma en las que interactuamos con la aplicación, en el caso particular de los frameworks web que implementan MVC las acciones se realizan a través de una URI y de verbos HTPP:

- `GET /perros`
- `POST /perros`
- `GET /perros/5`
- `DELETE /perros/10`



# Fin
