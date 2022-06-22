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

customer = st.selectbox("Select Customer to know CLV",df['CustomerID'].unique())

df_graph = pd.read_csv("clv_new.csv")
df_graph['CustomerID'] = df_graph['CustomerID'].astype(int)
customer_graph = customer
# st.write(customer_graph)

def fun_graph(CustomerID):
    data = df_graph[df_graph['CustomerID'] == CustomerID]
    value = data[['InvoiceDate','TotalPurchase']]
    return value

graph_df = fun_graph(customer)
# st.write(graph_df)
graph_df['InvoiceDate'] = pd.to_datetime(graph_df['InvoiceDate'])
graph_df["Date"] = graph_df["InvoiceDate"].dt.date
graph_df["Time"] = graph_df["InvoiceDate"].dt.time
graph_df=graph_df.groupby(['Date']).agg({'TotalPurchase': lambda price: price.sum()})
# graph_df.reset_index(inplace=True)
# value_avg = graph_df.TotalPurchase.values
# st.write(value_avg)
# st.write(sum(value_avg))
# st.write(average(value_avg))

nav = st.sidebar.radio("Select Method of Calculation",('Direct Method','Whole Calculation'))

if nav == 'Direct Method':
    theme_less = {'bgcolor': '#f9f9f9','title_color': 'red','content_color': 'red'}
    theme_middle = {'bgcolor': '#f9f9f9','title_color': 'orange','content_color': 'orange'}
    theme_high = {'bgcolor': '#f9f9f9','title_color': 'blue','content_color': 'blue'}

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
            st.sidebar.error("Customer will Discontinue")
        elif clv <5000:
            hc.info_card(title='Customer Lifetime Value Metric', content=clv, theme_override=theme_middle)
            st.sidebar.warning("Please Pay Attention to Customer")
        else:
            hc.info_card(title='Customer Lifetime Value Metric', content=clv, theme_override=theme_high)
            st.sidebar.success("Customer will Purchase Shortly")

elif nav == 'Whole Calculation':
    theme_less = {'bgcolor': '#f9f9f9','title_color': 'red','content_color': 'red'}
    theme_middle = {'bgcolor': '#f9f9f9','title_color': 'orange','content_color': 'orange'}
    theme_high = {'bgcolor': '#f9f9f9','title_color': 'blue','content_color': 'blue'}

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
        value = data['InvoiceNo']
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
            st.sidebar.error("Customer will Discontinue")
        elif cltv < 5000:
            hc.info_card(title='Customer Lifetime Value Metric', content=cltv, theme_override=theme_middle)
            st.sidebar.warning("Please Pay Attention to Customer")
        else:
            hc.info_card(title='Customer Lifetime Value Metric', content=cltv, theme_override=theme_high)
            st.sidebar.success("Customer will Purchase Shortly")

    col1, col2, col3 = st.columns((1,1,1))
    with col1:
        hc.info_card(title='Average Purchase Value', content=apv, theme_override=theme_less)
    with col2:
        hc.info_card(title='Average Purchase Frequency Rate', content=apfr, theme_override=theme_less)
    with col3:
        hc.info_card(title='Average Customer Lifespan', content=acl, theme_override=theme_less)

c1, c2, c3 = st.columns((0.6,1,0.2))
with c2:    
    st.subheader("Purchase Order Graph")
# graph_df["Average Value"] = average(value_avg)
st.bar_chart(graph_df)
