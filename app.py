import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import model_from_json
from tensorflow.keras.applications.efficientnet import preprocess_input
# ── Page Config ───────────────────────────────────────────
st.set_page_config(
    page_title=" Plant Disease Detector",
    page_icon="🌿",
    layout="wide"
)
# ── Load Model ───────────────────────────────────────────
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('plant_disease.keras')
    
    return model

# Initialize the model
model = load_model()
@st.cache_resource
def load_labels():
    with open('class_names.txt', 'r') as f:
        labels = f.read().splitlines()
    return labels
model = load_model()
class_names = load_labels()
# ── App Title ───────────────────────────────────────────
st.title("🌿 Plant Disease Detector")
st.markdown("##### Powered by EfficientNetB0 | 38 Classes | 97%+ Accuracy")
st.markdown("---")
# ── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.header("ℹ️ About")
    st.info("""
    This app detects plant diseases from leaf images.
    - 🌱 38 plant disease classes
    - 🧠 EfficientNetB0 model
    - 📊 97%+ accuracy
    - 🗃️ Trained on PlantVillage dataset
    """)
    st.header("🌿 Supported Plants")
    plants = list(set([c.split('___')[0].replace('_', ' ')
                       for c in class_names]))
    for p in sorted(plants):
        st.markdown(f"- {p}")
# ── Main UI ───────────────────────────────────────────────
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📤 Upload Leaf Image")
    uploaded_file = st.file_uploader(
        "Choose a plant leaf image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        img = Image.open(uploaded_file).convert('RGB')
        st.image(img, caption="Uploaded Image", use_column_width=True)
with col2:
    st.subheader("🔍 Prediction Results")

    if uploaded_file:
        with st.spinner("🔄 Analyzing image..."):

            # Preprocess
            img_resized = img.resize((224, 224))
            img_array   = np.array(img_resized, dtype=np.float32)
            img_array   = np.expand_dims(img_array, axis=0)
            img_array   = preprocess_input(img_array)
             # Predict
            predictions    = model.predict(img_array, verbose=0)
            top3_idx       = np.argsort(predictions[0])[-3:][::-1]
            predicted_class = class_names[top3_idx[0]]
            confidence      = predictions[0][top3_idx[0]] * 100

            # Parse name
            parts   = predicted_class.split('___')
            plant   = parts[0].replace('_', ' ')
            disease = parts[1].replace('_', ' ') if len(parts) > 1 else 'Unknown'
            # ── Result Card ───────────────────────────────
        if confidence >= 90:
            st.success(f"✅ Confidence: {confidence:.1f}%")
        elif confidence >= 70:
            st.warning(f"⚠️ Confidence: {confidence:.1f}%")
        else:
            st.error(f"❌ Low Confidence: {confidence:.1f}%")

        st.markdown(f"### 🌱 Plant: `{plant}`")
        st.markdown(f"### 🦠 Disease: `{disease}`")

        # ── Disease Info ──────────────────────────────
        if 'healthy' in disease.lower():
            st.balloons()
            st.success("🎉 This plant appears healthy!")
        else:
            st.warning("⚠️ Disease detected! Consider consulting an agronomist.")
        # ── Top 3 ─────────────────────────────────────
        st.markdown("---")
        st.markdown("#### 📊 Top 3 Predictions")
        for idx in top3_idx:
            name = class_names[idx].replace('___', ' → ').replace('_', ' ')
            conf = predictions[0][idx] * 100
            st.progress(int(conf), text=f"{name}  {conf:.1f}%")

    else:
        st.info("👈 Upload a leaf image to get started")
        st.markdown("""
        **How to use:**
        1. Click **Browse files** on the left
        2. Upload a plant leaf image
        3. See instant disease prediction!
        """)