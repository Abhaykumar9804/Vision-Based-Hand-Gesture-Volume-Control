<p align="center">
  <img src="assets/Banner.png" alt="VisionVolume Banner" width="100%">
</p>

# VisionVolume 

## Hand Gesture Based Computer Volume Controller

VisionVolume is a real-time computer vision application that allows users to control the Windows system volume using hand gestures.

The application uses a webcam to detect the user's hand and tracks the tips of the thumb and index finger. The distance between these two fingertips is converted into a volume percentage and applied directly to the Windows system volume.

This provides a simple touch-free way to control audio using natural hand movements.

---

## Features

- Real-time hand detection using a webcam
- Tracks thumb and index finger landmarks
- Calculates the distance between fingertips
- Converts finger distance into volume percentage
- Controls Windows system volume in real time
- Smooth volume adjustment
- Real-time volume percentage display
- Visual volume progress bar
- Displays current finger distance
- Displays volume level as LOW, MEDIUM, or HIGH
- Simple keyboard control for exiting the application

---

## How It Works

The project follows this process:

Webcam
↓
Hand Detection
↓
Thumb and Index Finger Detection
↓
Calculate Finger Distance
↓
Convert Distance to Volume Percentage
↓
Smooth Volume Value
↓
Set Windows System Volume

### Detailed Process

1. The webcam captures the user's hand.
2. MediaPipe detects the hand and its landmarks.
3. Landmark 4 is used to identify the thumb tip.
4. Landmark 8 is used to identify the index finger tip.
5. The pixel coordinates of both fingertips are calculated.
6. The distance between the two fingertips is calculated.
7. The distance is mapped to a value between 0% and 100%.
8. A smoothing algorithm reduces sudden volume fluctuations.
9. PyCaw applies the calculated value to the Windows master volume.
10. OpenCV displays the hand landmarks, distance, and volume information.

---

## Technologies Used

- Python 3.12
- OpenCV
- MediaPipe
- NumPy
- PyCaw
- Comtypes

---

## Requirements

Before installing the project, make sure you have:

- Windows 10 or later
- Python 3.12
- A working webcam
- Speakers or headphones
- Git

---

## Project Structure

```text
VisionVolume/
├── src/
│   ├── main.py
│   ├── hand_detector.py
│   └── volume_controller.py
├── assets/
├── output/
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Installation

### 1. Clone the Repository

Open PowerShell or Command Prompt and run:

git clone https://github.com/ibadarsh0/VisionVolume.git

Then move into the project directory:

cd VisionVolume


### 2. Create a Virtual Environment

Create a Python 3.12 virtual environment:

py -3.12 -m venv .venv

### 3. Activate the Virtual Environment

For Windows PowerShell:

.\.venv\Scripts\Activate.ps1

After activation, the terminal should show something similar to:

(.venv) PS C:\...\VisionVolume>

### 4. Install Dependencies

Install all required packages:

python -m pip install -r requirements.txt

The required dependencies are:

opencv-python
mediapipe==0.10.21
numpy
pycaw
comtypes

---

## Running the Application

Make sure the virtual environment is activated.

From the project root directory, run:

python src\main.py

The webcam window will open.

Place your hand in front of the camera and move your thumb and index finger closer or farther apart.

- Fingers close together → Lower volume
- Fingers farther apart → Higher volume

Press Q to exit the application.

---

## How to Use

### 🔊 Increase Volume
Move your **thumb and index finger farther apart**.

```text
Thumb ●────────● Index
          ↑
     Larger Distance
          ↓
     Higher Volume
```

### 🔉 Decrease Volume
Move your **thumb and index finger closer together**.

```text
Thumb ●──● Index
        ↑
  Smaller Distance
        ↓
   Lower Volume
