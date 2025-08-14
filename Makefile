
all: rpm

rpm:
	$(MAKE) -C packaging/rpm rpm

clean:
	rm -rf packaging/rpm/SOURCES pkgs
