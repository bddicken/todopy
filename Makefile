
INSTALL_DIR = /usr/bin

install:
	rm -r $(INSTALL_DIR)/todopy-source $(INSTALL_DIR)/todopy
	cp -r ../todopy/src $(INSTALL_DIR)/todopy-source
	ln -s $(INSTALL_DIR)/todopy-source/main.py $(INSTALL_DIR)/todopy
	chmod 777 $(INSTALL_DIR)/todopy-source/list.json
	chmod 777 $(INSTALL_DIR)/todopy-source/*.py
