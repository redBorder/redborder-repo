# redborder-repo

Este repositorio permite construir paquetes RPM de un producto específico de Redborder.

## Construir una versión específica del producto
Para compilar un RPM de una versión concreta del producto:

```
PRODUCT_VERSION=25.04 VERSION=0.0.1 make rpm
```

## Construir la última versión disponible
Si no se especifica **PRODUCT_VERSION**, por defecto se usará `latest`:

```bash
VERSION=0.0.1 make rpm
```

## Construir desde una URL distinta
Para usar un repositorio personalizado, por defecto se usará `https://packages.redborder.com`:

```bash
VERSION=0.0.1 REPO_URL="https://packages.redbordersc.lan" make rpm
```

## Construir el repo para desarrolladores
Si queremos instalar versiones personalizadas según el desarrollador que esté con una tarea específica, podemos construir el paquete especificando el nombre de usuario. Por ejemplo, si el usuario es `ljblanco` y ya existe una versión desactualizada el directorio de la URL, lanzaríamos lo siguiente:

```bash
USERNAME=ljblanco VERSION=0.0.2 make
```

# Testing
El proposito de los rpms es subirlos hacia la URL mencionada e instalar el paquete usando rpm -ivh. Sin embargo, para testear este repositorio, podemos lanzar
```bash
make
yum localinstall packaging/rpm/pkgs/<nombre del paquete> -y
```
Esto nos debería crea un nuevo fichero `.repo` en `/etc/yum.repos.d/` y cuyo contenido hemos definido en el fichero de configuración `redborder.repo`
