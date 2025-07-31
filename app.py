import streamlit as st
import pickle
import numpy as np

# Import Model

pipe = pickle.load(open("pipe.pkl", "rb"))
df = pickle.load(open("df.pkl", "rb"))

st.title("Laptop Predictor")

# brand
Company = st.selectbox("Brand",df["Company"].unique())

# Type of laptop
Type = st.selectbox("Type",df["TypeName"].unique())

# Ram
Ram = st.selectbox("Ram(in GB)", [2, 4, 6, 8, 12, 16, 24, 32, 64])

# Weight
Weight = st.number_input("Weight of the Laptop")

# Touchscreen
Touchscreen = st.selectbox("Touchscreen", ["No", "Yes"])

# IPS
Ips = st.selectbox("IPS", ["No", "Yes"])

# Screen Size
Screen_size = st.number_input("Screen Size")

# Resolution
Resolution = st.selectbox("Screen Resolution", ["1920x1080", "1366x768", "1600x900", "3840x2160", "3200x1800", "2880x1800", "2560x1600", "2560x1448", "2304x1440"])

# Cpu
Cpu = st.selectbox("Cpu Brand", df["Cpu Brand"].unique())

Hdd = st.selectbox("HDD(in GB)",[0,128,256,512,1024,2048])

Ssd = st.selectbox("SSD(in GB)",[0,8,128,256,512,1024])

Gpu = st.selectbox("GPU", df["Gpu Brand Name"].unique())

Os = st.selectbox("Os", df["OS"].unique())

if st.button("Predict Price"):
    
    #query
    
    if Touchscreen=="Yes":
        Touchscreen=1
    else:
        Touchscreen=0

    if Ips=="Yes":
        Ips=1
    else:
        Ips=0

    X_res=int(Resolution.split("x")[0])
    Y_res=int(Resolution.split("x")[1])
    Ppi=((X_res**2)+(Y_res**2))**0.5/Screen_size

    query=np.array([Company,Type,Ram,Weight,Touchscreen,Ips,Ppi,Cpu,Hdd,Ssd,Gpu,Os])

    query=query.reshape(1,12)
    st.title("The predicted price of this configuration is "+str(int(np.exp(pipe.predict(query)[0]))))



