
INSTALL_DIR = /usr/bin

install:
	rm -rf $(INSTALL_DIR)/todopy-source $(INSTALL_DIR)/todopy
	cp -r ../todopy $(INSTALL_DIR)/todopy-source
	cp src/todopy $(INSTALL_DIR)
	chmod 777 $(INSTALL_DIR)/todopy-source/src/list.json
	chmod 777 $(INSTALL_DIR)/todopy-source/src/*.py
	chmod 777 $(INSTALL_DIR)/todopy-source/src/*.pyc
