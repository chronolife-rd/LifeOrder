import random
import streamlit as st
import pandas as pd
import wording
import random

# global wording_list_order_ENG
# global wording_list_product_info_ENG
# global wording_list_end_user_info_ENG


class EndUserV2 :
    
    def __init__(self,Number, Date, ContratType ) :

        self.Number = Number
        self.Date = Date
        self.ContratType = ContratType

    
    def plotData (self,numbertoPlot) :
        a = 0
        global endUser_submite

        global wording_list_order_ENG
        global wording_list_order_FR
        global wording_list_end_user_info_ENG
        global wording_list_product_info_ENG

        obligatoire = " *"

        wording_list_order_ENG = [
            #Order Information 
            'Vente',
            'Location'


        ]

        wording_list_order_FR = [

        ]

        wording_list_end_user_info_ENG = [

             #End User information
            "test",#0
            "End user ID", #1
            "Title",#2
            "End User First Name", #3
            "End User Last Name", #4
            "End User phone number", #5
            'End User Country', #6

            "End User Address line 1", #7
            "End User Address line 2", #8
            "End User Postal/Zip code", #9
            "End User Town/City", #10
            
            
            "Chest size (cm)", #11
            "Waist size (cm)", #12
            "Hip size (cm)", #13

            #Element rajouté
            "End User mail"#14


        ]

        wording_list_product_info_ENG = [

             #Product Information
            'Choose product', #0
            'Number of Product', #1
            'Add End User Smartphone', #2
            "Adaptateur contry type", #3
            


        ]




        sexe_list = []
        poitrine_list = []
        Adapateur_list = []
        Ttaille_list = []
        Thanche_liste = []
        adresse_list = []
        endUser_id_liste = []

        product_list =[]

        #Pour Achat
        nb_tshrirt_list = []
        
        complement_list = []
        code_postal_list = []
        ville_list = []
        pays_list =  []
        telephone_list = [] 
        smartphone_list = []  

        firstName_list = []
        lastName_list = []  

        mail_list = []        
        
        EndUser_form  = st.form( f"End User : {self.Number}") 


        while a <= numbertoPlot -1 :

            a = a+1
       
            EndUser_form.write('---')
            EndUser_form.header(f"Form of end-user {a}")
            
     
            # End User specification 
            
            col1,col2 = EndUser_form.columns(2)
            endUser_sexe = col1.selectbox(
                wording_list_end_user_info_ENG[2], 
                ("-","Ms","Mr"),key = f"{a} {wording_list_end_user_info_ENG[2]}")
            
            col2_1_1,col2_1_2 = EndUser_form.columns(2)
            enduser_fisrtName = col2_1_1.text_input(wording_list_end_user_info_ENG[3],key = f"{a} {wording_list_end_user_info_ENG[3]}")
            enduser_lastName = col2_1_2.text_input(wording_list_end_user_info_ENG[4],key = f"{a} {wording_list_end_user_info_ENG[4]}")
            endUser_tel = col2_1_1.text_input(wording_list_end_user_info_ENG[5],key = f"{a} {wording_list_end_user_info_ENG[5]}")
            endUser_mail = col2_1_2.text_input(wording_list_end_user_info_ENG[14],key = f"{a} {wording_list_end_user_info_ENG[14]}")
            

            col2_1,col2_2,col2_3 = EndUser_form.columns(3)   
            

            endUser_adresse1 = col2_1.text_input(wording_list_end_user_info_ENG[7],key = f"{a} {wording_list_end_user_info_ENG[7]}")
            endUser_adresse2 = col2_2.text_input(wording_list_end_user_info_ENG[8],key = f"{a} {wording_list_end_user_info_ENG[8]}")
           
            
            endUser_codePostal = col2_3.text_input(wording_list_end_user_info_ENG[9],key = f"{a} {wording_list_end_user_info_ENG[9]}")
            endUser_ville = col2_2.text_input(wording_list_end_user_info_ENG[10],key = f"{a} {wording_list_end_user_info_ENG[10]}")
            
            endUser_pays = col2_3.selectbox(
                            wording_list_end_user_info_ENG[6],
                            ('-','England','France', 'Germany'),key = f"{a} {wording_list_end_user_info_ENG[6]}")

            
            
            #Product spécification 
            
            
            endUser_id = EndUser_form.text_input (wording_list_end_user_info_ENG[1],key = f"{a} {wording_list_end_user_info_ENG[1]}")

            EndUser_form_col1,EndUser_form_col2,EndUser_form_col3 = EndUser_form.columns(3)   
            endUser_Tpoitrine = EndUser_form_col1.number_input(wording_list_end_user_info_ENG[11], 0, 200,key = f"{a} {wording_list_end_user_info_ENG[11]}")
            endUser_Ttaille =  EndUser_form_col2.number_input(wording_list_end_user_info_ENG[12], 0, 200,key = f"{a} {wording_list_end_user_info_ENG[12]}")
            endUser_Thanche =  EndUser_form_col3.number_input(wording_list_end_user_info_ENG[13], 0, 200,key = f"{a} {wording_list_end_user_info_ENG[13]}")
            EndUser_Produit = EndUser_form_col1.selectbox(
                            wording_list_product_info_ENG[0],
                            ("-",'Keesense', 'CST'),key = f"{a} {wording_list_end_user_info_ENG[0]}")
            
            endUser_Adaptateur = EndUser_form_col2.selectbox(wording_list_product_info_ENG[3], ("-","US","EU","UK"),key = f"{a} {wording_list_product_info_ENG[3]}")


            
            



            if self.ContratType == wording_list_order_ENG[0]:

                enduser_Number = EndUser_form_col2.number_input(wording_list_product_info_ENG[1], 0, 200,key = f"{a} {wording_list_product_info_ENG[1]}")
                nb_tshrirt_list.append(enduser_Number)
            
            endUser_smartphone =  EndUser_form_col3.selectbox(
                            wording_list_product_info_ENG[2],
                            ('-','IPhone', 'A51'),key = f"{a} {wording_list_product_info_ENG[2]}")


            #Order detail
            
            sexe_list.append(endUser_sexe)
            Adapateur_list.append(endUser_Adaptateur)
            print(Adapateur_list)
            poitrine_list.append(endUser_Tpoitrine)
            Ttaille_list.append(endUser_Ttaille)
            Thanche_liste.append(endUser_Thanche)
            endUser_id_liste.append(endUser_id)
            product_list.append(EndUser_Produit)

            smartphone_list.append(endUser_smartphone)
            mail_list.append(endUser_mail)



            #End User information
            firstName_list.append(enduser_fisrtName)
            lastName_list.append(enduser_lastName)

            telephone_list.append(endUser_tel)
            adresse_list.append(endUser_adresse1)
            complement_list.append(endUser_adresse2)
            code_postal_list.append(endUser_codePostal)
            ville_list.append(endUser_ville)
            pays_list.append(endUser_pays)

            
        if self.ContratType == wording_list_order_ENG[1]:

        
            data = {
            wording_list_end_user_info_ENG[3]:firstName_list,
            wording_list_end_user_info_ENG[4]: lastName_list,
            wording_list_end_user_info_ENG[1]:endUser_id_liste,
            #A modifier pour title
            wording_list_end_user_info_ENG[2]:sexe_list,
            
            "Product":product_list,        
            wording_list_end_user_info_ENG[11]:poitrine_list,
            wording_list_end_user_info_ENG[12]:Ttaille_list,
            wording_list_end_user_info_ENG[13]:Thanche_liste,
            wording_list_product_info_ENG[3]:Adapateur_list,
            "End User Smartphone":smartphone_list,
             

            wording_list_end_user_info_ENG [5]: telephone_list,
            wording_list_end_user_info_ENG [14]: mail_list,

            wording_list_end_user_info_ENG[7]:adresse_list,
            wording_list_end_user_info_ENG[8] : complement_list,
            wording_list_end_user_info_ENG[9]: code_postal_list,
            wording_list_end_user_info_ENG[10]: ville_list,
            wording_list_end_user_info_ENG[6]: pays_list
            }


        else :

            data = {
            wording_list_end_user_info_ENG[3]:firstName_list,
            wording_list_end_user_info_ENG[4]: lastName_list,
            wording_list_end_user_info_ENG[1]:endUser_id_liste,
            wording_list_end_user_info_ENG[2]:sexe_list,

            #Achat
            wording_list_product_info_ENG[1]:nb_tshrirt_list,
            
            "Product":product_list,        
            wording_list_end_user_info_ENG[11]:poitrine_list,
            wording_list_end_user_info_ENG[12]:Ttaille_list,
            wording_list_end_user_info_ENG[13]:Thanche_liste,
            wording_list_product_info_ENG[3]:Adapateur_list,
            "End User Smartphone":smartphone_list,
             

            wording_list_end_user_info_ENG [5]: telephone_list,
            wording_list_end_user_info_ENG [14]: mail_list,

            wording_list_end_user_info_ENG[7]:adresse_list,
            wording_list_end_user_info_ENG[8] : complement_list,
            wording_list_end_user_info_ENG[9]: code_postal_list,
            wording_list_end_user_info_ENG[10]: ville_list,
            wording_list_end_user_info_ENG[6]: pays_list
            }

        
       
        df = pd.DataFrame(data)
    
        endUser_submite = EndUser_form.form_submit_button("Submit")
        return df,endUser_submite
       