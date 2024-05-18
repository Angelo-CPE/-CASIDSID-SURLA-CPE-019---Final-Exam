# -*- coding: utf-8 -*-
"""CSWP

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iOnrt08Evk6Onjl_uj496cn9JhXstijw
"""

import streamlit as st
import tensorflow as tf

@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('plant_classifier.hdf5')
  return model
model=load_model()
st.write("""
# CS - Weather Prediction System"""
)
file=st.file_uploader("Choose a weather image from computer",type=["jpg","png"])

import cv2
from PIL import Image,ImageOps
import numpy as np

def import_and_predict(image_data,model):
    size=(128,128)
    image=ImageOps.fit(image_data,size,Image.ANTIALIAS)
    img=np.asarray(image)
    img=cv2.resize(img, (128,128), interpolation=cv2.INTER_NEAREST)
    if img.ndim==3 and img.shape[2]==3:
      img=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_reshape=img.reshape((1,)+img.shape+(1,))
    prediction=model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names=['Shine', 'Rain', 'Sunrise', 'Cloudy']
    string="OUTPUT : "+class_names[np.argmax(prediction)]
    st.success(string)