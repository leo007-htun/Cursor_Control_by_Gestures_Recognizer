from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import pyautogui
import time

MARGIN = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54)  # vibrant green
screen_width, screen_height = pyautogui.size()
print(screen_height,screen_width)
x1 = y1 = x2 = y2 = 0

def draw_landmarks_on_image(rgb_image, detection_result):
    hand_landmarks_list = detection_result.hand_landmarks
    handedness_list = detection_result.handedness
    annotated_image = np.copy(rgb_image)

    # Loop through the detected hands to visualize.
    for idx in range(len(hand_landmarks_list)):
        hand_landmarks = hand_landmarks_list[idx]
        handedness = handedness_list[idx]

        # Draw the hand landmarks.
        hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        hand_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks])
        solutions.drawing_utils.draw_landmarks(
            annotated_image,
            hand_landmarks_proto,
            solutions.hands.HAND_CONNECTIONS,
            solutions.drawing_styles.get_default_hand_landmarks_style(),
            solutions.drawing_styles.get_default_hand_connections_style())

        # Get the top left corner of the detected hand's bounding box.
        height, width, _ = annotated_image.shape
        for id, landmark in enumerate(hand_landmarks):
            text_x = int(landmark.x * width)
            text_y = int(landmark.y * height)
            #print(text_x,text_y)
            if id == 4:  # thumb
                mouse_x = int(screen_width / width * text_x)
                mouse_y = int(screen_height / height * text_y)
                cv2.circle(annotated_image, (text_x, text_y), 10, (0, 255, 255))
                pyautogui.moveTo(mouse_x,mouse_y)
                x2 = text_x
                y2 = text_y


            if id == 8:  # pointy finger
                x1 = text_x
                y1 = text_y
                cv2.circle(annotated_image, (text_x, text_y), 10, (0, 255, 255))
                
        dist = y2 -y1
        print(dist)
        if (dist<30):
            pyautogui.click()
        # Draw handedness (left or right hand) on the image.
        cv2.putText(annotated_image, f"{handedness[0].category_name}",
                    (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX,
                    FONT_SIZE, HANDEDNESS_TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA)

    return annotated_image

base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)
camera = cv2.VideoCapture(2)
while True:
    _, image = camera.read()
     # Resize the image frames 
    resize = cv2.resize(image, (320, 240)) 
    image = cv2.flip(resize, 1)
    image_height, image_width, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert to NumPy array
    np_image = np.array(rgb_image)

    # Create mp.Image
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np_image)
    detection_result = detector.detect(mp_image)
    annotated_image = draw_landmarks_on_image(rgb_image, detection_result)

    cv2.imshow("Hand movement video capture", cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))
    key = cv2.waitKey(1)
    if key == 27:
        break

camera.release()
cv2.destroyAllWindows()
