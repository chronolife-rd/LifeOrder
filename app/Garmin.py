import streamlit as st

import Orderform
import FileGenrator as fg
import pandas as pd

myOrderNumberEndUser,TshirtQ,submit,dicOrder = Orderform.plotOrderInformation()


def EndUsersOrderGeneration (dic):

    mainDF = pd.DataFrame(columns=["endUserId","Reference",'Description','Quantity'])

    for i in range (1,len(dic)+1):
        
        endUserId = dic[f"End user {i}"]["EndUserID"]

        # Calule de lataille t-shirt et sélction de la référence (CST ou Keesense)
        endUserSize = dic[f"End user {i}"]["EndUserReferenceSize"]
        endUserTshirtRefrence = f'NEX -TSH-1-01-{endUserSize}'
        endUserTshirtDescription = f'CST T-shirt Size {endUserSize}'
        endUserTshirtQuantity = dic[f"End user {i}"]["EndUserTShirtQuantity"]

        mainDF = mainDF.append({'endUserId':endUserId,
                       "Reference":endUserTshirtRefrence,
                       'Description':endUserTshirtDescription,
                       'Quantity':endUserTshirtQuantity},
                       ignore_index = True
                       )
        
        # Choix de la langue du guide d'utilsiation

        endUserLanguage = dic[f"End user {i}"]["EndUserSpeakingLanguge"]
        endUserIFUQuantity = 1
        endUserQSGQuantity = 1


        if endUserLanguage == "English":
            endUserIFURefrence = "NEX-0001-LBL-07"
            endUserIFUDescription = "CST Instruction for Use – EN"

            mainDF = mainDF.append({'endUserId':endUserId,
                       "Reference":endUserIFURefrence,
                       'Description':endUserIFUDescription,
                       'Quantity':endUserIFUQuantity},
                       ignore_index = True
                       )
            
        
        elif endUserLanguage == "Français":
            endUserIFURefrence = "NEX-0014-LBL-09"
            endUserIFUDescription = "CST Instruction for Use – FR"

            mainDF = mainDF.append({'endUserId':endUserId,
                       "Reference":endUserIFURefrence,
                       'Description':endUserIFUDescription,
                       'Quantity':endUserIFUQuantity},
                       ignore_index = True
                       )

        
        if endUserLanguage == "English":
            endUserQSGDescription = "CST Quick Start Guide – EN"
            endUserQSGReference = "NEX-0018-LBL-08"
            mainDF = mainDF.append({'endUserId':endUserId,
                       "Reference":endUserQSGReference,
                       'Description':endUserQSGDescription,
                       'Quantity':endUserQSGQuantity},
                       ignore_index = True
                       )
        
        elif endUserLanguage == "Français":
            endUserQSGDescription = "CST Quick Start Guide – FR"
            endUserQSGReference = "NEX-0017-LBL-08"
            mainDF = mainDF.append({'endUserId':endUserId,
                       "Reference":endUserQSGReference,
                       'Description':endUserQSGDescription,
                       'Quantity':endUserQSGQuantity},
                       ignore_index = True
                       )


        endUserAdaptateur = dic[f"End user {i}"]["EndUserAdaptateur"]
        
        endUserWirelessChargerRefrence = "CHQ-3-01"	
        endUserWirelessChargerDescription = "Wireless Charger"
        endUserWirelessChargerQuantity = 1

# USQ-0-01	USB cable for wireless charger
# PSS-0-01 	Power Supply 
# ASE-0-01	EU adaptor

#         if 
  
         
    st.dataframe(mainDF)
    



if ( int(dicOrder["NumberEndUser"]) > 0 ):
    
    EnduserFormSubmit,dicOrderDetail = Orderform.GetEndUserInformationEnglish(dicOrder)

    if EnduserFormSubmit :

        
        fg.DicToDataframePlot(dicOrder,dicOrderDetail)  


        #Créer fonction de caluler et ajouter la taille des T-shirt dans le df
        #Creer fonctions de génératon des ID
        #Créer fonction d'ajour des ID dans le tablea
        EndUsersOrderGeneration(dicOrderDetail)


        print(dicOrderDetail)        

        fg.downloadKorePDF(dicOrder,dicOrderDetail)
        fg.ClientFileGenerator(dicOrder,dicOrderDetail)

        fg.downloadZipFile(dicOrder,dicOrderDetail)




        
        
    





