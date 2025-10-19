import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# App configuration
st.set_page_config(page_title="MNIST Digit Classifier", layout="centered")
st.title(" MNIST Digit Classifier")
st.markdown("Upload a **28x28 grayscale image** of a handwritten digit (PNG or JPG).")

# File upload
uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

if uploaded_file:
    try:
        # Load and preprocess image
        image = Image.open(uploaded_file).convert("L").resize((28, 28))
        img_array = np.array(image) / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)

        # Load trained model
        model = tf.keras.models.load_model("mnist_model.h5")

        # Predict
        prediction = model.predict(img_array)
        predicted_digit = np.argmax(prediction)

        # Display results
        st.image(image, caption=f"Predicted: {predicted_digit}", width=150)
        st.success(f" Model Prediction: **{predicted_digit}**")

    except Exception as e:
        st.error(" Error processing image or loading model.")
        st.code(str(e), language="bash")
else:
    st.info(" Please upload a digit image to begin.")
