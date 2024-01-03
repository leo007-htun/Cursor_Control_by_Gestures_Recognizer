<div align="center">
    
[![PyPI version](https://img.shields.io/pypi/v/gTTS.svg)](https://pypi.org/project/gTTS/)
[![PyPI - Python Version](https://img.shields.io/badge/Python-%3E%3D%203.9-blue)](https://www.python.org/)
    
</div>


## Hand Landmark Detection with pre-trained model from Mediapipe

``mediapipe`` the MediaPipe Hands module from the MediaPipe library to detect and track hand landmarks in real-time from webcam feed. The specific model used is a pre-trained model provided by MediaPipe for hand tracking.

    model_complexity=0: 
    min_detection_confidence=0.5: 
    min_tracking_confidence=0.5: 
    
This first parameter controls the complexity of the hand tracking model. A value of 0 indicates the simplest model.This 2nd parameter sets the minimum confidence threshold for a hand detection to be considered valid. The 3rd parameter sets the minimum confidence threshold for hand landmarks to be considered during tracking.

    cv2.VideoCapture(2)

The number inside parentheses is the available webcams from the user's device.
If there are multiple webcams, try the following to check the webcam indeces

    $sudo apt-get install v4l-utils
    $v4l2-ctl --list-devices

It will show as follows:

    HD720P Webcam: HD720P Webcam (usb-0000:06:00.3-2):
	/dev/video2
	/dev/video3
	/dev/media1

    USB2.0 HD UVC WebCam: USB2.0 HD (usb-0000:06:00.3-4):
    	/dev/video0
    	/dev/video1
    	/dev/media0




## Installation

    $ git clone https://github.com/leo007-htun/Cursor_Control_by_Hand_Landmark_Detection.git
    

    $ pip install -r requirements.txt

## RUN
    $ source best.sh 



    
