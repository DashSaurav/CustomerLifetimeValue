from math import floor
import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
from PIL import Image
import time
import requests
# from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_download = "https://assets3.lottiefiles.com/packages/lf20_jxdtgpuk.json"
lottie_download = load_lottieurl(lottie_url_download)
# df = pd.read_csv("Online Retail.csv", encoding= 'unicode_escape')


# col,hid,mid = st.columns(3)
# with hid:
img = Image.open("MicrosoftTeams-image.png")
st.sidebar.image(img, width=200)
st.sidebar.info("Customer lifetime value is a metric that indicates the total revenue a business can reasonably expect from a single customer account throughout the business relationship.")
st.header("Predicting Customer Lifetime Value")


c = st.columns(3)
with c[0]:
    spent_money = st.number_input("Provide the Total money spend by customer", value=100)
with c[2]:
    profit = st.number_input("Give the Average Profit by business in %", value=5)

profit_margin = spent_money * (profit/100)
# st.write(profit_margin)
st.subheader("Fill out Sales amount for the Customer for the Given Month in $")
cc = st.columns(3)
with cc[0]:
    jan = st.number_input("January month", value=10)
with cc[1]:
    feb = st.number_input("February Month", value=10)
with cc[2]:
    mar = st.number_input("March Month", value=10)
cc1 = st.columns(3)
with cc[0]:
    apr = st.number_input("April Month", value=10)
with cc[1]:
    may = st.number_input("May Month", value=10)
with cc[2]:
    jun = st.number_input("June Month", value=10)

cm = st.columns(3)
with cm[1]:
    if st.button("Compute the Customer Lifetime Value"):
        CLV = (jan+feb+mar+apr+may+jun) * profit_margin
        # st.info(CLV)
        if int(CLV) < 5000:
            with st_lottie_spinner(lottie_download, key="download", height=200,width=300):
                time.sleep(1)
            #st.snow()
            st.warning("Customer Might GO.")
            st.sidebar.subheader("Profit Margin in $")
            st.sidebar.info(floor(profit_margin))
            st.sidebar.subheader("Customer Lifetime Value in $")
            st.sidebar.info(floor(CLV))
        else:
            with st_lottie_spinner(lottie_download, key="download", height=200,width=300):
                time.sleep(1)
            #st.balloons()
            st.info("Customer Will Stay")
            st.sidebar.subheader("Profit Margin in $")
            st.sidebar.info(floor(profit_margin))
            st.sidebar.subheader("Customer Lifetime Value in $")
            st.sidebar.info(floor(CLV))


        
                    
        