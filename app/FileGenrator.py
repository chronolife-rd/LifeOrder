import streamlit as st
import pandas as pd
import random
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import datetime
import pdfkit
import jinja2
from zipfile import ZipFile


def DicToDataframePlot (GlobalOrderInfo,DetailOrderInfo):
     df_GlobalOrderInfo= pd.DataFrame(GlobalOrderInfo,index = [0]) 
     df_DetailOrderInfo= pd.DataFrame.from_dict(DetailOrderInfo,orient='index') 

     st.dataframe(df_GlobalOrderInfo)
     st.dataframe(df_DetailOrderInfo)



def generateQuantityDic (dicOrder):
    

     quantyDoc = {

          
          "quantity_NEX_TSH_1_01_A32" : 0,
          "quantity_NEX_TSH_1_01_A34" : 0,
          "quantity_NEX_TSH_1_01_A36" : 0,
          "quantity_NEX_TSH_1_01_A38" : 0,
          "quantity_NEX_TSH_1_01_A40" : 0,
          "quantity_NEX_TSH_1_01_A42" : 0,
          "quantity_NEX_TSH_1_01_A44" : 0,
          "quantity_NEX_TSH_1_01_A46" : 0,
          "quantity_NEX_TSH_1_01_A48" : 0,
          "quantity_NEX_TSH_1_01_A50" : 0,
          "quantity_NEX_TSH_1_01_A52" : 0,

          "quantity_AFF_TSH_1_01_A32" : 0,
          "quantity_AFF_TSH_1_01_A34" : 0,
          "quantity_AFF_TSH_1_01_A36" : 0,
          "quantity_AFF_TSH_1_01_A38" : 0,
          "quantity_AFF_TSH_1_01_A40" : 0,
          "quantity_AFF_TSH_1_01_A42" : 0,
          "quantity_AFF_TSH_1_01_A44" : 0,
          "quantity_AFF_TSH_1_01_A46" : 0,

          "quantity_AFF_TSH_1_01_A48" : 0,
          "quantity_AFF_TSH_1_01_A50" : 0,
          "quantity_AFF_TSH_1_01_A52" : 0,

          "quantity_CHQ_3_01" : 0,
          "quantity_USQ_0_01" : 0,
          "quantity_PSS_0_01" : 0,
          "quantity_ASE_0_01" : 0,

          "quantity_AFF_0001_LBL_13" : 0,
          "quantity_AFF_0010_LBL_06" : 0,
          "quantity_AFF_0090_LBL_08" : 0,
          "quantity_AFF_0090_LBL_05" : 0,
          "quantity_NEX_0014_LBL_09" : 0,
          "quantity_NEX_0017_LBL_08" : 0,
          "quantity_NEX_0001_LBL_07" : 0,
          "quantity_NEX_0018_LBL_08" : 0,
          
     }
          
     


     for i in range (1,len(dicOrder)+1):
          
          
          if  dicOrder[f"End user {i}"]["EndUserTShirtQuantity"] > 0 :

               quantyDoc["quantity_NEX_TSH_1_01_A50"] += dicOrder[f"End user {i}"]["EndUserTShirtQuantity"]   
               
               quantyDoc["quantity_PSS_0_01"] += dicOrder[f"End user {i}"]["EndUserTShirtQuantity"]
               quantyDoc["quantity_USQ_0_01"] += dicOrder[f"End user {i}"]["EndUserTShirtQuantity"]
               quantyDoc["quantity_CHQ_3_01"] += dicOrder[f"End user {i}"]["EndUserTShirtQuantity"] 

          else :
               st.warning("You have to order the number of paid t-shirt")

          if dicOrder[f"End user {i}"]["EndUserSpeakingLanguge"] == "Fran??ais":
               quantyDoc["quantity_NEX_0014_LBL_09"]  += dicOrder[f"End user {i}"]["EndUserTShirtQuantity"]
               quantyDoc["quantity_NEX_0017_LBL_08"] += dicOrder[f"End user {i}"]["EndUserTShirtQuantity"]

          elif dicOrder[f"End user {i}"]["EndUserSpeakingLanguge"] == "English":
               quantyDoc["quantity_NEX_0001_LBL_07"] += dicOrder[f"End user {i}"]["EndUserTShirtQuantity"]
               quantyDoc["quantity_NEX_0018_LBL_08"] += dicOrder[f"End user {i}"]["EndUserTShirtQuantity"]
          
          else :
               st.warning("You have to select a language")


          if dicOrder[f"End user {i}"]["EndUserAdaptateur"] == "Europe":
               quantyDoc["quantity_ASE_0_01"] += dicOrder[f"End user {i}"]["EndUserTShirtQuantity"]

          else :
               quantyDoc["quantity_ASE_0_01"] += 0

     return  quantyDoc



