from ultralytics import YOLO

# Load an official or custom model
# model = YOLO("yolov8n.pt")  # Load an official Detect model
# model = YOLO("yolov8n-seg.pt")  # Load an official Segment model
# model = YOLO("yolov8n-pose.pt")  # Load an official Pose model
model = YOLO("vehicle_kitti_v0_last.pt")  # Load a custom trained model

# Perform tracking with the model
# results = model.track("https://www.youtube.com/watch?v=xBwkNQ6ANeo", show=True)  # Tracking with default tracker
results = model.track("https://www.youtube.com/watch?v=xBwkNQ6ANeo", show=True, tracker="bytetrack.yaml")  # with ByteTrack