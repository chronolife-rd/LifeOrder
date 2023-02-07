import streamlit as st

import EndUserForm
import FileGenrator as fg


myOrderNumberEndUser,TshirtQ,submit,dicOrder = EndUserForm.plotOrderInformation()

if ( int(dicOrder["Order Information"]["NumberEndUser"]) > 0 ):
    
    EnduserFormSubmit,dicOrderDetail = EndUserForm.GetEndUserInformationEnglish(dicOrder)

    if EnduserFormSubmit :

        
        dfOrderInformation = fg.DicToDataframePlot(dicOrder)  
        dfOrderDetail = fg.DicToDataframePlot(dicOrderDetail)


        #Créer fonction de caluler et ajouter la taille des T-shirt dans le df
        #Creer fonctions de génératon des ID
        #Créer fonction d'ajour des ID dans le tablea
        
        st.write()

        fg.downloadKorePDF(dicOrder,dicOrderDetail)
        fg.ClientFileGenerator(dicOrder,dicOrderDetail)


        




