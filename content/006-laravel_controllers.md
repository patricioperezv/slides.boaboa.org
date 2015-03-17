% Laravel 5.0
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

# Rutas y controladores

## Rutas

Es necesario definir como interactua el usuario final con nuestra aplicación, para esto se utiliza el framework de *Routing*, este mapea una *URI + verbo HTTP* a un método existente en algún controlador*.

