# 🌿 Plant Disease Detector

![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.19.0-orange)
![Accuracy](https://img.shields.io/badge/Accuracy-97.37%25-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

> An AI-powered plant disease detection system using deep learning to help farmers identify crop diseases early and reduce yield losses.

## 🌐 Live Demo
👉 [Try the App on Hugging Face Spaces](https://huggingface.co/spaces/sam-imt296/farm_disease)
👉 [GitHub Repository](https://github.com/Samad296/Plant_disease_detection)

---

## 📌 Table of Contents
- [Problem Statement](#-problem-statement)
- [Our Solution](#-our-solution)
- [Model Performance](#-model-performance)
- [Supported Plants](#-supported-plants)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Tech Stack](#-tech-stack)
- [License](#-license)

---

## ❗ Problem Statement

Plant diseases significantly impact crop yields worldwide, causing major economic
losses for farmers.

### Key Challenges:
- 🔍 Manual inspection is slow and error-prone
- 👨‍🌾 Expert agronomists are scarce in rural areas
- 🦠 Disease symptoms look visually similar across species
- 📉 Up to **40% yield loss** without timely intervention
- 🌾 Common crops like tomatoes, potatoes, and apples suffer from
  fungal, bacterial, and viral infections
- 💸 Smallholder farmers lack access to affordable diagnostic tools

---

## ✅ Our Solution

We developed an **AI-powered plant disease detection system** that:

- 📸 Takes a **leaf image as input**
- 🧠 Uses **EfficientNetB0** deep learning model to analyze it
- 🦠 Identifies the **disease name** with confidence score
- 🌱 Covers **38 disease categories** across 14 plant species
- ⚡ Provides **instant results** via a simple web interface
- 🌐 Accessible to anyone via **Hugging Face Spaces** — no installation needed

### How It Solves The Problem:

| Problem | Our Solution |
|---------|-------------|
| Manual inspection too slow | ✅ Instant AI prediction |
| Expert shortage in rural areas | ✅ Available online 24/7 |
| Similar-looking symptoms | ✅ 97.37% accurate model |
| Expensive diagnostic tools | ✅ 100% free to use |
| Yield loss from late detection | ✅ Early detection system |

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Architecture | EfficientNetB0 |
| Dataset | PlantVillage |
| Total Training Images | 54,305 |
| Number of Classes | 38 |
| Validation Accuracy | **98.17%** |
| Test Accuracy | **97.37%** |
| Model Size | ~31 MB |

### Performance vs Other Models:

| Model | Accuracy |
|-------|---------|
| Basic CNN | ~85% |
| ResNet50 | ~95% |
| **Our EfficientNetB0** | **97.37%** ✅ |
| State of the Art | ~99% |

---

## 🌿 Supported Plants & Diseases

| Plant | Diseases Detected |
|-------|------------------|
| 🍎 Apple | Scab, Black Rot, Cedar Rust, Healthy |
| 🫐 Blueberry | Healthy |
| 🍒 Cherry | Powdery Mildew, Healthy |
| 🌽 Corn | Gray Leaf Spot, Common Rust, Blight, Healthy |
| 🍇 Grape | Black Rot, Esca, Leaf Blight, Healthy |
| 🍊 Orange | Citrus Greening |
| 🍑 Peach | Bacterial Spot, Healthy |
| 🫑 Pepper | Bacterial Spot, Healthy |
| 🥔 Potato | Early Blight, Late Blight, Healthy |
| 🍓 Strawberry | Leaf Scorch, Healthy |
| 🍅 Tomato | Bacterial Spot, Early Blight, Late Blight, Leaf Mold, and more |
| + More | Raspberry, Soybean, Squash |

---

## 📁 Project Structure
```
Plant_disease_detect/
├── app.py                        # Streamlit web application
├── requirements.txt              # Python dependencies
├── class_names.txt               # 38 disease class labels
├── plant_disease_model.tflite    # Optimized TFLite model
└── README.md                     # Project documentation
```

---

## 🛠️ Installation & Run Locally

### Prerequisites
- Python 3.10
- Anaconda (recommended)

### 1. Clone Repository
```bash
git clone https://github.com/Samad296/Plant_disease_detection.git
cd Plant_disease_detect
```

### 2. Create Environment
```bash
conda create -n plant_app python=3.10 -y
conda activate plant_app
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run App
```bash
streamlit run app.py
```

### 5. Open Browser
```
http://localhost:8501
```

---

## 💻 Usage

1. 📤 **Upload** a plant leaf image (JPG, JPEG, PNG)
2. 🔄 **Wait** for the AI to analyze the image
3. ✅ **View** the predicted disease with confidence score
4. 📊 **Check** top 3 predictions for reference

---

## 🧠 Model Architecture
```
Input (224 × 224 × 3)
        ↓
EfficientNetB0 (ImageNet pretrained)
  └── Last 20 layers trainable
  └── BatchNorm layers frozen
        ↓
GlobalAveragePooling2D
        ↓
Dense(256, ReLU)
        ↓
Dropout(0.3)
        ↓
Dense(38, Softmax)
        ↓
Output (38 disease classes)
```

---

## ⚙️ Training Details

| Parameter | Value |
|-----------|-------|
| Optimizer | Adam |
| Learning Rate | 0.001 |
| Batch Size | 32 |
| Epochs | 10 |
| Image Size | 224 × 224 |
| Augmentation | Rotation, Zoom, Flip, Shift |
| Class Weights | Balanced (handles imbalance) |
| Fine-tuned Layers | Last 20 of EfficientNetB0 |
| GPU | NVIDIA T4 (Google Colab) |

---

## 🧰 Tech Stack

| Category | Technology |
|----------|-----------|
| Deep Learning | TensorFlow 2.19, Keras |
| Model | EfficientNetB0 |
| Dataset | PlantVillage (Kaggle) |
| Web App | Streamlit |
| Deployment | Hugging Face Spaces |
| Language | Python 3.10 |
| Version Control | Git & GitHub |

---

## 📈 Future Improvements

- [ ] Add more plant species
- [ ] Mobile app (Android/iOS)
- [ ] Real-time camera detection
- [ ] Treatment recommendations
- [ ] Multi-language support (Urdu)
- [ ] Offline mode for rural areas

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

## 📜 License

This project is licensed under the **MIT License** — free to use and modify.

---

## 👨‍💻 Author

**Abdul Samad Imtiaz**
- 🐙 GitHub: [@Samad296](https://github.com/Samad296)
- 🤗 Hugging Face: [@sam-imt296](https://huggingface.co/sam-imt296)

---

## 🙏 Acknowledgements

- [PlantVillage Dataset](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset)
- [EfficientNet Paper](https://arxiv.org/abs/1905.11946)
- [TensorFlow](https://tensorflow.org)
- [Streamlit](https://streamlit.io)

---

⭐ **Star this repo if you found it helpful!**
