from ultralytics import YOLO
import cv2
import numpy as np
import winsound  # for buzzer sound 
import time

# Load your trained classification model
model = YOLO(r"C://Users//DELL//OneDrive//Desktop//AI RoadVision//runs//classify//train2//weights//best.pt")  # Update with your actual model path

# Open camera or video
cap = cv2.VideoCapture("C:\\Users\\DELL\\OneDrive\\Desktop\\AI RoadVision\\practicevideo.mp4")
pothole_alert_active = False  # flag to control buzzer

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Predict using YOLO model
    results = model.predict(frame)
    pred = results[0].probs.top1
    label = results[0].names[pred]
    conf = results[0].probs.top1conf.item()

    # Default color and text
    color = (0, 255, 0)
    text = f"ROAD NORMAL ({conf:.2f})"

    # If pothole detected (fake class)
    if label == "fake" and conf > 0.8:
        color = (0, 0, 255)
        text = "⚠ Danger!"
        
        # Red alert light
        cv2.circle(frame, (50, 50), 20, (0, 0, 255), -1)
        
        # Play buzzer only once per detection
        if not pothole_alert_active:
            pothole_alert_active = True
            print("Pothole detected! Buzzer ON!")
            winsound.Beep(1000, 600)  # 1000 Hz, 0.6 sec

    else:
        # Reset the alert when road becomes normal
        if pothole_alert_active:
            print("Road normal again.")
        pothole_alert_active = False

    # Display text
    cv2.putText(frame, text, (100, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

    # Show video
    cv2.imshow("Pothole Alert System", frame)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
