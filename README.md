# 🧥 Invisible Cloak - Red

This project implements a **Harry Potter–style invisible cloak** effect using **OpenCV**.  
When you wear a red-colored cloth, the program detects it and replaces that region with the background, making it appear as if the cloth (cloak) is invisible.  

---

## 🎯 Activity
Detects a red cloak in the webcam feed and replaces it with the background to create an invisibility effect.  

---

## 🛠️ Input
- Live video feed from your webcam  
- A red-colored cloth/object (the cloak)  

---

## 🎥 Output
- A fullscreen video window where the red cloak is replaced by the captured background, making it look invisible.  

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/ravinduanjana99/Invicible-Cloak.git
2. Navigate into the project folder:
   cd Invicible-Cloak
3. Install the required dependencies:
   pip install opencv-python numpy
4. Run the script:
   python invisible_cloak.py