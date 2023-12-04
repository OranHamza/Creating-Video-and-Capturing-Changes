import cv2
import numpy as np

def find_differences(video_path, threshold=1000000):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Read the first frame
    _, prev_frame = cap.read()

    # Create a list to store difference information
    differences = []

    # Loop through the video
    second = 0
    while True:
        # Read the next frame
        ret, frame = cap.read()

        # Break the loop when the end of the video is reached
        if not ret:
            break

        # Calculate the difference between two frames
        diff = cv2.absdiff(prev_frame, frame)

        # Calculate the total difference (sum of differences in color channels for color images)
        total_diff = np.sum(diff)

        # If the total difference exceeds the threshold, mark it as a difference
        if total_diff > threshold:
            differences.append(second)  # Add the time of difference in seconds

        # Set the current frame as the previous frame for the next iteration
        prev_frame = frame

        # Update the video time information
        second += 1 / cap.get(cv2.CAP_PROP_FPS)

    # Close the video file
    cap.release()

    return differences

# Find difference seconds in a different video
different_video_path = "C:/Users/Hamza Oran/Downloads/Carpal tunnel syndrome Ultrasound guided injection.mp4"
difference_seconds_different_video = find_differences(different_video_path)

# Print the found difference seconds for the different video
print(f"Difference seconds in the different video: {difference_seconds_different_video}")
