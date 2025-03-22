from ultralytics import YOLO
import cv2
import numpy as np

def process_image(image_path, model_path):
    # Load your trained model
    model = YOLO(model_path)
    
    # Read the image
    img = cv2.imread(image_path)
    
    # Run inference
    results = model(img)
    
    # Process results
    for r in results:
        boxes = r.boxes
        for i, box in enumerate(boxes, start=1):  # enumerate with start=1 for counting from 1
            # Get box coordinates
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            
            # Draw box with increased thickness
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 4)  # Thickness = 4
            
            # Add number label with larger font size and bold effect
            label = str(i)
            cv2.putText(img, label, (x1, y1-15), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)  # Font size = 1.2, Thickness = 3
    
    # Add total count on top of image with larger font size and bold effect
    total_count = len(boxes)
    cv2.putText(img, f'Total Count: {total_count}', (10, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)  # Font size = 1.5, Thickness = 4
    
    return img, total_count

def process_video(video_path, model_path):
    # Load your trained model
    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_path)
    
    # Get video properties for output
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # Create video writer
    output_path = 'output_video.mp4'
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
            
        # Run inference
        results = model(frame)
        
        # Process results
        for r in results:
            boxes = r.boxes
            for i, box in enumerate(boxes, start=1):
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                
                # Draw box with increased thickness
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 4)  # Thickness = 4
                
                # Add number label with larger font size and bold effect
                label = str(i)
                cv2.putText(frame, label, (x1, y1-15), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)  # Font size = 1.2, Thickness = 3
        
        # Add total count with larger font size and bold effect
        total_count = len(boxes)
        cv2.putText(frame, f'Total Count: {total_count}', (10, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)  # Font size = 1.5, Thickness = 4
        
        # Write frame
        out.write(frame)
        
        # Display frame (optional)
        cv2.imshow('Crowd Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Example usage:
def main():
    # Path to your trained model
    model_path = '../Crowd Scanner/runs/detect/train/weights/best.pt'
    
    # For image
    image_path = '../Crowd Scanner/1.jpg'
    output_img, count = process_image(image_path, model_path)
    cv2.imwrite('output_image.jpg', output_img)
    print(f'People counted in image: {count}')
    
    # For video
    video_path = '../Crowd Scanner/2.mp4'
    process_video(video_path, model_path)

if __name__ == '__main__':
    main()
