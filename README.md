# camera_trap
Records a video after a movement is detected by a motion detection sensor (e.g., of a fox in front of the camera trap).

# Hardware used
- Raspberry Pi 3 Model B+
- Raspberry Pi Camera V 2.1 (including connection cable)
- PIR Infrared Motion Sensor (HC-SR501)

## Picture of the test setting:
![hardware](https://raw.githubusercontent.com/jschito/camera_trap/master/pics/pic1.jpg)

# Installation
The following command copies camera_trap.py to directory where the deamons are located. This allows that the programm will be automatically started after booting (in the desired run level).
```Shell
sudo make install
```

# Uninstallation
Execute the following uninstallation command if you do not longer want to automatically run camera_trap.py after booting your system.
```Shell
sudo make uninstall
```
