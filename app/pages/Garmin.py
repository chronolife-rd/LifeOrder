import streamlit as st

import Orderform
import FileGenrator as fg


myOrderNumberEndUser,TshirtQ,submit,dicOrder = Orderform.plotOrderInformation()

if ( int(dicOrder["NumberEndUser"]) > 0 ):
    
    EnduserFormSubmit,dicOrderDetail = Orderform.GetEndUserInformationEnglish(dicOrder)

    if EnduserFormSubmit :

        
        fg.DicToDataframePlot(dicOrder,dicOrderDetail)  


        #Créer fonction de caluler et ajouter la taille des T-shirt dans le df
        #Creer fonctions de génératon des ID
        #Créer fonction d'ajour des ID dans le tablea
        

        fg.downloadKorePDF(dicOrder,dicOrderDetail)
        fg.ClientFileGenerator(dicOrder,dicOrderDetail)

        fg.downloadZipFile(dicOrder,dicOrderDetail)


        




