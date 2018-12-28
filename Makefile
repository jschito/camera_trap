all: camera_trap.py

install: camera_trap.py
	cp camera_trap.py /etc/init.d/
	chmod +x /etc/init.d/camera_trap.py
	update-rc.d camera_trap.py defaults
uninstall:
	update-rc.d camera_trap.py disable
	rm /etc/init.d/camera_trap.py
	update-rc.d camera_trap.py remove

