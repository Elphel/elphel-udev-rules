#!/bin/sh
mknod -m 0666   /dev/circbuf0   c 135   32
mknod -m 0666   /dev/circbuf1   c 135   33
mknod -m 0666   /dev/circbuf2   c 135   34
mknod -m 0666   /dev/circbuf3   c 135   35

mknod -m 0666   /dev/jpeghead0  c 135   48
mknod -m 0666   /dev/jpeghead1  c 135   49
mknod -m 0666   /dev/jpeghead2  c 135   50
mknod -m 0666   /dev/jpeghead3  c 135   51

mknod -m 0666   /dev/exif_exif0     c 125   16
mknod -m 0666   /dev/exif_exif1     c 125   17
mknod -m 0666   /dev/exif_exif2     c 125   18
mknod -m 0666   /dev/exif_exif3     c 125   19

mknod -m 0666   /dev/exif_meta0     c 125   32
mknod -m 0666   /dev/exif_meta1     c 125   33
mknod -m 0666   /dev/exif_meta2     c 125   34
mknod -m 0666   /dev/exif_meta3     c 125   35

mknod -m 0666   /dev/exif_template  c 125   2
mknod -m 0666   /dev/exif_metadir   c 125   3
