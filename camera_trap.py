import os
import RPi.GPIO as GPIO
import time
import picamera

# Define the time after the last motion detection until the camera continues to record
record_time = 30

# Define the directory into which the video should be recorded
out_dir = '/home/pi/Desktop/'

# Initialize these important variables used later
remaining_time = 0
recording = False

# Set, whether you want to preview the recording
preview = False

# Initialize hardware
camera = picamera.PiCamera()
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)


def main():
    global out_dir, remaining_time, recording, preview
    print('Photo trap is ready and running.')

    try:
        GPIO.add_event_detect(PIR_PIN, GPIO.BOTH, callback=motion)
        while True:
            # Decrease the recording time if greater than zero
            if remaining_time > 0:
                remaining_time -= 1
                
            # Start recording if required
            if not recording and remaining_time > 0:
                recording = True
                timestamp = str(time.time()).split('.')[0]
                camera.start_recording(os.path.join(out_dir, 'video-%s.h264' % timestamp))
                print('start recording')
                if preview:
                    camera.start_preview()
                
            # End recording if required
            elif recording and remaining_time <= 0:
                recording = False
                camera.stop_recording()
                print('stop recording')
                if preview:
                    camera.stop_preview()
            # DEBUG:
            # print('record will end in ' + str(remaining_time) + ' seconds.')
            time.sleep(1)
            
    except KeyboardInterrupt:
        print('Quit')
        GPIO.cleanup()


def motion(PIR_PIN):
    """
    Callback function is called after a motion has been detected. It returns the total recording time,
    which always starts by new after a motion has been detected. 
    :param int PIR_PIN: The pin to which the motion detection sensor is connected to the RasPi
    return global variable remaining_time (as the callback function has no return variable, we use a
    global variable instead.
    """
    global remaining_time
    remaining_time = record_time
    # DEBUG:
    # print('Boolean: ' + str(GPIO.input(PIR_PIN)))


if __name__ == '__main__':
    # Start the main process
    main()

