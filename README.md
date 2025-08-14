# redborder-repo

Este repositorio permite construir paquetes RPM de un producto específico de Redborder, ideal para controlar las distribuciones específicas para una versión de Redborder concreta.

## Construir una versión específica del producto
Para compilar un RPM de una versión concreta del producto:

```
PRODUCT_VERSION=25.04 VERSION=0.0.1 make rpm
```

## Construir la última versión disponible
Si no se especifica **PRODUCT_VERSION**, por defecto se usará `latest`:

```bash
make
```

## Construir desde una URL distinta
Para usar un repositorio personalizado, por defecto se usará `https://packages.redborder.com`:

```bash
REPO_URL="https://packages.redbordersc.lan" make
```


## Construir el paquete para una versión fixeada
En packages guardamos todas las versiones de redborder, coordinadas todas por redborder-repo. Para una release específica construimos el rpm así:

```bash
PRODUCT_VERSION=00.00 make
```

## Construir el paquete para testing
En packages guardamos las versiones para la primera build con jenkins. Para esta primera versión construimos el rpm así:

```bash
PRODUCT_VERSION=testing make
```

## Construir el repo para desarrolladores
Si queremos instalar versiones personalizadas según el **desarrollador** que esté con una tarea específica, podemos construir el paquete especificando el nombre de usuario. Por ejemplo, si el usuario es `ljblanco` lanzaríamos lo siguiente:

```bash
PRODUCT_VERSION=devel USERNAME=ljblanco make
```

# Testing
El proposito de los rpms es subirlos hacia la URL mencionada e instalar el paquete usando rpm -ivh. Sin embargo, para testear este repositorio, podemos lanzar
```bash
<parámetros opcionales> make
yum install packaging/rpm/pkgs/<nombre del paquete> -y
```
Esto nos debería crea un nuevo fichero `.repo` en `/etc/yum.repos.d/` y cuyo contenido hemos definido en el template de configuración `redborder|devel.repo`
