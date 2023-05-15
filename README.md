# pi-stillframe

This is a simple Flask web application that captures an image from a camera, adds a timestamp to the image, and serves it at an endpoint.

## Dependencies

- Flask: A lightweight web framework for Python.
- Pillow: A library for opening, manipulating, and saving image files.
- libcamera (optional): A camera library for capturing images (ensure the camera is supported by this library).

Brief instructions:
* make sure you can have write access to the directory the script is in  
* start Flask server `python app.py`  
* open a web browser and type in `XX.XXX.X.XXX:8899/show_img`


The IP address and port number to access the camera will be displayed in the console. Open a web browser and navigate to the displayed address to view the timestamped image.

Please note that this app is designed to work with cameras supported by the `libcamera` library. If your camera is not supported, you may need to modify the `show_img()` function to use an alternative method for capturing images.


### alt_motion
This is a Python script that captures images with the Picamera2 library and detects motion by comparing consecutive frames. If motion is detected, the current frame is saved as an image.

#### How it works

1. The script initializes the Picamera2 object and sets up preview and capture configurations.
2. In an infinite loop, the script captures frames and calculates the mean squared error (MSE) between the current and previous frames.
3. If the MSE exceeds a predefined threshold and a certain time has passed since the last saved image, the script saves the current frame as an image file.

#### Running the script

run `python alt_motion.py`  

Images are saved in the './img/' directory with the timestamp as their name.
Note: Ensure that the camera module is enabled and correctly connected to the Raspberry Pi before running the script.
