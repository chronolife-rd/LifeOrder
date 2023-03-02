# simple_table_with_style.py

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import pandas as pd
# Fonction pour créer une tableau 




# fonction pour mettre les tableau dans le PDF

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

def endUserListGeneratorV2 (endUserId,dic):

    end_user_list = []
    end_user_line = [f'{endUserId}','','']
    description_line = ['Reference','Description','Quantity']

    end_user_list.append(end_user_line)
    end_user_list.append(description_line)
    
    description_line = ['Reference','Description','Quantity']


    df_datamaindic2 = pd.DataFrame.from_dict(dic)

    df_datamaindic2_traspose = df_datamaindic2.transpose()

    refdic_1 = df_datamaindic2_traspose["Reference"][1]
    descriptionDic_1 = df_datamaindic2_traspose["Description"][1]
    quantityDic_1 = df_datamaindic2_traspose["Quantity"][1]

    reflist_1 = list(refdic_1)
    descriptionList_1 = list(descriptionDic_1)
    quantityList_1 = list(quantityDic_1)
    
    for i in range (len(df_datamaindic2_traspose)) :
        
        end_user_list.append([reflist_1[i],descriptionList_1[i],quantityList_1[i]])
        # end_user_list.append(descriptionList_1[i])
        # end_user_list.append(quantityList_1[i])

    return end_user_list



if __name__ == '__main__':
    
    my_flowables = []

    datamaindic2 = {
            1: {'EndUserID': 'ZEpxRz', 
                'Reference': {'CHQ-3-10', 'NEX-0014-LBL-09', 'USQ-0-01', 'NEX-TSH-1-01-1', 'PSS-0-01', 'ASE-0-01', 'NEX-0017-LBL-08'}, 
                'Description': {'Wireless Charger', 'USB cable for wireless charger', 'Power Supply', 'CST T-shirt Size 1', 'CST Quick Start Guide – FR', 'EU adaptor', 'CST Instruction for Use – FR'}, 
                'Quantity': {1,1,1,1,1,1}}, 
            # 2: {'EndUserID': 'ZEpxRz', 'Reference': 
            #     {'CHQ-3-01', 'NEX-0014-LBL-09', 'USQ-0-01', 'NEX-TSH-1-01-1', 'PSS-0-01', 'ASE-0-01', 'NEX-0017-LBL-08'}, 
            #     'Description': {'Wireless Charger', 'USB cable for wireless charger', 'Power Supply', 'CST T-shirt Size 1', 'CST Quick Start Guide – FR', 'EU adaptor', 'CST Instruction for Use – FR'}, 
            #     'Quantity': {1,1,1,1,1,1}}, 
            # 3: {'EndUserID': 'ZEpxRz', 'Reference': 
            #     {'CHQ-3-01', 'NEX-0014-LBL-09', 'USQ-0-01', 'NEX-TSH-1-01-1', 'PSS-0-01', 'ASE-0-01', 'NEX-0017-LBL-08'}, 
            #     'Description': {'Wireless Charger', 'USB cable for wireless charger', 'Power Supply', 'CST T-shirt Size 1', 'CST Quick Start Guide – FR', 'EU adaptor', 'CST Instruction for Use – FR'}, 
            #     'Quantity': {1,1,1,1,1,1}}}
    }
    
    df_data  = {       
            # "EndUserId":" EZPs23",
            "Reference":["NEX -TSH-1-01-A32","NEX -TSH-1-01-A34","NEX -TSH-1-01-A36"],
            "Description":['CST T-shirt Size 32','CST T-shirt Size 24','CST T-shirt Size 36'],
            "Quantity": [2,3,1]

    }


    # datapreparation = pd.json_normalize(df_data)

    

    my_df = pd.DataFrame.from_dict(df_data)



    my_main_list = endUserListGenerator("eSad2eda",my_df)
    
    mainlist2 = endUserListGeneratorV2('Test',datamaindic2)
    
    my_doc = create_PDF(name="test1")

    my_table = simple_table_with_style(mainlist2)

    my_flowables = add_table_to_PDF(my_table,my_flowables)
    
   
    my_flowables = add_table_to_PDF(my_table,my_flowables)
    

    
    generate_PDF(my_doc,my_flowables)