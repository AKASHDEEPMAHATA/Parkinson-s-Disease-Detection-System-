import numpy as np
import pickle
import streamlit as st
from sklearn import  *


st.title("Parkinson's Disease Detection System")
st.write("Parkinson's disease is a progressive disorder that affects the nervous system and the parts of the body controlled by the nerves. ")

# row 1
st.subheader("Vocal fundamental frequency")

col1,col2,col3 = st.columns(3)

with col1:
    ip1= st.text_input('MDVP:Fo(Hz) - Average vocal fundamental frequency')

with col2:
    ip2 = st.text_input('MDVP:Fhi(Hz) - Maximum vocal fundamental frequency')

with col3:
    ip3 = st.text_input('MDVP:Flo(Hz) - Minimum vocal fundamental frequency')


# row 2
st.subheader("Variation in fundamental frequency")

col4,col5,col6,col7,col8 = st.columns(5)

with col4:
    ip4= st.text_input('MDVP:Jitter(%)')

with col5:
    ip5 = st.text_input('MDVP:Jitter(Abs)')

with col6:
    ip6 = st.text_input('MDVP:RAP')

with col7:
    ip7 = st.text_input('MDVP:PPQ')

with col8:
    ip8 = st.text_input('Jitter:DDP')


# row 3
st.subheader("Variation in amplitude")

col9,col10,col11,col12,col13,col14 = st.columns(6)

with col9:
    ip9= st.text_input('MDVP:Shimmer')

with col10:
    ip10 = st.text_input('MDVP:Shimmer(dB)')

with col11:
    ip11 = st.text_input('Shimmer:APQ3')

with col12:
    ip12 = st.text_input('Shimmer:APQ5')

with col13:
    ip13 = st.text_input('MDVP:APQ')

with col14:
    ip14 = st.text_input('Shimmer:DDA')


# row 4
st.subheader("Ratio of noise to tonal components in the voice")

col15,col16 = st.columns(2)

with col15:
    ip15= st.text_input('NHR')

with col16:
    ip16 = st.text_input('HNR')



# row 5
st.subheader("Two nonlinear dynamical complexity measures")

col17,col18 = st.columns(2)

with col17:
    ip17= st.text_input('RPDE')

with col18:
    ip18 = st.text_input('D2')


# row 6
st.subheader("Signal fractal scaling exponent")

ip19= st.text_input('DFA')



# row 7
st.subheader("Three nonlinear measures of fundamental frequency variation")

col20,col21,col22 = st.columns(3)

with col20:
    ip20= st.text_input('spread1')

with col21:
    ip21 = st.text_input('spread2')

with col22:
    ip22 = st.text_input('PPE')


st.text("")
st.text("")
st.text("")

# -------------------------------------------------------------


parkinsons_model = pickle.load(open('parkinson.sav', 'rb'))

# code for Prediction
parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
if st.button("Parkinson's Test Result"):
        
        parkinsons_prediction = parkinsons_model.predict([[ip1,ip2,ip3,ip4,ip5,ip6,ip7,ip8,ip9,ip10,ip11,ip12,ip13,ip14,ip15,ip16,ip17,ip18,ip19,ip20,ip21,ip22]]) 

        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"

st.text("")
st.text("")
st.success(parkinsons_diagnosis)



