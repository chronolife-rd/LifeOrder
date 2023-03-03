


import streamlit as st
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def create_PDF (name):
    doc = SimpleDocTemplate(
            f"{name}.pdf",
            pagesize=letter,
            )

    return doc


def simple_table_with_style(my_data):
    

    data = my_data

    tblstyle = TableStyle([
        
        ('GRID',(0,0),(-1,-1),0.5,colors.black),
        ('SPAN',(0,0),(2,0)),
        ('ALIGN',(0,0),(2,0),'CENTER')
        
        ])

    tbl = Table(data)
    tbl.setStyle(tblstyle)
    tbl.spaceAfter = 40

    return tbl
   

def add_table_to_PDF (tableau,flowables):

    flowables.append(tableau)

    return flowables
    


def generate_PDF (doc,flowables):

    doc.build(flowables)

def endUserListGenerator (endUserId,dfEndUser):

    end_user_list = []
    end_user_line = [f'{endUserId}','','']
    description_line = ['Reference','Description','Quantity']

    end_user_list.append(end_user_line)
    end_user_list.append(description_line)

    dfEndUser = dfEndUser.values.tolist()
    for i in range (len(dfEndUser)):
        end_user_list.append(dfEndUser[i])
    
    return end_user_list


def EndUsersOrderGeneration (dic):

    mainDF = pd.DataFrame(columns=["endUserId","Reference",'Description','Quantity'])
    maindic = {}
    maindic2 = {}
    for i in range (1,len(dic)+1):
        
        endUserId = dic[f"End user {i}"]["EndUserID"]
        endUserLanguage = dic[f"End user {i}"]["EndUserSpeakingLanguge"]
        endUserAdaptateur = dic[f"End user {i}"]["EndUserAdaptateur"]
        
        endUserDic = {}

        enduserdic2 = {}

        endUserSize = dic[f"End user {i}"]["EndUserReferenceSize"]
        
        endUserTshirtRefrence = f'NEX-TSH-1-01-{endUserSize}'
        endUserTshirtDescription = f'CST T-shirt Size {endUserSize}'
        endUserTshirtQuantity = dic[f"End user {i}"]["EndUserTShirtQuantity"]

        mainDF = mainDF.append({'endUserId':endUserId,
                       "Reference":endUserTshirtRefrence,
                       'Description':endUserTshirtDescription,
                       'Quantity':endUserTshirtQuantity},
                       ignore_index = True
                       ) 


        if endUserLanguage == "English":
            endUserIFURefrence = "NEX-0001-LBL-07"
            endUserIFUDescription = "CST Instruction for Use – EN"
            endUserIFUQuantity = 1

            mainDF = mainDF.append({'endUserId':endUserId,
                       "Reference":"NEX-0001-LBL-07",
                       'Description':"CST Instruction for Use – EN",
                       'Quantity':1},
                       ignore_index = True
                       )
            
        
        else :
            endUserIFURefrence = "NEX-0014-LBL-09"
            endUserIFUDescription = "CST Instruction for Use – FR"
            endUserIFUQuantity = 1

            mainDF = mainDF.append({'endUserId':endUserId,
                       "Reference":"NEX-0014-LBL-09",
                       'Description':"CST Instruction for Use – FR",
                       'Quantity':1},
                       ignore_index = True
                       )
            
        


        # Choix du QSG
        if endUserLanguage == "English":
            
            endUserQSGDescription = "CST Quick Start Guide – EN"
            endUserQSGReference = "NEX-0018-LBL-08"
            endUserQSGQuantity = 1

            mainDF = mainDF.append({'endUserId':endUserId,
                       "Reference":"NEX-0018-LBL-08",
                       'Description':"CST Quick Start Guide – EN",
                       'Quantity':1},
                       ignore_index = True
                       )
        
        else :
            endUserQSGDescription = "CST Quick Start Guide – FR"
            endUserQSGReference = "NEX-0017-LBL-08"
            endUserQSGQuantity = 1

            mainDF = mainDF.append({'endUserId':endUserId,
                       "Reference":"NEX-0017-LBL-08",
                       'Description':"CST Quick Start Guide – FR",
                       'Quantity':1},
                       ignore_index = True
                       )

        endUserWCDescription = "Wireless Charger"
        endUserWCReference = "CHQ-3-01"
        endUserWCQuantity = 1

        mainDF = mainDF.append({'endUserId':endUserId,
                       "Reference":"CHQ-3-01",
                       'Description':"Wireless Charger",
                       'Quantity':1},
                       ignore_index = True
                       )
        
        endUserUSBDescription = "USB cable for wireless charger"
        endUserUSBReference = "USQ-0-01"
        endUserUSBQuantity = 1

        mainDF = mainDF.append({'endUserId':endUserId,
                       "Reference":"USQ-0-01",
                       'Description':"USB cable for wireless charger",
                       'Quantity':1},
                       ignore_index = True
                       )
        
        endUserPSDescription = "Power Supply"
        endUserPSReference = "PSS-0-01"
        endUserPSQuantity = 1
  
        mainDF = mainDF.append({'endUserId':endUserId,
                       "Reference":"PSS-0-01",
                       'Description':"Power Supply",
                       'Quantity':1},
                       ignore_index = True
                       )

        
        if endUserAdaptateur == "US":
            endUserAdaptateurReference = "ASU-0-01"
            endUserAdaptateurDescription = "US adaptor"
            endUserAdaptateurQuantity = 1

            mainDF = mainDF.append({'endUserId':endUserId,
                       "Reference":"ASU-0-01",
                       'Description':"US adaptor",
                       'Quantity':1},
                       ignore_index = True
                       )

        else :
            endUserAdaptateurReference = "ASE-0-01"
            endUserAdaptateurDescription = "EU adaptor"
            endUserAdaptateurQuantity = 1

            mainDF = mainDF.append({'endUserId':endUserId,
                       "Reference":"ASE-0-01",
                       'Description':"EU adaptor",
                       'Quantity':1},
                       ignore_index = True
                       )
        
        
        enduserdic2["EndUserID"] = endUserId    
            
    

        enduserdic2["Reference"] = {"Tshirt":endUserTshirtRefrence,
                                   "IFU":endUserIFURefrence,
                                   "QSG":endUserQSGReference,
                                   "WC":endUserWCReference,
                                   "USB":endUserUSBReference,
                                   "PS":endUserPSReference,
                                   "Adapt":endUserAdaptateurReference
                                   }
        
        enduserdic2["Description"]= {"Tshirt":endUserTshirtDescription,
                                   "IFU":endUserIFUDescription,
                                   "QSG":endUserQSGDescription,
                                   "WC":endUserWCDescription,
                                   "USB":endUserUSBDescription,
                                   "PS":endUserPSDescription,
                                   "Adapt":endUserAdaptateurDescription}
        
        enduserdic2["Quantity"]= {"Tshirt":endUserTshirtQuantity,
                                   "IFU":endUserIFUQuantity,
                                   "QSG":endUserQSGQuantity,
                                   "WC":endUserWCQuantity,
                                   "USB":endUserUSBQuantity,
                                   "PS":endUserPSQuantity,
                                   "Adapt":endUserAdaptateurQuantity}
        


        
        maindic[i]=endUserDic
        maindic2[i]=enduserdic2


    return mainDF,maindic,maindic2

