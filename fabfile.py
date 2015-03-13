from fabric.api import *
import sys
import os
import glob
#from datetime import datetime

# Modo semi-tuja
BASE_DIR = os.path.abspath(os.path.curdir)
SOURCE_FILES = os.path.join(BASE_DIR, 'content', '*.md')
MEDIA_SOURCE_DIR = os.path.join(BASE_DIR, 'content', 'media')
DEST_DIR = BASE_DIR
MEDIA_DEST_DIR = os.path.join(DEST_DIR, 'media')

REVEAL_JS_SOURCE_DIR = os.path.join(BASE_DIR, 'reveal.js')

def clean():
    if os.path.isdir(DEST_DIR):
        local('rm -rf {0}'.format(os.path.join(DEST_DIR, '*.html')))
        local('rm -rf {0}'.format(MEDIA_DEST_DIR))

def build():
    clean()
    #local('cp -rf {0} {1}'.format(REVEAL_JS_SOURCE_DIR, DEST_DIR))
    local('cp -rf {0} {1}'.format(MEDIA_SOURCE_DIR, MEDIA_DEST_DIR))
    for fichero in glob.glob(SOURCE_FILES):
        nombre = os.path.splitext(os.path.split(fichero)[-1])[0]
        destino = os.path.join(DEST_DIR, nombre + '.html')
        local('pandoc --slide-level 2 -f markdown -t revealjs --incremental --mathjax -V theme=night -s {0} -o {1}'.format(fichero, destino))

def serve():
    local('cd {0} && python -m SimpleHTTPServer 9000'.format(DEST_DIR))

def watch():
    build()
    local('watchmedo shell-command --timeout 5.0 --wait --ignore-directories --pattern="./content/*" --recursive --command="fab build" .')
