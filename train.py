import os, random, shutil
from ultralytics import YOLO

# Step 1️⃣: Define dataset paths
base_dir = r"C://Users//DELL//OneDrive//Desktop//AI RoadVision//baseFolder"
real_path = r"C://Users//DELL//OneDrive//Desktop//AI RoadVision//normal"
fake_path = r"C://Users//DELL//OneDrive//Desktop//AI RoadVision//potholes"

# Step 2️⃣: Create train/val folders
os.makedirs(f"{base_dir}/train/real", exist_ok=True)
os.makedirs(f"{base_dir}/train/fake", exist_ok=True)
os.makedirs(f"{base_dir}/val/real", exist_ok=True)
os.makedirs(f"{base_dir}/val/fake", exist_ok=True)

# Step 3️⃣: Split images into train/val sets (80/20)
for label, path in [('real', real_path), ('fake', fake_path)]:
    images = os.listdir(path)
    random.shuffle(images)
    split = int(0.8 * len(images))

    for i, img in enumerate(images):
        src = os.path.join(path, img)
        dst_folder = f"{base_dir}/train/{label}" if i < split else f"{base_dir}/val/{label}"
        shutil.copy(src, os.path.join(dst_folder, img))

print("✅ Dataset organized successfully!")

# Step 4️⃣: Train YOLOv8 classification model
model = YOLO('yolov8n-cls.pt')

results = model.train(
    data=base_dir,  # folder with 'train' and 'val' inside
    epochs=10,
    imgsz=224,
    batch=16
)
