<div align="center">
    
[![PyPI version](https://img.shields.io/pypi/v/gTTS.svg)](https://pypi.org/project/gTTS/)
[![PyPI - Python Version](https://img.shields.io/badge/Python-%3E%3D%203.9-blue)](https://www.python.org/)
    
</div>


https://github.com/leo007-htun/Cursor_Control_by_Hand_Landmark_Detection/assets/66962471/aa34c361-8dd9-4072-bab6-ed9bb4c1dcf8

## Hand Landmark Detection with pre-trained model from Mediapipe

``mediapipe`` the MediaPipe Hands module from the MediaPipe library to detect and track hand landmarks in real-time from webcam feed. The specific model used is a pre-trained model provided by MediaPipe for hand tracking.

    model_complexity=0: 
    min_detection_confidence=0.5: 
    min_tracking_confidence=0.5: 
    
This first parameter controls the complexity of the hand tracking model. A value of 0 indicates the simplest model.This 2nd parameter sets the minimum confidence threshold for a hand detection to be considered valid. The 3rd parameter sets the minimum confidence threshold for hand landmarks to be considered during tracking.

    cv2.VideoCapture(2)

The number inside parentheses is the available webcams from the user's device.
If there are multiple webcams, try the following to check the webcam indeces

    $ sudo apt-get install v4l-utils
    $ v4l2-ctl --list-devices

It will show as follows:

    HD720P Webcam: HD720P Webcam (usb-0000:06:00.3-2):
	/dev/video2
	/dev/video3
	/dev/media1

    USB2.0 HD UVC WebCam: USB2.0 HD (usb-0000:06:00.3-4):
    	/dev/video0
    	/dev/video1
    	/dev/media0

## Instructions

<img width="1073" alt="hand-landmarks" src="https://github.com/leo007-htun/Cursor_Control_by_Hand_Landmark_Detection/assets/66962471/b420286c-adc0-4efc-8b88-3b52fb3d71db">


There are two functions such as ``.click()`` and ``.press()`` from ``pyautogui``. For first function, the distance between ``thumb`` and ``index`` fingers tips are measured and once the two tips meet each other, it clicks. 
For ``.press()``, keyword ``f`` is passed into that function ``.press('f')`` to exit or enter full-screen mode. The closer the tip of ``thumb`` and ``middle`` finger gets, ``press`` initiates. In the image above, ``ID`` of finger joints can be found. 

> [!TIP]
> FPS and Image Resolutions are always inversely propotional, one must choose FPS over Resolution or Resolution over FPS

In this repo, resolution is set to minimal, since FPS is the priority while moving cursor around. As Futureworks, calibration techniques must be considered.

Check you webcam's resolution and fps as follows:

	$ v4l2-ctl --list-formats-ext
 
 It will show as follows:
 
 ioctl: VIDIOC_ENUM_FMT
	Type: Video Capture

	[0]: 'MJPG' (Motion-JPEG, compressed)
		Size: Discrete 1280x720
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 800x600
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 640x480
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 352x288
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 320x240
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 176x144
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 160x120
			Interval: Discrete 0.033s (30.000 fps)
	[1]: 'YUYV' (YUYV 4:2:2)
		Size: Discrete 640x480
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 1280x720
			Interval: Discrete 0.100s (10.000 fps)
		Size: Discrete 800x600
			Interval: Discrete 0.050s (20.000 fps)
		Size: Discrete 352x288
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 320x240
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 176x144
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 160x120
			Interval: Discrete 0.033s (30.000 fps)


## Installation

    $ git clone https://github.com/leo007-htun/Cursor_Control_by_Hand_Landmark_Detection.git
    

    $ pip install -r requirements.txt

## RUN
    $ source best.sh 



    