```

### 🚪 Exit
Press **`Q`** to close the application and release the webcam.

> 💡 **Tip:** Keep your hand clearly visible to the webcam and use smooth finger movements for better volume control.

---

## Volume Mapping

The application maps the distance between the thumb and index finger to a volume percentage.

Current mapping:

30 px   →   0% volume

75 px   →   approximately 26% volume

100 px  →   approximately 41% volume

150 px  →   approximately 70% volume

200 px  →   100% volume

Distances below the minimum are treated as 0% volume, while distances above the maximum are treated as 100%.

---

## Smoothing

Small movements of the hand can cause the detected distance to change rapidly.

To make the volume control more stable, VisionVolume applies a smoothing factor to the calculated volume.

The current smoothing factor is:

SMOOTHING = 0.2

A smaller value results in smoother but slower volume changes.

A larger value results in faster but potentially less stable changes.

---

## Configuration

The main configuration values can be changed in:

src/main.py

### Smoothing

SMOOTHING = 0.2

### Minimum Distance

MIN_DISTANCE = 30

This represents approximately 0% volume.

### Maximum Distance

MAX_DISTANCE = 200

This represents approximately 100% volume.

These values can be adjusted depending on the user's preferred hand position and webcam setup.

---

## Troubleshooting

### 1. Webcam Does Not Open

If the webcam does not open:

- Check that the webcam is connected.
- Make sure another application is not using the webcam.
- Check Windows camera permissions.
- Restart the application.

The application will display:

Error: Could not open webcam.

if the camera cannot be accessed.

### 2. Hand Is Not Detected

Try the following:

- Improve the lighting.
- Keep your entire hand inside the camera frame.
- Move your hand closer to the webcam.
- Avoid covering your fingertips.
- Use a simple background if possible.

### 3. MediaPipe Error

This project uses:

mediapipe==0.10.21

If MediaPipe is installed incorrectly, run:

python -m pip uninstall mediapipe -y

Then:

python -m pip install mediapipe==0.10.21

You can verify the installed version with:

python -c "import mediapipe as mp; print(mp.__version__)"

The expected output is:

0.10.21

### 4. PowerShell Virtual Environment Error

If PowerShell prevents virtual environment activation, run:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Then activate the environment again:

.\.venv\Scripts\Activate.ps1

### 5. PyCaw Error

Make sure the required packages are installed:

python -m pip install pycaw comtypes

The application is designed for Windows because PyCaw is used to control the Windows audio endpoint.

### 6. Volume Changes Too Quickly

If the volume reacts too quickly or feels unstable, decrease:

SMOOTHING = 0.2

For example:

SMOOTHING = 0.1

If the volume responds too slowly, increase the value:

SMOOTHING = 0.3

---

## Limitations

The current version has some limitations:

- It is designed for Windows.
- It requires a webcam.
- Hand detection can be affected by poor lighting.
- The volume mapping depends on the distance of the hand from the camera.
- Only one hand is used for volume control.
- The application controls the system master volume rather than individual application volumes.
- Very rapid hand movements can still cause small fluctuations.

---

## Future Improvements

Possible future improvements include:

- Multi-hand gesture support
- Gesture-based mute/unmute
- Play/pause media control
- Previous/next track controls
- Custom gesture recognition
- User-configurable volume ranges
- Improved adaptive smoothing
- Support for additional operating systems
- Graphical configuration interface
- Application-specific volume control
- Gesture-based brightness control

---

## Advantages

- Touch-free volume control
- Simple and intuitive gesture
- No additional hardware required
- Real-time response
- Lightweight implementation
- Easy to understand computer vision pipeline
- Can be extended to other gesture-based controls

---

## Use Cases

VisionVolume can be useful in situations where physical interaction with a computer is inconvenient.

Example use cases include:

- Controlling music while working
- Adjusting volume during presentations
- Touch-free media control
- Accessibility-oriented interfaces
- Human-computer interaction experiments
- Computer vision demonstrations
- Educational projects

---

## Security and Privacy

VisionVolume processes the webcam feed locally for hand detection.

The application does not require uploading webcam frames to a remote server for volume control.

The webcam is used only while the application is running.

---

## License

This project is licensed under the MIT License.

See the LICENSE file for more information.

---

## Author

Abhay Kumar

VisionVolume was developed as a computer vision project demonstrating real-time hand tracking and gesture-based system control.