def completeKoreHtml (OrderInformation,OrderDetails):

    env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
    myQuantitDoc = generateQuantityDic(OrderDetails)
    template = env.get_template("assets/Korefile/index.html")
    
   

    html = template.render(
        
          BillingReference = OrderInformation["BillingReference"],
          OrderNumber = OrderInformation["OrderNumber"],
          RequiredDate = OrderInformation["RequiredDate"],
          ClientPhoneNumber = OrderInformation["ClientPhoneNumber"],
          ClientMailAddress = OrderInformation["ClientMailAddress"],
          ClientInstitution = OrderInformation["ClientInstitution"],
          ClientAddressNumber = OrderInformation["ClientAddressNumber"],
          ClientStreet = OrderInformation["ClientStreet"],
          ClientAttn = OrderInformation["ClientAttn"],
          ClientZIPCode = OrderInformation["ClientZIPCode"],
          ClientCity = OrderInformation["ClientCity"],
          ClientCountry = OrderInformation["ClientCountry"],
          ClientSiteNR = OrderInformation["ClientSiteNR"],
          ClientDepartement = OrderInformation["ClientDepartement"],
          TShirtQuantity = OrderInformation["TShirtQuantity"],
          NumberEndUser = OrderInformation["NumberEndUser"],

          quantity_NEX_TSH_1_01_A32 = myQuantitDoc["quantity_NEX_TSH_1_01_A32"],
          quantity_NEX_TSH_1_01_A34 = myQuantitDoc["quantity_NEX_TSH_1_01_A34"],
          quantity_NEX_TSH_1_01_A36 = myQuantitDoc["quantity_NEX_TSH_1_01_A36"],
          quantity_NEX_TSH_1_01_A38 = myQuantitDoc["quantity_NEX_TSH_1_01_A38"],
          quantity_NEX_TSH_1_01_A40 = myQuantitDoc["quantity_NEX_TSH_1_01_A40"],
          quantity_NEX_TSH_1_01_A42 = myQuantitDoc["quantity_NEX_TSH_1_01_A42"],
          quantity_NEX_TSH_1_01_A44 = myQuantitDoc["quantity_NEX_TSH_1_01_A44"],
          quantity_NEX_TSH_1_01_A46 = myQuantitDoc["quantity_NEX_TSH_1_01_A46"],
          quantity_NEX_TSH_1_01_A48 = myQuantitDoc["quantity_NEX_TSH_1_01_A48"],
          quantity_NEX_TSH_1_01_A50 = myQuantitDoc["quantity_NEX_TSH_1_01_A50"],
          quantity_NEX_TSH_1_01_A52 = myQuantitDoc["quantity_NEX_TSH_1_01_A52"],

          quantity_AFF_TSH_1_01_A32 = myQuantitDoc["quantity_AFF_TSH_1_01_A32"],
          quantity_AFF_TSH_1_01_A34 = myQuantitDoc["quantity_AFF_TSH_1_01_A34"],
          quantity_AFF_TSH_1_01_A36 = myQuantitDoc["quantity_AFF_TSH_1_01_A36"],
          quantity_AFF_TSH_1_01_A38 = myQuantitDoc["quantity_AFF_TSH_1_01_A38"],
          quantity_AFF_TSH_1_01_A40 = myQuantitDoc["quantity_AFF_TSH_1_01_A40"],
          quantity_AFF_TSH_1_01_A42 = myQuantitDoc["quantity_AFF_TSH_1_01_A42"],
          quantity_AFF_TSH_1_01_A44 = myQuantitDoc["quantity_AFF_TSH_1_01_A44"],
          quantity_AFF_TSH_1_01_A46 = myQuantitDoc["quantity_AFF_TSH_1_01_A46"],
          quantity_AFF_TSH_1_01_A48 = myQuantitDoc["quantity_AFF_TSH_1_01_A48"],
          quantity_AFF_TSH_1_01_A50 = myQuantitDoc["quantity_AFF_TSH_1_01_A50"],
          quantity_AFF_TSH_1_01_A52 = myQuantitDoc["quantity_AFF_TSH_1_01_A52"],

          quantity_CHQ_3_01 = myQuantitDoc["quantity_CHQ_3_01"],
          quantity_USQ_0_01 = myQuantitDoc["quantity_USQ_0_01"],
          quantity_PSS_0_01 = myQuantitDoc["quantity_PSS_0_01"],
          quantity_ASE_0_01 = myQuantitDoc["quantity_ASE_0_01"],

          quantity_AFF_0001_LBL_13 = myQuantitDoc["quantity_AFF_0001_LBL_13"],
          quantity_AFF_0010_LBL_06 = myQuantitDoc["quantity_AFF_0010_LBL_06"],
          quantity_AFF_0090_LBL_08 = myQuantitDoc["quantity_AFF_0090_LBL_08"],
          quantity_AFF_0090_LBL_05 =myQuantitDoc["quantity_AFF_0090_LBL_05"],
          quantity_NEX_0014_LBL_09 =myQuantitDoc["quantity_NEX_0014_LBL_09"],
          quantity_NEX_0017_LBL_08 =myQuantitDoc["quantity_NEX_0017_LBL_08"],
          quantity_NEX_0001_LBL_07 =myQuantitDoc["quantity_NEX_0001_LBL_07"],
          quantity_NEX_0018_LBL_08 =myQuantitDoc["quantity_NEX_0018_LBL_08"],


    )

    

    
    return html


