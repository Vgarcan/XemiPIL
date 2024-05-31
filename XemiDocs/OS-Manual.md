# Guía Extensa del Uso del Paquete `os` en Python

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Importación del Paquete `os`](#importación-del-paquete-os)
3. [Navegación en el Sistema de Archivos](#navegación-en-el-sistema-de-archivos)
    - [Obtener el Directorio Actual](#obtener-el-directorio-actual)
    - [Cambiar de Directorio](#cambiar-de-directorio)
    - [Listar Archivos y Directorios](#listar-archivos-y-directorios)
4. [Manipulación de Archivos y Directorios](#manipulación-de-archivos-y-directorios)
    - [Crear Directorios](#crear-directorios)
    - [Eliminar Archivos y Directorios](#eliminar-archivos-y-directorios)
    - [Renombrar Archivos y Directorios](#renombrar-archivos-y-directorios)
5. [Permisos de Archivos](#permisos-de-archivos)
    - [Cambiar Permisos](#cambiar-permisos)
    - [Cambiar Propietario del Archivo](#cambiar-propietario-del-archivo)
6. [Ejecutar Comandos del Sistema](#ejecutar-comandos-del-sistema)
7. [Variables de Entorno](#variables-de-entorno)
    - [Leer Variables de Entorno](#leer-variables-de-entorno)
    - [Establecer Variables de Entorno](#establecer-variables-de-entorno)
8. [Rutas de Archivos](#rutas-de-archivos)
    - [Obtener Rutas Absolutas](#obtener-rutas-absolutas)
    - [Dividir Rutas](#dividir-rutas)
    - [Comprobar la Existencia de Archivos o Directorios](#comprobar-la-existencia-de-archivos-o-directorios)
9. [Módulo `os.path`](#módulo-ospath)
    - [Unir Rutas](#unir-rutas)
    - [Obtener el Nombre del Archivo y la Extensión](#obtener-el-nombre-del-archivo-y-la-extensión)
    - [Comprobar si es un Archivo o un Directorio](#comprobar-si-es-un-archivo-o-un-directorio)
10. [Manejo de Errores](#manejo-de-errores)
11. [Operaciones de Archivo Avanzadas](#operaciones-de-archivo-avanzadas)
    - [Copiar y Mover Archivos](#copiar-y-mover-archivos)
    - [Uso del Módulo `shutil`](#uso-del-módulo-shutil)
12. [Información de Archivos](#información-de-archivos)
13. [Trabajo con Enlaces Simbólicos](#trabajo-con-enlaces-simbólicos)
14. [Uso de `os.walk` para Recorrer Directorios](#uso-de-oswalk-para-recorrer-directorios)
15. [Operaciones con Tiempos de Archivos](#operaciones-con-tiempos-de-archivos)
16. [Compatibilidad entre Sistemas Operativos](#compatibilidad-entre-sistemas-operativos)
17. [Conclusión](#conclusión)

## Introducción

El módulo `os` en Python proporciona una manera portátil de interactuar con el sistema operativo. Permite realizar operaciones como leer y escribir en el sistema de archivos, manipular rutas y directorios, y ejecutar comandos del sistema. Este módulo es fundamental para scripts y aplicaciones que necesitan interactuar con el entorno en el que se ejecutan.

## Importación del Paquete `os`

Para usar las funciones del módulo `os`, primero debes importarlo en tu script de Python:

```python
import os
```

## Navegación en el Sistema de Archivos

### Obtener el Directorio Actual

Para obtener el directorio de trabajo actual, usa `os.getcwd()`:

```python
import os

current_directory = os.getcwd()
print("Current Directory:", current_directory)
```

### Cambiar de Directorio

Para cambiar el directorio de trabajo actual, usa `os.chdir(path)`:

```python
os.chdir('/path/to/directory')
print("Changed to:", os.getcwd())
```

### Listar Archivos y Directorios

Para listar los archivos y directorios en el directorio actual, usa `os.listdir(path)`:

```python
files = os.listdir('.')
print("Files and Directories in Current Directory:", files)
```

## Manipulación de Archivos y Directorios

### Crear Directorios

Para crear un nuevo directorio, usa `os.mkdir(path)`:

```python
os.mkdir('new_directory')
```

Para crear un nuevo directorio junto con cualquier directorio padre necesario, usa `os.makedirs(path)`:

```python
os.makedirs('parent_directory/child_directory')
```

### Eliminar Archivos y Directorios

Para eliminar un archivo, usa `os.remove(path)`:

```python
os.remove('file.txt')
```

Para eliminar un directorio vacío, usa `os.rmdir(path)`:

```python
os.rmdir('directory')
```

Para eliminar un directorio y todo su contenido, usa `os.removedirs(path)`:

```python
os.removedirs('parent_directory/child_directory')
```

### Renombrar Archivos y Directorios

Para renombrar un archivo o directorio, usa `os.rename(src, dst)`:

```python
os.rename('old_name.txt', 'new_name.txt')
```

## Permisos de Archivos

### Cambiar Permisos

Para cambiar los permisos de un archivo, usa `os.chmod(path, mode)`:

```python
# Establecer permisos de lectura y escritura para el propietario, y de lectura para el grupo y otros
os.chmod('file.txt', 0o644)
```

### Cambiar Propietario del Archivo

Para cambiar el propietario de un archivo, usa `os.chown(path, uid, gid)`:

```python
os.chown('file.txt', 1000, 1000)
```

## Ejecutar Comandos del Sistema

Para ejecutar un comando del sistema, usa `os.system(command)`:

```python
os.system('echo "Hello, World!"')
```

Para una ejecución más segura y avanzada, considera usar el módulo `subprocess`.

## Variables de Entorno

### Leer Variables de Entorno

Para leer una variable de entorno, usa `os.getenv(key, default=None)`:

```python
path = os.getenv('PATH')
print("PATH:", path)
```

### Establecer Variables de Entorno

Para establecer una variable de entorno, usa `os.putenv(key, value)` (ten en cuenta que esta función no está recomendada para nuevos proyectos) o modifica `os.environ` directamente:

```python
os.environ['MY_VARIABLE'] = 'my_value'
print("MY_VARIABLE:", os.getenv('MY_VARIABLE'))
```

## Rutas de Archivos

### Obtener Rutas Absolutas

Para obtener la ruta absoluta de un archivo o directorio, usa `os.path.abspath(path)`:

```python
absolute_path = os.path.abspath('file.txt')
print("Absolute Path:", absolute_path)
```

### Dividir Rutas

Para dividir una ruta en el directorio y el nombre del archivo, usa `os.path.split(path)`:

```python
directory, file_name = os.path.split('/path/to/file.txt')
print("Directory:", directory)
print("File Name:", file_name)
```

### Comprobar la Existencia de Archivos o Directorios

Para comprobar si un archivo o directorio existe, usa `os.path.exists(path)`:

```python
exists = os.path.exists('file.txt')
print("File Exists:", exists)
```

## Módulo `os.path`

El módulo `os.path` incluye funciones para manipular rutas de archivos y directorios.

### Unir Rutas

Para unir varias partes de una ruta, usa `os.path.join(path, *paths)`:

```python
full_path = os.path.join('/path/to', 'directory', 'file.txt')
print("Full Path:", full_path)
```

### Obtener el Nombre del Archivo y la Extensión

Para obtener el nombre del archivo y su extensión, usa `os.path.splitext(path)`:

```python
file_name, file_extension = os.path.splitext('file.txt')
print("File Name:", file_name)
```python
print("File Extension:", file_extension)
```

### Comprobar si es un Archivo o un Directorio

Para comprobar si una ruta es un archivo, usa `os.path.isfile(path)`:

```python
is_file = os.path.isfile('file.txt')
print("Is File:", is_file)
```

Para comprobar si una ruta es un directorio, usa `os.path.isdir(path)`:

```python
is_directory = os.path.isdir('/path/to/directory')
print("Is Directory:", is_directory)
```

## Manejo de Errores

### Capturar Excepciones

Cuando trabajas con operaciones del sistema de archivos, es importante manejar los errores correctamente para evitar que tu programa falle inesperadamente.

```python
try:
    os.remove('file.txt')
except FileNotFoundError as e:
    print(f"Error: {e}")
except PermissionError as e:
    print(f"Error: {e}")
```

### Comprobaciones Previas

Antes de realizar operaciones, comprueba la existencia del archivo o directorio para evitar errores.

```python
if os.path.exists('file.txt'):
    os.remove('file.txt')
else:
    print("File does not exist")
```

## Operaciones de Archivo Avanzadas

### Copiar y Mover Archivos

Para copiar archivos, puedes usar el módulo `shutil`.

```python
import shutil

shutil.copy('source.txt', 'destination.txt')
```

Para mover archivos o directorios:

```python
shutil.move('source', 'destination')
```

### Uso del Módulo `shutil`

El módulo `shutil` ofrece funciones avanzadas para la manipulación de archivos y directorios.

- Copiar directorios recursivamente:

```python
shutil.copytree('source_directory', 'destination_directory')
```

- Eliminar directorios recursivamente:

```python
shutil.rmtree('directory')
```

## Información de Archivos

### Obtener Información del Archivo

Puedes obtener información detallada sobre un archivo utilizando `os.stat(path)`.

```python
file_info = os.stat('file.txt')
print("File Size:", file_info.st_size)
print("Last Modified:", file_info.st_mtime)
```

### Convertir Tiempos de Archivos

Puedes convertir tiempos de archivos a formatos legibles utilizando el módulo `time`.

```python
import time

last_modified = time.ctime(file_info.st_mtime)
print("Last Modified (Readable):", last_modified)
```

## Trabajo con Enlaces Simbólicos

### Crear Enlaces Simbólicos

Para crear un enlace simbólico, usa `os.symlink(src, dst)`:

```python
os.symlink('source_file', 'link_name')
```

### Leer Enlaces Simbólicos

Para leer el destino de un enlace simbólico, usa `os.readlink(path)`:

```python
link_target = os.readlink('link_name')
print("Link Target:", link_target)
```

## Uso de `os.walk` para Recorrer Directorios

La función `os.walk` permite recorrer directorios de forma recursiva.

```python
for dirpath, dirnames, filenames in os.walk('/path/to/directory'):
    print("Current Path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)
```

## Operaciones con Tiempos de Archivos

### Obtener y Modificar Tiempos de Archivos

Para obtener los tiempos de acceso y modificación de un archivo, usa `os.path.getatime(path)` y `os.path.getmtime(path)`.

```python
access_time = os.path.getatime('file.txt')
modification_time = os.path.getmtime('file.txt')
print("Access Time:", time.ctime(access_time))
print("Modification Time:", time.ctime(modification_time))
```

Para cambiar los tiempos de acceso y modificación de un archivo, usa `os.utime(path, times)`.

```python
os.utime('file.txt', (new_access_time, new_modification_time))
```

## Compatibilidad entre Sistemas Operativos

### Identificar el Sistema Operativo

Puedes identificar el sistema operativo en el que se está ejecutando tu script usando `os.name` o `platform.system()`.

```python
import platform

print("OS Name:", os.name)
print("Platform:", platform.system())
```

### Escribir Código Portátil

Para escribir código portátil, usa funciones de `os` y `os.path` en lugar de comandos específicos del sistema operativo.

```python
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')
```

## Conclusión

El módulo `os` de Python es una herramienta poderosa para interactuar con el sistema operativo. Desde la navegación y manipulación del sistema de archivos hasta la ejecución de comandos del sistema y la gestión de variables de entorno, `os` proporciona una amplia gama de funcionalidades esenciales para el desarrollo de scripts y aplicaciones robustas y portátiles. Al combinar `os` con `shutil`, puedes realizar operaciones de archivos avanzadas de manera efectiva y eficiente.
