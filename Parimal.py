import streamlit as st
import easyocr
from PIL import Image
import numpy as np

# Set up the page title
st.title("OCR and Keyword Search (Supports English & Hindi)")

# Initialize EasyOCR reader with Hindi ('hi') and English ('en') support
reader = easyocr.Reader(['en', 'hi'])

# File uploader to allow image upload
uploaded_file = st.file_uploader("Upload an image (supports English & Hindi text)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert the image to a numpy array for OCR processing
    img_array = np.array(image)
    
    # Perform OCR on the image using EasyOCR
    with st.spinner("Extracting text..."):
        result = reader.readtext(img_array)
    
    # Extract the text and display it
    extracted_text = "\n".join([res[1] for res in result])
    st.subheader("Extracted Text:")
    st.text_area("OCR Result (English & Hindi)", extracted_text, height=200)

    # Keyword search functionality
    keyword = st.text_input("Enter a keyword to search in the extracted text:")

    if keyword:
        # Search for the keyword in the extracted text (case insensitive)
        search_results = [text for text in extracted_text.split('\n') if keyword.lower() in text.lower()]
        
        # Display the matching results
        if search_results:
            st.subheader("Search Results:")
            st.text_area("Matching Sections", "\n".join(search_results), height=200)
        else:
            st.warning(f"No matches found for the keyword: {keyword}")
else:
    st.info("Please upload an image containing English or Hindi text.")