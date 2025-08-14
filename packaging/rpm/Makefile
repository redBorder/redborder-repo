PRODUCT_VERSION?= latest # devel | latest | testing | xx.x.x

ifeq (devel,$(PRODUCT_VERSION))
USERNAME?= noob
else
USERNAME= redborder
endif

VERSION?=	$(shell git describe --abbrev=6 --tags HEAD --always | sed 's/-/_/g')

BUILD_NUMBER?= 1

MOCK_CONFIG?=default

RESULT_DIR?=pkgs

REPO_URL?=https://packages.redborder.com

# Nombre del paquete: si PRODUCT_VERSION=devel, sin versión; si no, agrega versión
IS_DEVEL := $(findstring devel,$(PRODUCT_VERSION))
VERSION_SUFFIX := $(if $(IS_DEVEL),,$(-$(PRODUCT_VERSION)))
PACKAGE_NAME = $(USERNAME)-repo$(VERSION_SUFFIX)

# Nombre de template de repo: devel.repo si devel, redborder.repo para el resto
REPO_TEMPLATE ?= $(if $(filter devel,$(PRODUCT_VERSION)),devel.repo,redborder.repo)

# Nombre final del archivo de repo: si devel, $(USERNAME).repo; redborder-$(VERSION).repo para el resto
REPO_FILENAME ?= $(if $(filter devel,$(PRODUCT_VERSION)),$(USERNAME).repo,redborder-$(VERSION).repo)

all: rpm

SOURCES:
	mkdir -p SOURCES

archive: SOURCES
	cd ../../ && \
	git archive --prefix=$(PACKAGE_NAME)-$(VERSION)/ \
		-o packaging/rpm/SOURCES/$(PACKAGE_NAME)-$(VERSION).tar.gz HEAD

build_prepare: archive
	mkdir -p $(RESULT_DIR)
	rm -f $(RESULT_DIR)/$(PACKAGE_NAME)*.rpm

srpm: build_prepare
	/usr/bin/mock \
		-r $(MOCK_CONFIG) \
		--define "__product_version $(PRODUCT_VERSION)" \
		--define "__username $(USERNAME)" \
		--define "__package_name $(PACKAGE_NAME)" \
		--define "__version $(VERSION)" \
		--define "__release $(BUILD_NUMBER)" \
		--define "__repo_url $(REPO_URL)" \
		--define "__repo_template ${REPO_TEMPLATE}" \
		--define "__repo_filename ${REPO_FILENAME}" \
		--resultdir=$(RESULT_DIR) \
		--buildsrpm \
		--spec=redborder-repo.spec \
		--sources=SOURCES
	@echo "======= Source RPM now available in $(RESULT_DIR) ======="

rpm: srpm
	/usr/bin/mock \
		-r $(MOCK_CONFIG) \
		--define "__product_version $(PRODUCT_VERSION)" \
		--define "__username $(USERNAME)" \
		--define "__package_name $(PACKAGE_NAME)" \
		--define "__version $(VERSION)"\
		--define "__release $(BUILD_NUMBER)"\
		--define "__repo_url $(REPO_URL)" \
		--define "__repo_template ${REPO_TEMPLATE}" \
		--define "__repo_filename ${REPO_FILENAME}" \
		--resultdir=$(RESULT_DIR) \
		--rebuild $(RESULT_DIR)/$(PACKAGE_NAME)*.src.rpm
	@echo "======= Binary RPMs now available in $(RESULT_DIR) ======="

clean:
	rm -rf SOURCES pkgs

distclean: clean
	rm -f build.log root.log state.log available_pkgs installed_pkgs \
		*.rpm *.tar.gz
