# redborder-repo

Build a particular product version:

```
PRODUCT_VERSION=25.04 VERSION=0.0.1 make rpm
```

Build latest (by default PRODUCT_VERSION=latest):

```
VERSION=0.0.1 make rpm
```

Build with different URL:
```
VERSION=0.0.1 REPO_URL="https://packages.redborder.com" make rpm
```