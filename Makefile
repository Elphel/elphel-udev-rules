TARGETDIR=$(DESTDIR)/lib/udev/devices
X393_DEVICES=$(STAGING_DIR_HOST)/usr/include-uapi/elphel/x393_devices.h
include generated_include
generated_include:$(X393_DEVICES) generate_mknods.py
	./generate_mknods.py $(X393_DEVICES)  >generated_include

install:generated_include
	install -d $(DESTDIR)/etc/udev/rules.d
	install -m 644 90-elphel-automount.rules $(DESTDIR)/etc/udev/rules.d
	install -d $(TARGETDIR)
	@$(mknodes)
	
clean:
	-rm -f generated_include	
