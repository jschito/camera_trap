import RPi.GPIO as GPIO
import time
import picamera

camera = picamera.PiCamera()
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

record_time = 20
remaining_time = 0
recording = False

def MOTION(PIR_PIN):
    global remaining_time
    remaining_time = record_time
    print('Boolean: ' + str(GPIO.input(PIR_PIN)))

print('Photo trap is ready and running.')

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.BOTH, callback=MOTION)
    while True:
        if remaining_time > 0:
            remaining_time -= 1
            
        # Start recording if required
        if not recording and remaining_time > 0:
            recording = True
            timestamp = str(time.time()).split('.')[0]
            camera.start_recording('/home/pi/Desktop/video-%s.h264' % timestamp)
            print('start recording')
            camera.start_preview()
            
        # End recording if required
        elif recording and remaining_time <= 0:
            recording = False
            camera.stop_recording()
            print('stop recording')
            camera.stop_preview()
        
        print(remaining_time)
        time.sleep(1)
        
except KeyboardInterrupt:
    print('Quit')
    GPIO.cleanup()
