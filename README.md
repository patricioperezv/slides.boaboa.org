slides.boaboa.org
=======

Este repositorio contiene los fuentes y html de las presentaciones para boaboa.org, utiliza el hosting de github-pages (it's free!).

Para utilizarlo es necesario instalar un par de cosillas:

- [Pandoc](http://johnmacfarlane.net/pandoc/) (Transforma desde markdown al framework de presentaciones [reveal.js](http://lab.hakim.se/reveal-js/#/))
- [Fabric](http://www.fabfile.org/) (Automatiza la tarea de ejecutar pandoc, borrar directorios y otras)
- [Watchdog](https://pypi.python.org/pypi/watchdog) (No es taaan necesario, pero es comodo, permite detectar cambios en los ficheros markdown y regenerar las presentaciones)
- Un editor de markdown (Sólo por comodidad, hasta un nano de perros basta, en OSX uso [MacDown](http://macdown.uranusjr.com/))


Para instalar todas las dependencias en OSX hice lo siguiente:

```bash
sudo pip install fabric watchdog
brew install pandoc
```

Asumiendo que ya tenemos funcionando pip (Uso el python de Homebrew, a eso le instale pip y presto) y [Homebrew](http://brew.sh/) (No es tan cómodo como apt, pero de algo se parte...).

Despues de tooodo eso, ya podría empezar a generar presentaciones, generando ficheros .md en el directorio `content`, meter las imagenes en `content/images`.

Los comandos que trae para la automatización son:

* `fab build` Regenera los ficheos de salida (html + imagenes)
* `fab watch` *Vigila* los cambios realizados en `content/*.md`, si detecta alguno se pega un `fab build` :heart_eyes_cat:
* `fab serve` Ejecuta un servidor http integrado de python, para servir las presentaciones (Útil para ir probando las presentaciones)
