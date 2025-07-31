import streamlit as st
import pickle as pk
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

model = pk.load(open("model.pkl","rb"))
scaler2 = pk.load(open("scaler2.pkl","rb"))

heading = st.header(" Leptop  Price Prediction ")


Inches = st.slider("Choose Inches",0,18)
Ram = st.slider("Choose Ram",0,64)
Weight= st.slider("Choose Weight(kgs)",0,5)




if st.button("Price"):

    leptop = pd.DataFrame([['Inches', 'Ram', 'Weight', 'Price']],
                         columns = ['Inches', 'Ram', 'Weight', 'Price'])
    
    leptop = scaler2.transform(leptop)
    price = model.predict(leptop)
    
    print(price)
    # ans = price
    # a = ans.item()
    # print(type(a))
    # st.markdown(" leptop  Price    =     {} " .format(a))
  