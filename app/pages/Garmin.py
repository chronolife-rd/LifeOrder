import streamlit as st
from pandas import json_normalize
import json
import EndUserForm
import FileGenrator as fg


NumberOfTshirtToOrder = 4

myOrderNumberEndUser,TshirtQ,submit,dicOrder = EndUserForm.plotOrderInformation(NumberOfTshirtToOrder)


if int (myOrderNumberEndUser > 0):
    
    EnduserFormSubmit,DicOrderDetail = EndUserForm.GetEndUserInformationEnglish(myOrderNumberEndUser)

    if EnduserFormSubmit :

        
        dfOrderInformation = fg.DicToDataframePlot(dicOrder)  
        dfOrderDetail = fg.DicToDataframePlot(DicOrderDetail)


        #Créer fonction de caluler et ajouter la taille des T-shirt dans le df
        #Creer fonctions de génératon des ID
        #Créer fonction d'ajour des ID dans le tableau


        fg.downloadKorePDF(dicOrder)


        





