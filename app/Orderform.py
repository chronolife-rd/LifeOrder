
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
            
            globalOrder1,globalOrder2 , globalOrder3= st.columns(3)
            BillingReference = globalOrder1.text_input("Biling Reference :")
            ClientReference = globalOrder1.text_input("Client Reference :", "PO-FO-121123")

            RequiredDate = globalOrder1.text_input("Required Order Date:",f"{Orderdate}")


            ClientPhoneNumber = globalOrder1.text_input("Client Phone Number","06 50 62 93 22")
            ClientMailAddress = globalOrder1.text_input("Client E-mail :","francois@inserm.fr")


            ClientInstitution = globalOrder2.text_input("Institution / Company :","INSERM")
            ClientAddressNumber = globalOrder2.text_input ("Adresse Number :","43 bis")
            ClientStreet = globalOrder2.text_input("Delivery Street:","rue de la république")
            ClientAttn = globalOrder2.text_input("Attn :","None")
            ClientZIPCcode =  globalOrder2.text_input("Delivery ZIPC code :","59700")

            ClientCity =  globalOrder2.text_input("City :","Lille")
            ClientCountry = globalOrder2.text_input("Country","France")
            ClientSiteNR =  globalOrder2.text_input("Site NR","123")
            ClientDepartement = globalOrder2.text_input("Departement", "Cardiologie")            

            
            TShirtQuantity = globalOrder3.number_input("Number of T-shirt to left Order ",  10) # COnnécté à la base de données doit on laiser le choix ?
            NumberEndUser = globalOrder3.number_input("Number of End User",0) 
            submite = st.form_submit_button ("Submit")
           
           
            OrderDic = {
                 
                 
                 
                    "BillingReference":BillingReference,
                    "ClientReference": ClientReference,
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

            

        
        return NumberEndUser,TShirtQuantity, submite,OrderDic
     
def GetEndUserInformationEnglish (OrderDic):
        EndUserQuantity = OrderDic["NumberEndUser"]
        
        if ( EndUserQuantity > 0) :
            EndUser_form  = st.form( f"End User : {EndUserQuantity}") 

            GlobalDic = {}

            for i in range (1,int(EndUserQuantity)+1) :
                
                EndUser_form.write('---')
                EndUser_form.header(f"Form of end-user {i}")

                EndUserFormRightCol,EndUserFormLeftCol = EndUser_form.columns(2)
                EndUserGender = EndUserFormRightCol.selectbox("Gender", 
                            ("-","Female","Male"),key = f"{i} Gender")

                
                # EndUserFirstName = EndUserFormRightCol.text_input("End User First Name :","François",key = f"{i} EndUserFirstName")
                # EndUserLastName = EndUserFormLeftCol.text_input("End User Last Name :","Ottavi",key = f"{i} EndUserLastName")
                EndUserID = EndUserFormRightCol.text_input("End User ID :","ZEpxRz",key = f"{i} EndUserID")
                 
                EndUserSpeakingLanguge = EndUserFormRightCol.selectbox("Speaking Language :", 
                            ("-","English","Français"),key = f"{i} EndUserSpeakingLanguge")
                
                # ------------- Device ----------------
                EndUserTshirtQuantity = EndUserFormLeftCol.number_input("Quantity of T-shirt for this End User :",1,key = f"{i} EndUserTshirtQuantity")
                EndUserChestTopSize = EndUserFormLeftCol.number_input("End User chest top size :",1,key = f"{i} EndUserChestTopSize")
                EndUserChestNippleSize = EndUserFormLeftCol.number_input("End User chest Nipple size :",1,key = f"{i} EndUserChestNippleSize")
                EndUserWaistSize = EndUserFormLeftCol.number_input("End User EndUserWaistSize size :",1,key = f"{i} EndUserWaistSize")
                EndUserHipsSize = EndUserFormLeftCol.number_input("End User EndUserHipsSize size :",1,key = f"{i} EndUserHipsSize")
                EndUserReferenceSize = EndUserFormRightCol.number_input("End User EndUserReferenceSize size :",1,key = f"{i} EndUserReferenceSize")
                EndUserAdaptateur = EndUserFormRightCol.selectbox("Adapteur Type :", 
                            ("Europe","US"),key = f"{i} EndUserAdaptateur")


                endUserDict = {
                    
                    f"End user {i}" : {
                     
                    # "End user reference ": f"End user {i}",
                                    
                    "EndUserID":EndUserID,
                    "Gendre":EndUserGender,

                    # "EndUserFirstName":EndUserFirstName,
                    # "EndUserLastName":EndUserLastName,
                    "EndUserSpeakingLanguge":EndUserSpeakingLanguge,

                    "EndUserTShirtQuantity": EndUserTshirtQuantity,
                    # "EndUserChestTopSize":EndUserChestTopSize,
                    # "EndUserChestNippleSize":EndUserChestNippleSize,
                    # "EndUserWaistSize":EndUserWaistSize,
                    # "EndUserHipsSize":EndUserHipsSize,
                    "EndUserReferenceSize":EndUserReferenceSize,

                    "EndUserAdaptateur":EndUserAdaptateur,

                    }

                }


                GlobalDic.update(endUserDict)
                    
            submite = EndUser_form.form_submit_button ("Submit")
            return submite,GlobalDic
    
        else :
            
            submite = False
            df = []
            return submite,df





    