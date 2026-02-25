# Vehic-Vision

An AI-powered automated vehicle inspection system designed for the insurance and car rental industries. **Vehi-Vision** leverages computer vision to detect, segment, and explain exterior vehicle damage through a transparent scoring system.

## Overview
The goal of this graduation project is to create a seamless inspection pipeline that:
1. Detects exterior damages (dents, scratches, broken lights, etc.) using YOLO.
2. Segments specific car parts to provide localized context for the damage.
3. Utilizes XAI (Grad-CAM) to generate heatmaps, explaining the model's decision-making.
4. Generates a severity report and damage score based on visual findings.

*Note: This project is strictly for exterior assessment; it does not cover internal mechanics or cabin interiors.*

## Tech Stack
**Development:**
* **Language:** Python 3.11.x (Specifically to avoid compatibility issues)
* **Detection & Segmentation:** YOLO (v8/v11) and YOLO-Seg
* **Explainable AI:** Grad-CAM (PyTorch-based)
* **Libraries:** OpenCV, Pillow, NumPy, Matplotlib  

**Deployment**
* **UI Framework:** Streamlit (For the functional application interface)

## ⚙️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AbdullahGhulam/Vehi-Vision
   cd Vehi-Vision
    ```
    Create a Virtual Environment:

    ```bash
    # This creates a new environment (run it only ONCE)
    python -m venv venv
    ```

    After that, activate the environment using:
    ```bash
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate   # Windows
    ```

2. **Install Dependencies:**
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
3.  **Verify Installation:**  
After installing the requirements, run the following script to ensure your environment (Python, PyTorch, and GPU) is configured correctly:
    ```bash
    python check_setup.py
    ```


📂 **Project Structure**
```text
Vehi-Vision
├── data/               # Local datasets (Ignored by Git)
├── venv/               # Python Environment (Ignored by Git)
├── weights/            # Saved model weights (.pt or .onnx)
├── notebooks/          # Research, EDA, and prototyping
├── src/                # Source code (Detection, Segmentation, XAI)
├── .gitignore          # Files to exclude from Git
└── README.md
```

👥  **Team & Credits**

    Abdullah Ghulam – GitHub | LinkedIn

    Elyas Yar – GitHub | LinkedIn

    Azzam Abdullah – GitHub | LinkedIn

    [Member Name] – GitHub | LinkedIn
