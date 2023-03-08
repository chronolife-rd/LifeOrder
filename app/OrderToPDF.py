# simple_table_with_style.py

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import pandas as pd


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

def globalOrderTableStyle(my_data):
    

    data = my_data
    tblstyle = TableStyle([
        
        ('GRID',(0,0),(-1,-1),0.5,colors.black),
        
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

def globalOrderToTable(globalOrder):
    globalOrderTale = []
    title_line = ['Receiver Information','']


    globalOrderTale.append(title_line)
    globalOrderTale.append(["Institution / Company : ",f"{globalOrder['ClientInstitution']}"])
    globalOrderTale.append(["Required Date",f"{globalOrder['RequiredDate']}"])
    globalOrderTale.append(["Client Phone Number",f"{globalOrder['ClientPhoneNumber']}"])
    globalOrderTale.append(["Client Mail Address",f"{globalOrder['ClientMailAddress']}"])
    globalOrderTale.append(["Billing Reference",f"{globalOrder['BillingReference']}"])
    globalOrderTale.append(["Client Reference",f"{globalOrder['ClientReference']}"])
    globalOrderTale.append(["Number",f"{globalOrder['ClientAddressNumber']}"])
    globalOrderTale.append(["Street",f"{globalOrder['ClientStreet']}"])
    globalOrderTale.append(["Attn",f"{globalOrder['ClientAttn']}"])
    globalOrderTale.append(["Site NR",f"{globalOrder['ClientSiteNR']}"])
    globalOrderTale.append(["ZIP code",f"{globalOrder['ClientZIPCode']}"])
    globalOrderTale.append(["City",f"{globalOrder['ClientCity']}"])
    globalOrderTale.append(["Client Departement",f"{globalOrder['ClientDepartement']}"])
    globalOrderTale.append(["Country",f"{globalOrder['ClientCountry']}"])

    
  
    return globalOrderTale



def endUserListGeneratorV3 (endUserDic,endUserId):
    end_user_list = []

        
    end_user_line = [f'End user ID : {endUserId}','','']
    description_line = ['Reference','Description','Quantity']

    end_user_list.append(end_user_line)
    end_user_list.append(description_line)

    df_endUserOrder = pd.DataFrame(endUserDic)

    refdic_1 = df_endUserOrder["Reference"]
    descriptionDic_1 = df_endUserOrder["Description"]
    quantityDic_1 = df_endUserOrder["Quantity"]

    reflist_1 = list(refdic_1)
    descriptionList_1 = list(descriptionDic_1)
    quantityList_1 = list(quantityDic_1)

    for i in range (len(quantityDic_1)) :
                    
        end_user_list.append([reflist_1[i],descriptionList_1[i],quantityList_1[i]])

   

    return end_user_list

def order_to_PDF (globalOrderJson,orderJsonData,fileName):
    my_flowables = []


    my_doc = create_PDF(name=f"{fileName}")

    my_globalOrderTable = globalOrderToTable(globalOrderJson)
    my_globalOrderTable = globalOrderTableStyle(my_globalOrderTable)
    my_flowables = add_table_to_PDF(my_globalOrderTable,my_flowables)
    
    
    for i in range (1,len(orderJsonData)+1):
        my_data = endUserListGeneratorV3(orderJsonData[i],orderJsonData[i]["EndUserID"])
        my_table = simple_table_with_style(my_data)
        my_flowables = add_table_to_PDF(my_table,my_flowables)
    
        
    generate_PDF(my_doc,my_flowables)


    
    


if __name__ == '__main__':
    
    
    datamaindic3 = {
                1: {'EndUserID': 'Test1', 
                    'Reference': {'Tshirt': 'NEX-TSH-1-01-1', 'IFU': 'NEX-0014-LBL-09', 'QSG': 'NEX-0017-LBL-08', 'WC': 'CHQ-3-01', 'USB': 'USQ-0-01', 'PS': 'PSS-0-01', 'Adapt': 'ASE-0-01'}, 
                    'Description': {'Tshirt': 'CST T-shirt Size 1', 'IFU': 'CST Instruction for Use – FR', 'QSG': 'CST Quick Start Guide – FR', 'WC': 'Wireless Charger', 'USB': 'USB cable for wireless charger', 'PS': 'Power Supply', 'Adapt': 'EU adaptor'}, 
                    'Quantity': {'Tshirt': 2, 'IFU': 1, 'QSG': 1, 'WC': 1, 'USB': 1, 'PS': 1, 'Adapt': 1}}, 
                2: {'EndUserID': 'Test2', 
                    'Reference': {'Tshirt': 'NEX-TSH-1-01-1', 'IFU': 'NEX-0014-LBL-09', 'QSG': 'NEX-0017-LBL-08', 'WC': 'CHQ-3-01', 'USB': 'USQ-0-01', 'PS': 'PSS-0-01', 'Adapt': 'ASE-0-01'}, 
                    'Description': {'Tshirt': 'CST T-shirt Size 1', 'IFU': 'CST Instruction for Use – FR', 'QSG': 'CST Quick Start Guide – FR', 'WC': 'Wireless Charger', 'USB': 'USB cable for wireless charger', 'PS': 'Power Supply', 'Adapt': 'EU adaptor'}, 
                    'Quantity': {'Tshirt': 2, 'IFU': 1, 'QSG': 1, 'WC': 1, 'USB': 1, 'PS': 1, 'Adapt': 1}},

                3: {'EndUserID': 'Test3', 
                    'Reference': {'Tshirt': 'NEX-TSH-1-01-1', 'IFU': 'NEX-0014-LBL-09', 'QSG': 'NEX-0017-LBL-08', 'WC': 'CHQ-3-01', 'USB': 'USQ-0-01', 'PS': 'PSS-0-01', 'Adapt': 'ASE-0-01'}, 
                    'Description': {'Tshirt': 'CST T-shirt Size 1', 'IFU': 'CST Instruction for Use – FR', 'QSG': 'CST Quick Start Guide – FR', 'WC': 'Wireless Charger', 'USB': 'USB cable for wireless charger', 'PS': 'Power Supply', 'Adapt': 'EU adaptor'}, 
                    'Quantity': {'Tshirt': 2, 'IFU': 1, 'QSG': 1, 'WC': 1, 'USB': 1, 'PS': 1, 'Adapt': 1}},
                    
                4: {'EndUserID': 'Test3', 
                    'Reference': {'Tshirt': 'NEX-TSH-1-01-1', 'IFU': 'NEX-0014-LBL-09', 'QSG': 'NEX-0017-LBL-08', 'WC': 'CHQ-3-01', 'USB': 'USQ-0-01', 'PS': 'PSS-0-01', 'Adapt': 'ASE-0-01'}, 
                    'Description': {'Tshirt': 'CST T-shirt Size 1', 'IFU': 'CST Instruction for Use – FR', 'QSG': 'CST Quick Start Guide – FR', 'WC': 'Wireless Charger', 'USB': 'USB cable for wireless charger', 'PS': 'Power Supply', 'Adapt': 'EU adaptor'}, 
                    'Quantity': {'Tshirt': 2, 'IFU': 1, 'QSG': 1, 'WC': 1, 'USB': 1, 'PS': 1, 'Adapt': 1}}
          
                }

    
    
    order_to_PDF(datamaindic3,'TestGarmin') 
    
