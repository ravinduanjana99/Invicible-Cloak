import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
time.sleep(2)

# Capture background
background = None
for i in range(60):
    ret, frame = cap.read()
    if ret:
        background = cv2.flip(frame, 1)

# ✅ Create full screen window
cv2.namedWindow("Invisible Cloak - Red", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Invisible Cloak - Red", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red cloak HSV ranges
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # Create masks
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    # Refine mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))

    mask_inv = cv2.bitwise_not(mask)

    # Replace cloak with background
    res1 = cv2.bitwise_and(background, background, mask=mask)
    res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    final = cv2.add(res1, res2)

    cv2.imshow("Invisible Cloak - Red", final)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