def downloadKorePDF (OrderInformation, OrderDetails):
     
     html = completeKoreHtml(OrderInformation,OrderDetails)

     pdf = pdfkit.from_string(html, False)
     st.download_button(
          "?????? Download PDF for Kore order",
            data = pdf,
            file_name="Order_Kore_Chronolife.pdf",
          
     )




def ClientFileGenerator (OrderInformation, OrderDetails):
     
     companyName = OrderInformation["ClientInstitution"]
     orderNumber = OrderInformation["OrderNumber"]


     clientFileName = f"{companyName}_{orderNumber}"


     df_OrderInformation = pd.DataFrame(OrderInformation,index = [0]) 
     df_OrderDetails = pd.DataFrame.from_dict(OrderDetails,orient="index")

     templateLoader = jinja2.FileSystemLoader(searchpath="./")
     templateEnv = jinja2.Environment(loader=templateLoader)
     TEMPLATE_FILE = "assets/ClientFile/index.html"
     template = templateEnv.get_template(TEMPLATE_FILE)
     
     outputText = template.render( 
          
          BillingReference = OrderInformation["BillingReference"],
          OrderNumber = OrderInformation["OrderNumber"],
          RequiredDate = OrderInformation["RequiredDate"],
          ClientPhoneNumber = OrderInformation["ClientPhoneNumber"],
          ClientMailAddress = OrderInformation["ClientMailAddress"],
          ClientInstitution = OrderInformation["ClientInstitution"],
          ClientAddressNumber = OrderInformation["ClientAddressNumber"],
          ClientStreet = OrderInformation["ClientStreet"],
          ClientAttn = OrderInformation["ClientAttn"],
          ClientZIPCode = OrderInformation["ClientZIPCode"],
          ClientCity = OrderInformation["ClientCity"],
          ClientCountry = OrderInformation["ClientCountry"],
          ClientSiteNR = OrderInformation["ClientSiteNR"],
          ClientDepartement = OrderInformation["ClientDepartement"],
          TShirtQuantity = OrderInformation["TShirtQuantity"],
          NumberEndUser = OrderInformation["NumberEndUser"],
          df=df_OrderDetails)

     html_file = open(clientFileName + '.html', 'w')
     html_file.write(outputText)
     html_file.close()
     
     pdfkit.from_file(clientFileName + '.html', clientFileName + '.pdf')

     with open(f"{clientFileName}.pdf","rb") as file :
          st.download_button("Tableau pdf",
                         data= file,
                         file_name=f"{clientFileName}.pdf",
                         
                         )





def downloadZipFile (OrderInformation, OrderDetails):
     
     
     #Required Information to rename the Kore et Client file 
     companyName = OrderInformation["ClientInstitution"]
     orderNumber = OrderInformation["OrderNumber"]

     #Create a Zip file  with Client & Kore file in pdf 
     zipObj = ZipFile('sample.zip','w')


     #Genrate Kore file and crete a PDF file
     html = completeKoreHtml(OrderInformation,OrderDetails)
     koreFileName = f"{companyName}_{orderNumber}_Kore.pdf"
     pdfkit.from_string(html, koreFileName)

     clientFileName = f"{companyName}_{orderNumber}"


     #Compress Client & Kore file in a zip file


     zipObj.write(f"{clientFileName}.pdf")
     zipObj.write(koreFileName)
     zipObj.close()


     #Create a streamlit button to download ZIP file
     with open("sample.zip", "rb") as fp:
          st.download_button(
               '?????? Download Zip file',
               data= fp,
               file_name= f"{orderNumber}.zip"
          )




