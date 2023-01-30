import streamlit as st
import pandas as pd
import random
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import datetime
import pdfkit



def DicToDataframePlot (dic):
     df = pd.DataFrame.from_dict(dic,orient='index') 
     st.dataframe(df)

     return df

def completBilingInformation ():
    pass

def completDetailInformation ():
    
    pass


def completeKoreHtml (OrderInformation,OrderDetails):

    env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
    
    template = env.get_template("assets/Korefile/index.html")
    html = template.render(
        
          BillingReference = OrderInformation["Order Information"]["BillingReference"],
          PurchaseOrder = OrderInformation["Order Information"]["PurchaseOrder"],
          ClientPhoneNumber = OrderInformation["Order Information"]["ClientPhoneNumber"],
          ClientMailAddress = OrderInformation["Order Information"]["ClientMailAddress"],
          ClientInstitution = OrderInformation["Order Information"]["ClientInstitution"],
          ClientAddressNumber = OrderInformation["Order Information"]["ClientAddressNumber"],
          ClientStreet = OrderInformation["Order Information"]["ClientStreet"],
          ClientAttn = OrderInformation["Order Information"]["ClientAttn"],
          ClientZIPCode = OrderInformation["Order Information"]["ClientZIPCode"],
          ClientCity = OrderInformation["Order Information"]["ClientCity"],
          ClientCountry = OrderInformation["Order Information"]["ClientCountry"],
          ClientSiteNR = OrderInformation["Order Information"]["ClientSiteNR"],
          ClientDepartement = OrderInformation["Order Information"]["ClientDepartement"],
          TShirtQuantity = OrderInformation["Order Information"]["TShirtQuantity"],
          NumberEndUser = OrderInformation["Order Information"]["NumberEndUser"],

          quantity_NEX_TSH_1_01_A32 =  OrderDetails["End user 1"]["T-shirt Quantity "]









    )

    return html


def downloadKorePDF (OrderInformation, OrderDetails):

    html = completeKoreHtml(OrderInformation,OrderDetails)
    pdf = pdfkit.from_string(html, False)
    st.download_button(
          "⬇️ Download PDF for Kore order",
            data = pdf,
            file_name="Order_Kore_Chronolife.pdf",
          
     )


def download_csv_file ( df):
     csvFile  = convertDataFrameToCSV(df)
     st.download_button(
          "⬇️ Download PDF order",
            data = csvFile,
            file_name="Order_Chronolife.csv",
          
     )
              

@st.cache
def convertDataFrameToCSV(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
