TARGETDIR=$(DESTDIR)/lib/udev/devices

install:
	install -d $(DESTDIR)/etc/udev/rules.d
	install -m 644 90-elphel-automount.rules $(DESTDIR)/etc/udev/rules.d

	install -d $(TARGETDIR)
	mknod -m 0622   $(TARGETDIR)/circbuf0   c 135   32
	mknod -m 0622   $(TARGETDIR)/circbuf1   c 135   33
	mknod -m 0622   $(TARGETDIR)/circbuf2   c 135   34
	mknod -m 0622   $(TARGETDIR)/circbuf3   c 135   35

	mknod -m 0622   $(TARGETDIR)/jpeghead0  c 135   48
	mknod -m 0622   $(TARGETDIR)/jpeghead1  c 135   49
	mknod -m 0622   $(TARGETDIR)/jpeghead2  c 135   50
	mknod -m 0622   $(TARGETDIR)/jpeghead3  c 135   51

	mknod -m 0622   $(TARGETDIR)/exif_exif0     c 125   16
	mknod -m 0622   $(TARGETDIR)/exif_exif1     c 125   17
	mknod -m 0622   $(TARGETDIR)/exif_exif2     c 125   18
	mknod -m 0622   $(TARGETDIR)/exif_exif3     c 125   19

	mknod -m 0622   $(TARGETDIR)/exif_meta0     c 125   32
	mknod -m 0622   $(TARGETDIR)/exif_meta1     c 125   33
	mknod -m 0622   $(TARGETDIR)/exif_meta2     c 125   34
	mknod -m 0622   $(TARGETDIR)/exif_meta3     c 125   35

	mknod -m 0622   $(TARGETDIR)/exif_template  c 125   2
	mknod -m 0622   $(TARGETDIR)/exif_metadir   c 125   3
