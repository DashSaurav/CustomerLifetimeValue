import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
from PIL import Image
import hydralit_components as hc

df = pd.read_csv("clv.csv")
df['CustomerID'] = df['CustomerID'].astype(int)
# st.write(df['CustomerID'][0], type(df['CustomerID'][0]))

img = Image.open("MicrosoftTeams-image.png")
st.sidebar.image(img, width=300)
st.sidebar.info("Customer lifetime value is a metric that indicates the total revenue a business can reasonably expect from a single customer account throughout the business relationship.")
c1, c2, c3 = st.columns((0.4,1,0.2))
with c2:
    st.header("Predicting Customer Lifetime Value")

nav = st.sidebar.radio("Select Method of Calculation",('Direct Method','Whole Calculation'))

if nav == 'Direct Method':
    theme_less = {'bgcolor': '#f9f9f9','title_color': 'red','content_color': 'red'}
    theme_middle = {'bgcolor': '#f9f9f9','title_color': 'orange','content_color': 'orange'}
    theme_high = {'bgcolor': '#f9f9f9','title_color': 'blue','content_color': 'blue'}

    customer = st.selectbox("Select Customer to know CLV",df['CustomerID'].unique())
    # st.write(customer)

    def func_1(CustomerID):
        data = df[df['CustomerID'] == CustomerID]
        value = data['TotalPurchase']
        return int(value)

    # st.info(func_1(customer))
    clv = func_1(customer)*2
    col1, col2, col3 = st.columns((0.5,1,0.5))
    with col2:
        if clv < 1000:
            hc.info_card(title='Customer Lifetime Value Metric', content=clv, theme_override=theme_less)
        elif clv <5000:
            hc.info_card(title='Customer Lifetime Value Metric', content=clv, theme_override=theme_middle)
        else:
            hc.info_card(title='Customer Lifetime Value Metric', content=clv, theme_override=theme_high)

elif nav == 'Whole Calculation':
    theme_less = {'bgcolor': '#f9f9f9','title_color': 'red','content_color': 'red'}
    theme_middle = {'bgcolor': '#f9f9f9','title_color': 'orange','content_color': 'orange'}
    theme_high = {'bgcolor': '#f9f9f9','title_color': 'blue','content_color': 'blue'}

    customer = st.selectbox("Select Customer to know CLV",df['CustomerID'].unique())
    # st.write(customer)

    def fun_apv(CustomerID):
        data = df[df['CustomerID'] == CustomerID]
        value = data['InvoiceNo']
        value_1 = data['TotalPurchase']
        apv = int(value_1)/int(value)
        return round(apv)
    
    def fun_apfr(CustomerID):
        data = df[df['CustomerID'] == CustomerID]
        value = data['InvoiceNo']
        value_1 = len(data['TotalPurchase'])
        apfr = int(value)/int(value_1)
        return round(apfr)
    
    def fun_acl(CustomerID):
        data = df[df['CustomerID'] == CustomerID]
        value = data['CustomerID']
        acl = 2/len(value)
        return round(acl)

    apv = fun_apv(customer)
    apfr = fun_apfr(customer)
    cv = apv*apfr
    acl = fun_acl(customer)
    cltv = cv*acl 
    
    col1, col2, col3 = st.columns((0.5,1,0.5))
    with col2:
        if cltv < 1000:
            hc.info_card(title='Customer Lifetime Value Metric', content=cltv, theme_override=theme_less)
        elif cltv < 5000:
            hc.info_card(title='Customer Lifetime Value Metric', content=cltv, theme_override=theme_middle)
        else:
            hc.info_card(title='Customer Lifetime Value Metric', content=cltv, theme_override=theme_high)

    col1, col2, col3 = st.columns((1,1,1))
    with col1:
        hc.info_card(title='Average Purchase Value', content=apv, theme_override=theme_less)
    with col2:
        hc.info_card(title='Average Purchase Frequency Rate', content=apfr, theme_override=theme_less)
    with col3:
        hc.info_card(title='Customer Value', content=cv, theme_override=theme_less)
