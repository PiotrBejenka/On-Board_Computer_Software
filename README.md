# On-board_Computer_Software
Part of my engineering project - inspection vehicle on-board computer software.

### Needed stuff:
- Raspberry Pi (I used RPi 4b)
- camera (I used the RPi Camera v2)
- LED ring (I used a ring with 12 RGB WS2812 5050 LEDs)
- dc engines controller (I used a two-channel motor driver - Pololu TB6612FNG)
- dc engines(I used N20 motors which are similar to the popular Pololu DC motors) 
- three push buttons (two are enough for the main tasks)<br /> <br />

### ! The program must be run as root. Command to run: sudo python3 <program_name.py>. This is required by the neopixel library that supports the LED ring !

<br />

The on-board computer was prepared for the pipeline visual inspection vehicle. Such a device is designed to record images from the pipeline. Movable structure allows to take turns with a constant engine control value.
<br />

The main tasks, which are switching on the lighting, starting the engines and recording, are triggered by pressing the first button, which should be done after placing the vehicle in the pipe. Pressing another button, which should be done after the vehicle leaves the other side of the pipeline, will turn off the lighting, stop the engines and stop recording.
<br />

The third button is for "safe" shutdown of the minicomputer. This is useful to use it after the inspection is completed if you put the RPi in the vehicle and add the program start command to the rc.local file (the program will start when the system boots, which will happen when the power source is connected to the minicomputer). A sliding or rocker switch should be placed between the RPi and the power source to control the connection to the power supply.
