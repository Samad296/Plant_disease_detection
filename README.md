# 🌿 Plant Disease Detector

A deep learning web application that detects plant diseases from leaf images 
using EfficientNetB0 trained on the PlantVillage dataset.

## 🚀 Live Demo
[Click here to try the app](https://huggingface.co/spaces/YOUR_USERNAME/plant-disease-detector)

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Architecture | EfficientNetB0 |
| Dataset | PlantVillage |
| Total Images | 54,305 |
| Classes | 38 |
| Validation Accuracy | 98.17% |
| Test Accuracy | 97.37% |

---

## 🌿 Supported Plants & Diseases

| Plant | Diseases |
|-------|---------|
| Apple | Scab, Black Rot, Cedar Rust, Healthy |
| Corn | Gray Leaf Spot, Common Rust, Blight, Healthy |
| Grape | Black Rot, Esca, Leaf Blight, Healthy |
| Potato | Early Blight, Late Blight, Healthy |
| Tomato | Bacterial Spot, Early Blight, Late Blight, Leaf Mold, and more |
| + 9 more plants | ... |

---

## 🛠️ Installation & Run Locally

### 1. Clone repo
```bash
git clone https://github.com/YOUR_USERNAME/plant-disease-app.git
cd plant-disease-app
```

### 2. Create environment
```bash
conda create -n plant_app python=3.10 -y
conda activate plant_app
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run app
```bash
streamlit run app.py
```

### 5. Open browser
```
http://localhost:8501
```

---

## 📁 Project Structure
```
plant-disease-app/
├── app.py                  # Streamlit web app
├── requirements.txt        # Dependencies
├── class_names.txt         # 38 class labels
├── best_model.keras        # Trained EfficientNetB0 model
└── README.md               # Project documentation
```

---

## 🧠 Model Architecture
```
Input (224x224x3)
    ↓
EfficientNetB0 (pretrained ImageNet)
    ↓
GlobalAveragePooling2D
    ↓
Dense(256, relu)
    ↓
Dropout(0.3)
    ↓
Dense(38, softmax)
```

---

## ⚙️ Training Details

| Parameter | Value |
|-----------|-------|
| Optimizer | Adam |
| Learning Rate | 0.001 |
| Batch Size | 32 |
| Epochs | 10 |
| Image Size | 224x224 |
| Augmentation | Rotation, Zoom, Flip, Shift |
| Class Weights | Balanced |
| Fine-tuned Layers | Last 20 |

---

## 📦 Dependencies
```txt
streamlit==1.32.0
tensorflow==2.19.0
keras==3.10.0
numpy
Pillow
```

---

## 🖼️ Screenshots

> Upload leaf image → instant disease detection

![App Screenshot](screenshot.png)

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.

---

## 📜 License
MIT License

---

## 👨‍💻 Author
**YOUR NAME**
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)

---

⭐ Star this repo if you found it helpful!
```

---

## How to Add Topics on GitHub
```
Your Repo Page
→ Click ⚙️ gear icon next to "About"
→ Add description (short one)
→ Add topics/tags
→ Save ✅
