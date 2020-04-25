#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:02:09 2020

@author: utsav
"""

import numpy as np
import cv2
import base64
import requests
import json

def to_image_string(image_filepath):
    return base64.b64encode(open(image_filepath, 'rb').read())#.encode('base64')

def from_base64(base64_data):
    nparr = np.fromstring(base64_data.decode('base64'), np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)

def hit_api_validate(number):
    # prepare headers for http request
    content_type = 'application/json'
    headers = {'content-type': content_type}
    addr = 'http://localhost:9001'
    url = addr + '/api/validate'
    response = requests.post(url, json={"test_number": number} , headers=headers)
    return json.loads(response.text)

def hit_api_extract(img):
    #img_bytes = base64.b64encode(img)
    #convert byte to string
    #encoded_string = img_bytes.decode("utf-8")
    # prepare headers for http request
    content_type = 'application/json'
    headers = {'content-type': content_type}
    addr = 'http://localhost:9001'
    url = addr + '/api/ocr'
    response = requests.post(url, json={"doc_b64": base64.b64encode(img.getvalue()).decode()} , headers=headers)
    return json.loads(response.text)


def hit_api_mask_aadhaar(img,number_list):
#    img_bytes = to_image_string(filepath)
#    #convert byte to string
#    encoded_string = img_bytes.decode("utf-8")
#    # prepare headers for http request
    content_type = 'application/json'
    headers = {'content-type': content_type}
    addr = 'http://localhost:9001'
    url = addr + '/api/mask'
    response = requests.post(url, json={"doc_b64": base64.b64encode(img.getvalue()).decode(), 'aadhaar': [str(number_list)]}, headers=headers)
    
    return json.loads(response.text)
    


def hit_api_brut_mask(img):
#    img_bytes = to_image_string(input_name)
#    #convert byte to string
#    encoded_string = img_bytes.decode("utf-8")
#    # prepare headers for http request
    content_type = 'application/json'
    headers = {'content-type': content_type}
    addr = 'http://localhost:9001'
    url = addr + '/api/brut_mask'
    response = requests.post(url, json={"doc_b64": base64.b64encode(img.getvalue()).decode()}, headers=headers)
    return json.loads(response.text)
#    r = json.loads(response.text)
#    save_name = output_name
#    decoded_data = base64.b64decode(r['doc_b64_brut_masked'])
#    np_data = np.fromstring(decoded_data,np.uint8)
#    img = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)
#    cv2.imwrite(save_name,img)
#    return "masked document saved as "+ save_name

def hit_api_sample_pipe(img,brut = False):
#    img_bytes = to_image_string(input_name)
#    #convert byte to string
#    encoded_string = img_bytes.decode("utf-8")
#    # prepare headers for http request
    content_type = 'application/json'
    headers = {'content-type': content_type}
    addr = 'http://localhost:9001'
    url = addr + '/api/sample_pipe'
    response = requests.post(url, json={"doc_b64": base64.b64encode(img.getvalue()).decode(), "brut" : brut}, headers=headers)
    return json.loads(response.text)
#    r = json.loads(response.text)
#    if r['is_masked']:
#        save_name = output_name
#        decoded_data = base64.b64decode(r['doc_b64_masked'])
#        np_data = np.fromstring(decoded_data,np.uint8)
#        img = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)
#        cv2.imwrite(save_name,img)
#        print("Execution Mode =>",r['mode_executed'])
#        if r['mode_executed'] == "OCR-MASKING":
#            print("Aadhaar List =>",r['aadhaar_list'])
#            print("Validated Aadhaar list =>",r['valid_aadhaar_list'])
#        return "masked document saved as "+ save_name
#    else:
#        print("Execution Mode =>",r['mode_executed'])
#        print("Error =>",r['error'])
#        return "Unable to find given number in the image :/ (try brut mode)"
#

################################################### UI ################################

import streamlit as st

st.title("[PyraDox :page_with_curl:](https://github.com/festivitymishra/PyraDox)")

st.info(
    """
    **PyraDox is a python tool which helps in document digitization** by extracting text 
    information and masking of personal information with the help of Tesseract-ocr.
