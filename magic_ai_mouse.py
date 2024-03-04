import cv2
import mediapipe as mp

# capture video from camera
cap = cv2.VideoCapture(1)
# add hand detection
mp_hands = mp.solutions.hands.Hands()
# add drawing utilities
mp_drawing = mp.solutions.drawing_utils


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = mp_hands.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            mp_drawing.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                print(x, y)
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(255, 255, 51), thickness=-1)
                

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break