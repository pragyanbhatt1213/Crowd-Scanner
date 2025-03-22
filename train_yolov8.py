from ultralytics import YOLO

def main():
    # Path to the dataset.yaml file
    dataset_yaml = "dataset/dataset.yaml"

    # Initialize YOLOv8 model
    model = YOLO("yolov8n.pt")  # Pretrained weights for YOLOv8 nano

    # Train the model
    model.train(
        data=dataset_yaml,     # Path to dataset.yaml
        epochs=50,             # Number of epochs
        imgsz=640,             # Image size (reduce to 512 or 416 if needed)
        batch=8,               # Batch size (reduce to 4 or 2 if memory issues occur)
        device=0               # Use GPU (device=0 for first GPU)
    )

    # Evaluate the model on the validation set
    metrics = model.val()
    print("Validation Metrics:", metrics)

    # Save the best model
    model.save("best_yolov8_custom.pt")

if __name__ == "__main__":
    main()
