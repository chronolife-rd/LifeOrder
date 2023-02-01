import streamlit as st
import pandas as pd
import random
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import datetime
import pdfkit

class FileGenration :
     
     
     def __init__(self,GlobalOrderInformation,DetailOrderInformation) :

          self.GlobalOrderInformation = GlobalOrderInformation
          self.DetailOrderInformation = DetailOrderInformation



          
          

def DicToDataframePlot (dic):
     df = pd.DataFrame.from_dict(dic,orient='index') 
     st.dataframe(df)

     return df

def completBilingInformation ():
    pass

def generateQuantityDic (dicOrder):
     
     quantity_NEX_TSH_1_01_A32 = 0
     quantity_ASE_0_01 = 0
     quantity_PSS_0_01 = 0 
     quantity_USQ_0_01 = 0
     quantity_CHQ_3_01 = 0
     
     quantity_NEX_0014_LBL_09 = 0
     quantity_NEX_0017_LBL_08 = 0
     quantity_NEX_0001_LBL_07 = 0
     quantity_NEX_0018_LBL_08 = 0


     for i in range (1,len(dicOrder)+1):


          
          
          if  dicOrder[f"End user {i}"]["T-shirt Quantity "] > 0 :

               quantity_NEX_TSH_1_01_A32 += dicOrder[f"End user {i}"]["T-shirt Quantity "]   
               
               quantity_ASE_0_01 += dicOrder[f"End user {i}"]["T-shirt Quantity "]
               quantity_PSS_0_01 += dicOrder[f"End user {i}"]["T-shirt Quantity "]
               quantity_USQ_0_01 += dicOrder[f"End user {i}"]["T-shirt Quantity "]
               quantity_CHQ_3_01 += dicOrder[f"End user {i}"]["T-shirt Quantity "] 

          else :
               st.warning("You have to order the number of paid t-shirt")

          if dicOrder[f"End user {i}"]["EndUserSpeakingLanguge"] == "Français":
               quantity_NEX_0014_LBL_09 += dicOrder[f"End user {i}"]["T-shirt Quantity "]
               quantity_NEX_0017_LBL_08 += dicOrder[f"End user {i}"]["T-shirt Quantity "]

          elif dicOrder[f"End user {i}"]["EndUserSpeakingLanguge"] == "English":
               quantity_NEX_0001_LBL_07 += dicOrder[f"End user {i}"]["T-shirt Quantity "]
               quantity_NEX_0018_LBL_08 += dicOrder[f"End user {i}"]["T-shirt Quantity "]
          
          else :
               st.warning("You have to select a language")


     quantyDoc = [
          quantity_NEX_TSH_1_01_A32,

          quantity_ASE_0_01,
          quantity_PSS_0_01,
          quantity_USQ_0_01,
          quantity_CHQ_3_01,

          quantity_NEX_0014_LBL_09,
          quantity_NEX_0017_LBL_08,
          quantity_NEX_0001_LBL_07,
          quantity_NEX_0018_LBL_08
     ]

     return  quantyDoc


def completeKoreHtml (OrderInformation,OrderDetails):

    env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
    myQuantitDoc = generateQuantityDic(OrderDetails)
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

          quantity_NEX_TSH_1_01_A32 = myQuantitDoc[0],
          quantity_NEX_TSH_1_01_A34 = 0,
          quantity_NEX_TSH_1_01_A36 =0,
          quantity_NEX_TSH_1_01_A38 =0,
          quantity_NEX_TSH_1_01_A40 = 0,
          quantity_NEX_TSH_1_01_A42 =0,
          quantity_NEX_TSH_1_01_A44 = 0,
          quantity_NEX_TSH_1_01_A46 =0,
          quantity_NEX_TSH_1_01_A48 =0,
          quantity_NEX_TSH_1_01_A50 = 0,
          quantity_NEX_TSH_1_01_A52 = 0,

          quantity_AFF_TSH_1_01_A32 =0,
          quantity_AFF_TSH_1_01_A34 =0,
          quantity_AFF_TSH_1_01_A36 =0,
          quantity_AFF_TSH_1_01_A38 = 0,
          quantity_AFF_TSH_1_01_A40 =0,
          quantity_AFF_TSH_1_01_A42 =0,
          quantity_AFF_TSH_1_01_A44 =0,
          quantity_AFF_TSH_1_01_A46 = 0,
          quantity_AFF_TSH_1_01_A48 =0,
          quantity_AFF_TSH_1_01_A50 = 0,
          quantity_AFF_TSH_1_01_A52 =0,

          quantity_CHQ_3_01 = myQuantitDoc[2],
          quantity_USQ_0_01 = myQuantitDoc[2],
          quantity_PSS_0_01 = myQuantitDoc[2],
          quantity_ASE_0_01 = 0,

          quantity_AFF_0001_LBL_13 = 0,
          quantity_AFF_0010_LBL_06 = 0,
          quantity_AFF_0090_LBL_08 = 0,
          quantity_AFF_0090_LBL_05 =0,
          quantity_NEX_0014_LBL_09 =0,
          quantity_NEX_0017_LBL_08 =0,
          quantity_NEX_0001_LBL_07 =0,
          quantity_NEX_0018_LBL_08 =0,

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
