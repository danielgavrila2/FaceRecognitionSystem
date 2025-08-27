# 🤖 FaceRecognitionSystem

A Python application that detects and recognizes multiple faces in real-time, assigning each to a known individual.  
Utilizes OpenCV and Haar cascades for face detection, and records attendance data in CSV format.

---

## ✨ Features

- 👥 **Multi-Face Detection**  
  Simultaneously detects and recognizes multiple faces in a single frame.

- 🧠 **Real-Time Recognition**  
  Matches detected faces against a pre-trained dataset of known individuals.

- 🗂️ **Attendance Logging**  
  Automatically records recognized faces along with timestamps in a CSV file.

- 🖼️ **Media Support**  
  Processes both live video streams and static images.

---

## 🛠️ Installation

### Prerequisites

- Python 3.6+
- OpenCV
- NumPy

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/danielgavrila2/FaceRecognitionSystem.git
   cd FaceRecognitionSystem
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Prepare your dataset:

   - Place images of known individuals in the `data` directory.
   - Ensure each image is named after the individual (e.g., `john_doe.jpg`).

---

## 🚀 Usage

### Adding Faces to Dataset

To add new faces to the dataset:

```bash
python add_faces.py
```

Follow the on-screen instructions to capture images of the new individual.

### Running the Recognition System

To start the face recognition system:

```bash
python app.py
```

The application will open a window displaying the live video feed with detected and recognized faces.

---

## 📂 Project Structure

```
FaceRecognitionSystem/
│── app.py                 # Main application script
│── add_faces.py           # Script to add new faces to dataset
│── test.py                # Testing script
│── data/                  # Directory containing known face images
│── Media/                 # Directory for media files
│── Attendance/            # Directory for attendance logs
│── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 📈 Attendance Data

All recognized faces are logged in the `Attendance` directory as CSV files. Each entry includes:

- Name of the recognized individual
- Timestamp of recognition

---

## 🔧 Roadmap

- [ ] Enhance recognition accuracy with deep learning models
- [ ] Implement real-time attendance dashboard
- [ ] Add support for video file input
- [ ] Improve user interface for adding new faces

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your proposed changes.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📞 Contact

For questions or feedback, please open an issue on the [GitHub repository](https://github.com/danielgavrila2/FaceRecognitionSystem).
