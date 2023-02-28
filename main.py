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



if __name__ == '__main__':

    my_flowables = []
    
    df_data  = {
        # "EndUserID":["","EZPs23",""],
        "Reference":["NEX -TSH-1-01-A32","NEX -TSH-1-01-A34","NEX -TSH-1-01-A36"],
        "Description":['CST T-shirt Size 32','CST T-shirt Size 34','CST T-shirt Size 36'],
        "Quantity": [2,3,1]
    }

    my_df = pd.DataFrame(df_data)


    my_data = [['End User XXX','',''],
            ['Reference','Description','Quantity'],
            ['col_{}'.format(x) for x in range(1, 4)],
            [str(x) for x in range(1, 4)],
            ['a', 'b', 'c'],
            ]
    
    my_main_list = endUserListGenerator("eSar23a",my_df)
    
    my_doc = create_PDF(name="test1")

    my_table = simple_table_with_style(my_main_list)
    my_table2 = simple_table_with_style(my_data)

    my_flowables = add_table_to_PDF(my_table,my_flowables)
    
    for i in range (5):
        my_flowables = add_table_to_PDF(my_table,my_flowables)
    

    
    generate_PDF(my_doc,my_flowables)