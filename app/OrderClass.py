import streamlit as st


class Order :
    
    
    def  __init__(self,ReferenceFacture,TShirtQuantity,CompanyName) :

        self.ReferenceFacture = ReferenceFacture
        self.TShirtQuantity = TShirtQuantity
        self.CompanyName = CompanyName


    def plotOrderInformation ():

        st.title("Order form")


        with st.form ("Form") :
            
            leftColOrder,rightColOrder = st.columns(2)
            BillingReference = leftColOrder.text_input("Biling Reference :", "BR-FO-121123")
            PurchaseOrder = rightColOrder.text_input("Purchase Order :", "PO-FO-121123")


            ClientPhoneNumber = leftColOrder.text_input("Contractore Phone Number","06 50 62 93 22",disabled=True)
            ClientmailAdresse = rightColOrder.text_input("E-mail :","francois@inserm.fr",disabled=True)


            ClientInstitution = leftColOrder.text_input("Institution :","INSERM",disabled=True)
            ClientAdresseNumber = leftColOrder.text_input ("Adresse Number :","43 bis",disabled=True)
            ClientStreet = leftColOrder.text_input("Delivery Street:","rue de la république",disabled=True)
            ClientAttn = leftColOrder.text_input("Attn :","None",disabled=True)
            ClientZIPCcode =  leftColOrder.text_input("Delivery ZIPC code :","59700",disabled=True)

            ClientCity =  rightColOrder.text_input("City :","Lille",disabled=True)
            ClientCountry = rightColOrder.text_input("Country","France",disabled=True)
            ClientSiteNR =  rightColOrder.text_input("Site NR","123",disabled=True)
            ClientDepartement = rightColOrder.text_input("Departement", "Cardiologie",disabled=True)            

            
            TShirtQuantity = rightColOrder.number_input("Number of T-shirt to left Order ", self.TShirtQuantity,disabled=True) # COnnécté à la base de données doit on laiser le choix ?
            NumberEndUser = leftColOrder.number_input("Number of End User",5,disabled=True) 

            submite = st.form_submit_button ("Submit")

        
        return NumberEndUser,TShirtQuantity, submite


