#!/usr/bin/python3

import time
import numpy as np
from picamera2 import Picamera2

picam2 = Picamera2()

# picam2.start_preview(Preview.QTGL)
preview_config = picam2.create_preview_configuration()
capture_config = picam2.create_still_configuration(raw={}, display=None)

picam2.configure(preview_config)
picam2.start()
time.sleep(0.5)
# image.show()

# w, h = 4056,3040

prev = None
last_save_time = 0
save_interval=3

while True:
    # cur = picam2.capture()
    cur_array = picam2.capture_array()

    if prev is not None:
        # Measure pixel differences between current and previous frame
        mse = np.square(np.subtract(cur_array, prev)).mean()
        print("capture mse", mse)
        if mse > 7:
            current_time = time.time()
            if current_time - last_save_time > save_interval:
                # Save the current frame as an image
                image_name = "./img/"+f"{int(current_time)}.jpg"
                picam2.switch_mode_and_capture_file(capture_config, image_name)
                # cur.save(image_name)
                print("New Motion", mse)
                last_save_time = current_time

    prev = cur_array
    
    picam2.stop()
    
    capture_config = picam2.create_still_configuration()
    picam2.configure(preview_config)
    
    picam2.start()
    time.sleep(0.5)