"""
)


st.sidebar.subheader('PyraDox :page_with_curl:')

Run_Mode = st.sidebar.selectbox(
    'Select Document Type',
    ('Select Doc','Aadhaar Card', 'Driver Licence', 'Passport', 'Pan Card'))


if Run_Mode == 'Select Doc':

    image_filepath = 'resources/PyraDox.jpg'
    
    st.image(open(image_filepath, 'rb').read(), caption='', use_column_width=True)
    
    st.write("Supported Documents : \n - Aadhaar Card (UIDAI)"
             )
elif Run_Mode == 'Aadhaar Card':
    st.write(" Document Type **Aadhaar Card** ")
    feature = st.sidebar.radio("What's dow you want to try?",('Mask 1st 8 digits of Aadhaar',
                                                              'Validate Aadhaar Number',
                                                              'Extract Aadhaar Number', 
                                                              'Mask Aadhaar Number',
                                                              'Brut Mask Numbers'))
    
    if feature == "Validate Aadhaar Number":
        st.write('Please enter 12 digit Aadhaar Number')
        number = st.number_input('Insert aadhaar number', min_value=10000000000, 
                                  max_value=999999999999, value=397788000234, 
                                  step=1,format = '%d')
        #st.write('The current number is ', number)
        if st.button('Validate'):
            if hit_api_validate(number)['validity']:
                st.write(" :white_check_mark: Valid Aadhaar Card Sequence Number")
            else:
                st.write(" :no_entry: Invalid Aadhaar Card Sequence Number")
    elif feature == "Extract Aadhaar Number":

        uploaded_file = st.file_uploader("Upload an image file", type=['png', 'jpg'])
        
        if uploaded_file is not None:
#            image = Image.open(uploaded_file)
            st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True) #width = 450)#
            st.write("Click on extract to **extract** Aadhar Number from the image!")
            if st.button('Extract'):
                #st.write(hit_api_extract_new(uploaded_file))
                extract_response = hit_api_extract(uploaded_file)['aadhaar_list']
                
                
                if len(extract_response)>0:
                    st.write(" :white_check_mark: Extracted Aadhaar Number is **",extract_response[0],"**")
                else:
                    st.write(" :no_entry: Failed to find any Aadhaar Number in the given document")
    elif feature == "Mask Aadhaar Number":
        uploaded_file_2 = st.file_uploader("Upload an image file", type=['png', 'jpg'])
        st.write('Please enter 12 digit Aadhaar Number to be Masked')
        number_2 = st.number_input('Insert aadhaar number', min_value=10000000000, 
                                  max_value=999999999999, value=397788000234, 
                                  step=1,format = '%d')
        
        if uploaded_file_2 is not None and number_2 is not None:
            st.image(uploaded_file_2, caption='Uploaded Image.', width = 400)#
            st.write("Click on **Mask** to mask given Aadhar Number from the image!")
            
            if st.button('Mask'):
                r = hit_api_mask_aadhaar(uploaded_file_2,number_2)
                if r['is_masked']:
                    decoded_data = base64.b64decode(r['doc_b64_masked'])
                    st.image(decoded_data, caption='Masked Image.', width = 400)#
                    st.write(" :white_check_mark: Masked Given Number in the Document")
                else:
                    st.write(" :no_entry: Unable to find given number in the image :/ (try brut mode)")


        
    elif feature == "Mask 1st 8 digits of Aadhaar":
        uploaded_file_3 = st.file_uploader("Upload an image file", type=['png', 'jpg'])
        
        if uploaded_file_3 is not None:
            st.image(uploaded_file_3, caption='Uploaded Image.', width = 400)#
            st.write("Click on **Mask** to Mask first 8 digits Aadhar Number from the image!")
            brut_mode = st.checkbox('Use Brut Mode')
#            st.write("brut_mode is",brut_mode)
            if st.button('Mask'):
                r = hit_api_sample_pipe(uploaded_file_3,brut_mode)
                if r['is_masked']:
                    decoded_data_1 = base64.b64decode(r['doc_b64_masked'])
                    st.image(decoded_data_1, caption='Masked Image.', width = 400)#
                    st.write(" :white_check_mark: Masked Given Number in the Document")
                    st.write("Execution Mode =>",r['mode_executed'])
                    if r['mode_executed'] == "OCR-MASKING":
                        st.write("Aadhaar List =>**",r['aadhaar_list'][0],"**")
                        st.write("Validated Aadhaar list =>**",r['valid_aadhaar_list'][0],"**")
                else:
                    st.write("Execution Mode =>",r['mode_executed'])
                    st.write("Error =>",r['error'])
                    st.write("  :no_entry:  Unable to find given number in the image :/ (try brut mode)")
    elif feature == "Brut Mask Numbers":
        uploaded_file_4 = st.file_uploader("Upload an image file", type=['png', 'jpg'])
        
        if uploaded_file_4 is not None:
            st.image(uploaded_file_4, caption='Uploaded Image.', width = 400)#
            st.write("Click on **BRUT Mask** to Brut Mask Numbers from the image!")
#            st.write("brut_mode is",brut_mode)
            if st.button('BRUT Mask'):
                r = hit_api_brut_mask(uploaded_file_4)
                decoded_data_2 = base64.b64decode(r['doc_b64_brut_masked'])
                st.image(decoded_data_2, caption='Masked Image.', width = 400)#

else:
    st.write(" **Yowza! we are yet baking it for you ...** :penguin:")
    comingsoon = 'resources/coming-soon.jpg'
    st.image(open(comingsoon, 'rb').read(), caption='', use_column_width=True)




#
#w = st.file_uploader("Upload a CSV file", type="csv")
#if w:
#    import pandas as pd
#
#    data = pd.read_csv(w)
#    st.write(data)
