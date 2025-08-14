# redborder-repo

This repository allows building RPM packages for a specific Redborder product, ideal for controlling specific distributions for a particular Redborder version.

## Build a specific product version
To compile an RPM for a specific product version:

```bash
PRODUCT_VERSION=25.04 VERSION=0.0.1 make rpm
```

## Build the latest available version
If **PRODUCT_VERSION** is not specified, `latest` will be used by default:

```bash
make
```

## Build from a different URL
To use a custom repository, the default is `https://packages.redborder.com`:

```bash
REPO_URL="https://packages.redbordersc.lan" make
```

## Build the package for a fixed version
In `packages` we store all Redborder versions, all coordinated through `redborder-repo`. For a specific release, we build the RPM like this:

```bash
PRODUCT_VERSION=00.00 make
```

## Build the package for testing
In `packages` we store the versions for the first Jenkins build. For this first version, we build the RPM like this:

```bash
PRODUCT_VERSION=testing make
```

## Build the repo for developers
If we want to install customized versions according to the **developer** working on a specific task, we can build the package by specifying the username. For example, if the user is `ljblanco`, we would run:

```bash
PRODUCT_VERSION=devel USERNAME=ljblanco make
```

# Testing
The purpose of the RPMs is to upload them to the mentioned URL and install the package using `rpm -ivh`. However, to test this repository, we can run:

```bash
<optional parameters> make
yum install packaging/rpm/pkgs/<package-name> -y
```

This should create a new `.repo` file in `/etc/yum.repos.d/`, whose contents are defined in the configuration template `redborder|devel.repo`.
