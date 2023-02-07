
import streamlit as st
import pandas as pd
import random
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from  datetime import date
import pdfkit


def plotOrderInformation ():

        st.title("Order form")

        Orderdate = date.today()
        Orderdate = Orderdate.strftime("%d/%m/%Y")

        with st.form ("Form") :
            
            leftColOrder,rightColOrder = st.columns(2)
            BillingReference = leftColOrder.text_input("Biling Reference :")
            PurchaseOrder = rightColOrder.text_input("Purchase Order :", "PO-FO-121123")

            RequiredDate = leftColOrder.text_input("Required Order Date:",f"{Orderdate}",disabled=True)


            ClientPhoneNumber = leftColOrder.text_input("Contractore Phone Number","06 50 62 93 22",disabled=True)
            ClientMailAddress = rightColOrder.text_input("E-mail :","francois@inserm.fr",disabled=True)


            ClientInstitution = leftColOrder.text_input("Institution :","INSERM",disabled=True)
            ClientAddressNumber = leftColOrder.text_input ("Adresse Number :","43 bis",disabled=True)
            ClientStreet = leftColOrder.text_input("Delivery Street:","rue de la république",disabled=True)
            ClientAttn = leftColOrder.text_input("Attn :","None",disabled=True)
            ClientZIPCcode =  leftColOrder.text_input("Delivery ZIPC code :","59700",disabled=True)

            ClientCity =  rightColOrder.text_input("City :","Lille",disabled=True)
            ClientCountry = rightColOrder.text_input("Country","France",disabled=True)
            ClientSiteNR =  rightColOrder.text_input("Site NR","123",disabled=True)
            ClientDepartement = rightColOrder.text_input("Departement", "Cardiologie",disabled=True)            

            
            TShirtQuantity = rightColOrder.number_input("Number of T-shirt to left Order ",  10 ,disabled=True) # COnnécté à la base de données doit on laiser le choix ?
            NumberEndUser = leftColOrder.number_input("Number of End User",0) 
            submite = st.form_submit_button ("Submit")
           
           
            OrderDic = {
                 
                 "Order Information": {
                 
                    "BillingReference":BillingReference,
                    "PurchaseOrder": PurchaseOrder,
                    "RequiredDate":RequiredDate,
                    
                    "ClientPhoneNumber": ClientPhoneNumber,
                    "ClientMailAddress":ClientMailAddress,
                    "ClientInstitution":ClientInstitution,
                    "ClientAddressNumber":ClientAddressNumber,
                    "ClientStreet":ClientStreet,
                    "ClientAttn":ClientAttn,
                    "ClientZIPCode":ClientZIPCcode,
                    "ClientCity":ClientCity,
                    "ClientCountry":ClientCountry,
                    "ClientSiteNR":ClientSiteNR,
                    "ClientDepartement":ClientDepartement,

                    "TShirtQuantity":TShirtQuantity,
                    "NumberEndUser":NumberEndUser,
                 
                 }
               
            }

            

        
        return NumberEndUser,TShirtQuantity, submite,OrderDic
     
def GetEndUserInformationEnglish (OrderDic):
        EndUserQuantity = OrderDic["Order Information"]["NumberEndUser"]
        
        if ( EndUserQuantity > 0) :
            EndUser_form  = st.form( f"End User : {EndUserQuantity}") 

            GlobalDic = {}

            for i in range (1,int(EndUserQuantity)+1) :
                
                EndUser_form.write('---')
                EndUser_form.header(f"Form of end-user {i}")

                EndUserFormRightCol,EndUserFormLeftCol = EndUser_form.columns(2)
                EndUserGender = EndUserFormRightCol.selectbox("Gender", 
                            ("-","Ms","Mr"),key = f"{i} Gender")

                
                # EndUserFirstName = EndUserFormRightCol.text_input("End User First Name :","François",key = f"{i} EndUserFirstName")
                # EndUserLastName = EndUserFormLeftCol.text_input("End User Last Name :","Ottavi",key = f"{i} EndUserLastName")
                EndUserID = EndUserFormLeftCol.text_input("End User ID :","ZEpxRz",key = f"{i} EndUserID")
                 
                EndUserSpeakingLanguge = EndUserFormLeftCol.selectbox("Speaking Language :", 
                            ("-","English","Français"),key = f"{i} EndUserSpeakingLanguge")
                
                # ------------- Device ----------------
                EndUserTshirtQuantity = EndUserFormRightCol.number_input("Quantity of T-shirt for this End User :",1,key = f"{i} EndUserTshirtQuantity")
                EndUserChestTopSize = EndUserFormRightCol.number_input("End User chest top size :",1,key = f"{i} EndUserChestTopSize")
                EndUserChestNippleSize = EndUserFormRightCol.number_input("End User chest Nipple size :",1,key = f"{i} EndUserChestNippleSize")
                EndUserWaistSize = EndUserFormRightCol.number_input("End User EndUserWaistSize size :",1,key = f"{i} EndUserWaistSize")
                EndUserHipsSize = EndUserFormRightCol.number_input("End User EndUserHipsSize size :",1,key = f"{i} EndUserHipsSize")
                EndUserReferenceSize = EndUserFormRightCol.number_input("End User EndUserReferenceSize size :",1,key = f"{i} EndUserReferenceSize")
                EndUserAdaptateur = EndUserFormRightCol.selectbox("Adapteur Type :", 
                            ("-","US","Europe"),key = f"{i} EndUserAdaptateur")


                endUserDict = {
                    
                    f"End user {i}" : {
                    "Gendre":EndUserGender,

                    "EndUserID":EndUserID,
                    # "EndUserFirstName":EndUserFirstName,
                    # "EndUserLastName":EndUserLastName,
                    "EndUserSpeakingLanguge":EndUserSpeakingLanguge,

                    "EndUserTShirtQuantity": EndUserTshirtQuantity,
                    # "EndUserChestTopSize":EndUserChestTopSize,
                    # "EndUserChestNippleSize":EndUserChestNippleSize,
                    # "EndUserWaistSize":EndUserWaistSize,
                    # "EndUserHipsSize":EndUserHipsSize,
                    # "EndUserReferenceSize":EndUserReferenceSize,

                    "EndUserAdaptateur":EndUserAdaptateur,

                    }

                }


                GlobalDic.update(endUserDict)
                    
            submite = EndUser_form.form_submit_button ("Submit")
            return submite,GlobalDic
    
        else :
            
            st.warning("Pas end user séléctionné")
            submite = False
            df = []
            return submite,df





    