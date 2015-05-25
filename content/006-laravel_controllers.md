% Controladores en Laravel
% Patricio Pérez <patricio.perez@ceinf.cl>
% Primer semestre 2015

# El tintero!

## Haciendo pruebas con la shell de laravel

Es natural que queramos ver si todo lo que hemos hecho funciona, ver algo de datos en la db, en general ver si metimos o no la pata.

. . .

*Laravel* incluye una consola interactiva (o *REPL*) para ir probando código.

---

~~~bash
$ php artisan tinker
~~~

---

Demo time!

---

~~~php
$rol_encargado = App\Models\Rol::create(['nombre' => 'Encargado Campus']);
$encargado_macul = App\Models\User::create(['rut' => '8069139', 'nombres' => 'Ivan Alexis', 'apellidos' => 'Kemp Reyes', 'email' => 'macullallea@utem.cl']);
$rol_encargado->users()->attach($encargado_macul);

$macul = new App\Models\Campus;
$macul->nombre = 'Campus Macul';
$macul->encargado()->associate($encargado_macul);
$macul->save();
$facultad_ing = new App\Models\Facultad;
$facultad_ing->nombre = 'Facultad Ingenieria';
$facultad_ing->campus()->associate($macul);
$facultad_ing->save();

$carrera_informatica = new App\Models\Carrera;
$carrera_informatica->nombre = "Ingenieria en Informatica";
$carrera_informatica->codigo = 21030;
$facultad_ing->carreras()->save($carrera_informatica);
~~~

# Rutas

## Servidor web

Este punto es importante, serviremos la aplicacion web usando el servidor integrado de php:

~~~bash
php artisan serve
~~~

Basta que abran el browser en [http://localhost:8000](http://localhost:8000)

---

![Welcome](media/welcome_l5.png)

## Rutas

Es necesario definir como interactua el usuario final con nuestra aplicación, para esto se utiliza el framework de *Routing*, este mapea una *URI + verbo HTTP* a un método existente en algún controlador*.

---

~~~bash
cat app/Http/routes.php
~~~

~~~php
<?php

// ...

Route::get('/', 'WelcomeController@index');

Route::get('home', 'HomeController@index');

Route::controllers([
	'auth' => 'Auth\AuthController',
	'password' => 'Auth\PasswordController',
]);
~~~

## Definiendo rutas

Los verbos http son los que la llevan aquí:

~~~php
Route::get('pato', function()
{
    return 'Patoh';
});

Route::post('hola/holaa', function()
{
    return 'Hola World';
});

Route::put('foo/bar', function()
{
    //
});

Route::delete('foo/bar', function()
{
    //
});
~~~

Basta que disparemos con nuestro navegador a las urls correspondientes y deberiamos 

## Pasando parámetros

Hagamoslo más interesante, obtengamos parámetros desde la url:

~~~php
Route::get('hola/{nombre}', function($nombre)
{
    return 'Hola ' . $nombre;
});
~~~

Prueben en su [navegador](http://localhost:8000/hola/patricio)

## Otros detalles

Algunas funcionalidades de rutas:

* Restricciones con expresiones regulares (#valecorby)
* Parámetros por defecto
* Usar prefijos
* Usar subdominios

---

* Acceder a ellas por nombre (Lo veremos más a fondo)
* Binding a modelos (Lo veremos más a fondo)
* Pasar más de un parámetro (ej: /decir/hola/pedro; /decir/saludar/pedro)
* Agrupar rutas (Para ejecución de `middlewares` y `namespaces`, lo veremos...)
* Usar controladores RESTful

# Controladores

## La C del MVC

Concentraremos la lógica de acción de nuestra aplicación en estos. Son básicamente el pegamento entre los datos (Modelos) y lo que se ve (Vistas).

## Estructura

Los controladores son clases, heredan de `Controller`, sus métodos son referenciados desde alguna ruta y se encargan de trabajar con datos en función a los requerimientos del usuario.

---

~~~php
<?php namespace App\Http\Controllers;

use App\Http\Controllers\Controller;

class UserController extends Controller {

    /**
     * Show the profile for the given user.
     *
     * @param  int  $id
     * @return Response
     */
    public function showProfile($id)
    {
        $user = User::findOrFail($id);
        return view('user.profile')
               ->with('user', $user);
    }
}
~~~

---

~~~bash
cat app/Http/routes.php
~~~

~~~php
Route::get('user/{id}', 'UserController@showProfile');
~~~

## Controladores RESTful

El tema con REST es aprovecharse de los verbos HTTP para modelar el comportamiento de la aplicación:

* Al hacer POST a un recurso, crear un nuevo registro
* Al hacer DELETE a un recurso específico, eliminarlo
* Al hacer GET a un recurso específico, mostrar sus detalles

## Crear un controlador RESTful

Desde Laravel 5.0 se le puso más amor al generador de código:

~~~bash
php artisan make:controller Backend/SalasController
~~~

---

~~~php
<?php namespace App\Http\Controllers\Backend;

use App\Http\Requests;
use App\Http\Controllers\Controller;

use Illuminate\Http\Request;

class SalaController extends Controller {
	public function index() {}
	public function create() {}
	public function store() {}
	public function show($id) {}
	public function edit($id) {}
	public function update($id) {}
	public function destroy($id) {}
}
~~~

## Que haremos?

Hoy armaremos una demo (funcional!) de un CRUD (Create, Read, Update, Delete) para el backend del encargado de campus.
