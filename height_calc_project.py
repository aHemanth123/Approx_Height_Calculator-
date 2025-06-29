import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def calculate_height_in_inches(landmarks, image_height):
    try:
        y_head = landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].y * image_height
        y_foot = landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].y * image_height
        pixel_height = abs(y_foot - y_head)
        height_inches = pixel_height / 6.5  # Adjust scaling factor as needed
        return round(height_inches, 2)
    except:
        return None

def inches_to_feet_and_inches(height_in_inches):
    feet = int(height_in_inches // 12)
    inches = int(height_in_inches % 12)
    return f"{feet} ft {inches} in"

def main():
    cap = cv2.VideoCapture(0)
    pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    window_name = 'Top-Down Height Estimation'
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        people_heights = []

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            h, w, _ = image.shape
            height = calculate_height_in_inches(landmarks, h)

            if height:
                feet_inches = inches_to_feet_and_inches(height)
                people_heights.append((height, landmarks[0].x * w, landmarks[0].y * h))

                cv2.putText(image, feet_inches, (int(landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].x * w),
                            int(landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].y * h) - 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        if len(people_heights) >= 2:
            people_heights.sort(key=lambda x: x[0], reverse=True)
            taller = people_heights[0]
            shorter = people_heights[1]

            cv2.putText(image, "Taller", (int(taller[1]), int(taller[2]) - 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            cv2.putText(image, "Shorter", (int(shorter[1]), int(shorter[2]) - 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        cv2.imshow(window_name, image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    pose.close()
    cap.release()
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()
