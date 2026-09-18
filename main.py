import cv2
import numpy as np

from hand_detector import HandDetector
from volume_controller import VolumeController


# -----------------------------
# Configuration
# -----------------------------

SMOOTHING = 0.2

MIN_DISTANCE = 30
MAX_DISTANCE = 200

smooth_volume = 0


# -----------------------------
# Initialize camera
# -----------------------------

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open webcam.")
    exit()


# -----------------------------
# Initialize components
# -----------------------------

detector = HandDetector()
volume_controller = VolumeController()


print("================================")
print("       VisionVolume Started")
print("================================")
print("Move thumb and index finger")
print("to control Windows volume.")
print("Press Q to exit.")


# -----------------------------
# Main loop
# -----------------------------

while True:

    success, frame = camera.read()

    if not success:
        print("Error: Could not read webcam frame.")
        break


    # Mirror webcam
    frame = cv2.flip(frame, 1)


    # Detect hand
    frame, results = detector.find_hands(frame)


    # --------------------------------
    # Hand detected
    # --------------------------------

    if results.multi_hand_landmarks:

        hand = results.multi_hand_landmarks[0]


        # Thumb tip
        thumb = hand.landmark[4]

        # Index finger tip
        index = hand.landmark[8]


        # Frame dimensions
        h, w, _ = frame.shape


        # Convert coordinates
        thumb_x = int(thumb.x * w)
        thumb_y = int(thumb.y * h)

        index_x = int(index.x * w)
        index_y = int(index.y * h)


        # --------------------------------
        # Draw fingertips
        # --------------------------------

        cv2.circle(
            frame,
            (thumb_x, thumb_y),
            12,
            (255, 0, 0),
            -1
        )

        cv2.circle(
            frame,
            (index_x, index_y),
            12,
            (255, 0, 0),
            -1
        )


        # Draw connecting line
        cv2.line(
            frame,
            (thumb_x, thumb_y),
            (index_x, index_y),
            (255, 0, 0),
            3
        )


        # --------------------------------
        # Calculate finger distance
        # --------------------------------

        distance = (
            (index_x - thumb_x) ** 2
            + (index_y - thumb_y) ** 2
        ) ** 0.5


        # --------------------------------
        # Convert distance to volume
        # --------------------------------

        volume = np.interp(
            distance,
            [MIN_DISTANCE, MAX_DISTANCE],
            [0, 100]
        )

        volume = int(np.clip(volume, 0, 100))


        # --------------------------------
        # Smooth volume
        # --------------------------------

        smooth_volume = (
            SMOOTHING * volume
            + (1 - SMOOTHING) * smooth_volume
        )

        smooth_volume = int(smooth_volume)


        # --------------------------------
        # Set Windows volume
        # --------------------------------

        volume_controller.set_volume(smooth_volume)


        # --------------------------------
        # Volume status
        # --------------------------------

        if smooth_volume < 30:
            status = "LOW"

        elif smooth_volume < 70:
            status = "MEDIUM"

        else:
            status = "HIGH"


        # --------------------------------
        # Title
        # --------------------------------

        cv2.putText(
            frame,
            "VisionVolume",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )


        # --------------------------------
        # Distance
        # --------------------------------

        cv2.putText(
            frame,
            f"Distance: {int(distance)} px",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2
        )


        # --------------------------------
        # Volume percentage
        # --------------------------------

        cv2.putText(
            frame,
            f"Volume: {smooth_volume}%",
            (20, 115),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )


        # --------------------------------
        # Status
        # --------------------------------

        cv2.putText(
            frame,
            f"Level: {status}",
            (20, 150),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )


        # --------------------------------
        # Volume bar
        # --------------------------------

        bar_x = 20
        bar_y = 175

        bar_width = 300
        bar_height = 30


        # Outer bar
        cv2.rectangle(
            frame,
            (bar_x, bar_y),
            (bar_x + bar_width, bar_y + bar_height),
            (255, 255, 255),
            2
        )


        # Filled bar
        filled_width = int(
            bar_width * smooth_volume / 100
        )


        cv2.rectangle(
            frame,
            (bar_x, bar_y),
            (bar_x + filled_width, bar_y + bar_height),
            (0, 255, 0),
            -1
        )


        # --------------------------------
        # Instructions
        # --------------------------------

        cv2.putText(
            frame,
            "Move fingers to control volume",
            (20, h - 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            "Press Q to exit",
            (20, h - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (200, 200, 200),
            1
        )


    # --------------------------------
    # No hand detected
    # --------------------------------

    else:

        cv2.putText(
            frame,
            "VisionVolume",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            "Show your hand",
            (20, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        cv2.putText(
            frame,
            "Use thumb and index finger",
            (20, 125),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )


    # --------------------------------
    # Display window
    # --------------------------------

    cv2.imshow(
        "VisionVolume - Hand Gesture Volume Controller",
        frame
    )


    # --------------------------------
    # Exit
    # --------------------------------

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# -----------------------------
# Cleanup
# -----------------------------

camera.release()
cv2.destroyAllWindows()

print("VisionVolume stopped.")