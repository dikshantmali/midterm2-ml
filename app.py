import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import tensorflow as tf
#from keras.preprocessing import image
from werkzeug.utils import secure_filename
st.set_option('deprecation.showfileUploaderEncoding', False)
#from keras.models import load_model

html_temp = """
   <div class="" style="background-color:salmon;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Dikshant Mali - PIET18CS049</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Digital Image Processing End-Term Examination</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
  
st.title("""
        Collor Palette
         """
         )
R = st.slider('R', min_value=0, max_value=255, step=1)
G = st.slider('G', min_value=0, max_value=255, step=1)
B = st.slider('B', min_value=0, max_value=255, step=1)

import cv2
from  PIL import Image, ImageOps
def import_and_predict():
  image_data = np.zeros((100,100,3), np.uint8)
	   
  image_data[:] = [R,G,B]
  st.image(image_data, use_column_width=True)
  return 0
    
if st.button("Change Color"):
  result=import_and_predict()
  
if st.button("About"):
  st.header("Dikshant Mali")
  st.subheader("Student, Department of Computer Engineering, PIET")
html_temp = """
   <div class="" style="background-color:white;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:black;margin-top:10px;">Digital Image processing EndTerm Lab</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
