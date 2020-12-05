# Editing code on the esp32

## Thonny

Currently pretty happy with Thonny. Makes it easy to access and manipulate the files on the device.

For a new file on save you have the option to save it directly to the device or to local files. Save As... will give option to save an existing file to either destination.

Once the device directory is displayed, you can create folders, delete files etc. from the small hamburger icon in the upper right of the dialog.

### Thonny File Manager:

Thonny has a pretty handy file manager. Choose View -> Files to display the files sidebar. You can copy files to/from the device and also create directories.

## Adafruit-ampy

Playing with ampy as a file transfer tool.

```ampy --port /dev/cu.SLAB_USBtoUART put <file>```

## rshell

A bit easier to use, more like being directly connected to the device and can also open a REPL
by typing `repl`.

install with `pip install rshell` and launch with `rshell` alone or `rshell -p /dev/cu.SLAB_USBtoUART`

Sometimes it seem I need to unplug the device and re-insert to get access to the device. May be the the
caused by the fact I have been trying to access it with screen and not exiting correctly.

rshell is much easier. Has all the typical commands you need to access the files on the device.

