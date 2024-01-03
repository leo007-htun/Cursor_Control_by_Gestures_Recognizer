import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
import pyautogui

screen_width, screen_height = pyautogui.size()

cap = cv2.VideoCapture(2)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    resize = cv2.resize(image, (240, 240)) 
    image = cv2.flip(resize,1)
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

            # Get the top left corner of the detected hand's bounding box.
            height, width, _ = image.shape
            for id, landmark in enumerate(hand_landmarks.landmark):
                text_x = int(landmark.x * width)
                text_y = int(landmark.y * height)

                # Rest of your code for processing hand landmarks
                # ...

                if id == 4:  # thumb
                    mouse_x = int(screen_width / width * text_x)
                    mouse_y = int(screen_height / height * text_y)
                    cv2.circle(image, (text_x, text_y), 10, (0, 255, 255))
                    pyautogui.moveTo(mouse_x, mouse_y)
                    x2 = text_x
                    y2 = text_y

                if id == 8:  # pointy finger
                    x1 = text_x
                    y1 = text_y
                    cv2.circle(image, (text_x, text_y), 10, (0, 255, 255))

                if id == 16:  # pointy finger
                    x3 = text_x
                    y3 = text_y
                    cv2.circle(image, (text_x, text_y), 10, (0, 255, 255))
        dist = y2 -y1
        print("click : ",dist)
        dist_ = y3 - y1
        print("esc : ",dist_)
        if (dist<30):
            pyautogui.click()
        if (dist_>5):
           pyautogui.press('f')



    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()