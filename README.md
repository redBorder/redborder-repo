# redborder-repo

RPM package that configures the official redBorder yum repository on RHEL 9 systems.

## What it installs

| File | Destination |
|------|-------------|
| `redborder-<PRODUCT_VERSION>.repo` | `/etc/yum.repos.d/` |
| `RPM-GPG-KEY-redborder-repo` | `/etc/pki/rpm-gpg/` |

## Requirements

- `mock` must be installed and configured on the build host.
- `epel-release` is required as a runtime dependency on the target system.

## Build variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PRODUCT_VERSION` | `latest` | redBorder product release series (e.g. `25.04`, `26.06`) |
| `VERSION` | `git describe` | RPM version, derived automatically from git tags |
| `BUILD_NUMBER` | `1` | RPM release number |
| `REPO_URL` | `https://packages.redborder.com/releases` | Base URL for the repository |
| `MOCK_CONFIG` | `default` | mock configuration profile to use |

## Usage

Build using the current product version and auto-derived git version:

```bash
make rpm
```

Build for a specific product version:

```bash
PRODUCT_VERSION=25.04 VERSION=0.0.1 make rpm
```

Build with a custom repository URL:

```bash
VERSION=0.0.1 REPO_URL="https://packages.redborder.com" make rpm
```

The resulting RPMs are placed in `packaging/rpm/pkgs/`.

## Makefile targets

| Target | Description |
|--------|-------------|
| `rpm` | Build source and binary RPMs (default) |
| `srpm` | Build source RPM only |
| `archive` | Create the source tarball |
| `clean` | Remove build artifacts (`SOURCES/`, `pkgs/`) |
| `distclean` | Deep clean including logs and leftover RPMs |
