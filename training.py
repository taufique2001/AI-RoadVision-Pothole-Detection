import os
import cv2
import matplotlib.pyplot as plt

real_path = "C://Users//user//OneDrive//Desktop//AI RoadVision//normal"
fake_path = "C://Users//user//OneDrive//Desktop//AI RoadVision//potholes"

# Pick one image from each folder
real_img = cv2.imread(os.path.join(real_path, os.listdir(real_path)[0]))
fake_img = cv2.imread(os.path.join(fake_path, os.listdir(fake_path)[0]))

# Convert BGR → RGB for proper display
real_img = cv2.cvtColor(real_img, cv2.COLOR_BGR2RGB)
fake_img = cv2.cvtColor(fake_img, cv2.COLOR_BGR2RGB)

# Display both
plt.subplot(1, 2, 1)
plt.imshow(real_img)
plt.title("Real Face")

plt.subplot(1, 2, 2)
plt.imshow(fake_img)
plt.title("Fake Face")
plt.show()