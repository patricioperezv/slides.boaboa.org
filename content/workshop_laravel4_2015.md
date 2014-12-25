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
</div>

El resumen corto de todo eso (En mi opinión bien vaga) es que sus proyectos deben cumplir:

- Planificación (No hagan todo a última hora)
- Estándares (Quizas no los de industrias, ISO, IEEE, sino estándares fijados por ustedes)


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
- Que sus commits indiquen (o traten) que cambio realizaron en el código
- Idealmente usen branches (ramas) al desarrollar, cuando la funcionalidad que agregaron este "lista" hacen merge a su branch principal (e.g: master)

## Perfil

![Mi perfil en github](images/github_profile.png)

## Config git

![Config git](images/git_config.png)

## Log de commits

![Commit log](images/commit_tree.png)
