

from queue import Empty
import pandas as pd
import numpy as np

import streamlit.components.v1 as components
import pandas as pd

import streamlit as st
from datetime import datetime
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import os, sys, subprocess, platform
import pdfkit



@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def globalContractInformation(typeContrat):

        st.title("Formulaire Client")
        st.header(f"{typeContrat}")

        with st.form ("Form") :
            
                contract_reference = st.text_input("Contract Reference")
                
                contractor_name = st.text_input("Contrcator Name")
                contractor_company = st.text_input("Contractor Company")
                contractor_phoneNumber = st.text_input("Contractor phone number")
                
                number_endUser = st.number_input("Please indicate the total number of end users", 0, 50)
                submite = st.form_submit_button ("Submit")

        return number_endUser,contract_reference,contractor_name,contractor_company,contractor_phoneNumber



def generatorOrder(DataFrame, contract_type,contract_reference,contractor_name,contractor_company,contractor_phoneNumber):

    st.dataframe(DataFrame)
    if platform.system() == "Windows":
        pdfkit_config = pdfkit.configuration(wkhtmltopdf=os.environ.get('WKHTMLTOPDF_BINARY', 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'))

    else:
        WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_PATH', '/app/bin/wkhtmltopdf')],
        stdout=subprocess.PIPE).communicate()[0].strip()
        pdfkit_config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)


       
    env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
    # template = env.get_template("C:/Users/franc/Desktop/python_software/KoreTool/Chronolife Forms/index.html")
    template = env.get_template("index.html")




    html = template.render(
            
            # contract_type = contract_type
            # contractor_company = contractor_company,
            # contract_reference = contract_reference,
            contractor_name = contractor_name,
            # contractor_phoneNumber = contractor_phoneNumber

        )

    # html = html + DataFrame.to_html( justify='center')

 
    # pdf = pdfkit.from_string(html, False,configuration=pdfkit_config
    css = ["df_style.css"]
    pdf = pdfkit.from_file("index.html", css= css,verbose=True)

        
    date = datetime.now()
    
    st.download_button(
            "⬇️ Download PDF order",
            data = pdf,
            file_name=f"Order_Chronolife_{contractor_company}_{contract_type}_{date}.pdf",
            # mime="application/octet-tream"
        )


def matchingFunc ( ludoPoitrine,ludoHanche,ludoTaille):
    file_path = "KoreTool/data/TailleFile.xlsx"
    file_path = "TailleFile.xlsx"
    xls = pd.ExcelFile(file_path)

    # xls = pd.ExcelFile(open('TailleFie.xlsx'))

    size = ["32","34","36","38","40","42","44","46","48","50","52"]   

    dff = pd.read_excel(xls,'TailleMatching')
    
    sizeTable = {
            'Interval Mersure' : ["Poitrine", "Taille","Hanche"],

            '32':[[i for i in np.arange(dff.iloc[0,1],dff.iloc[1,1]+1)],
                    [i for i in np.arange(dff.iloc[2,1],dff.iloc[3,1]+1)],
                    [i for i in np.arange(dff.iloc[4,1],dff.iloc[5,1]+1)]],
           

            '34':[[i for i in np.arange(dff.iloc[0,2],dff.iloc[1,2]+1)],
                    [i for i in np.arange(dff.iloc[2,2],dff.iloc[3,2]+1)],
                    [i for i in np.arange(dff.iloc[4,2],dff.iloc[5,2]+1)]],


            '36':[[i for i in np.arange(dff.iloc[0,3],dff.iloc[1,3]+1)],
                    [i for i in np.arange(dff.iloc[2,3],dff.iloc[3,3]+1)],
                    [i for i in np.arange(dff.iloc[4,3],dff.iloc[5,3]+1)]],

            '38' : [[i for i in np.arange(dff.iloc[0,4],dff.iloc[1,4]+1)],
                    [i for i in np.arange(dff.iloc[2,4],dff.iloc[3,4]+1)],
                    [i for i in np.arange(dff.iloc[4,4],dff.iloc[5,4]+1)]],

            '40' : [[i for i in np.arange(dff.iloc[0,5],dff.iloc[1,5]+1)],
                    [i for i in np.arange(dff.iloc[2,5],dff.iloc[3,5]+1)],
                    [i for i in np.arange(dff.iloc[4,5],dff.iloc[5,5]+1)]],

            '42': [[i for i in np.arange(dff.iloc[0,6],dff.iloc[1,6]+1)],
                    [i for i in np.arange(dff.iloc[2,6],dff.iloc[3,6]+1)],
                    [i for i in np.arange(dff.iloc[4,6],dff.iloc[5,6]+1)]],

            '44' : [[i for i in np.arange(dff.iloc[0,7],dff.iloc[1,7]+1)],
                    [i for i in np.arange(dff.iloc[2,7],dff.iloc[3,7]+1)],
                    [i for i in np.arange(dff.iloc[4,7],dff.iloc[5,7]+1)]],
                    
            '46': [[i for i in np.arange(dff.iloc[0,8],dff.iloc[1,8]+1)],
                    [i for i in np.arange(dff.iloc[2,8],dff.iloc[3,8]+1)],
                    [i for i in np.arange(dff.iloc[4,8],dff.iloc[5,8]+1)]],

            '48': [[i for i in np.arange(dff.iloc[0,9],dff.iloc[1,9]+1)],
                    [i for i in np.arange(dff.iloc[2,9],dff.iloc[3,9]+1)],
                    [i for i in np.arange(dff.iloc[4,9],dff.iloc[5,9]+1)]],

            '50' : [[i for i in np.arange(dff.iloc[0,10],dff.iloc[1,10]+1)],
                    [i for i in np.arange(dff.iloc[2,10],dff.iloc[3,10]+1)],
                    [i for i in np.arange(dff.iloc[4,10],dff.iloc[5,10]+1)]],

            '52' : [[i for i in np.arange(dff.iloc[0,11],dff.iloc[1,11]+1)],
                    [i for i in np.arange(dff.iloc[2,11],dff.iloc[3,11]+1)],
                    [i for i in np.arange(dff.iloc[4,11],dff.iloc[5,11]+1)]],
        }


    df = pd.DataFrame(sizeTable)
    a = 0 
    tailleHancheValid = []
    
    # List Taille valide Hanche
    
    for a in range (len(size)):
        
        test = df[size[a]].iloc[2]
        #print (test)
        b = 0
        
        for b in range (len(test)):
            
            TailleMesure = test[b]
            #print ("Valuer Mesure b",TailleMesure)
                
            if test[b] > ludoHanche :
                            
                
                tailleHancheValid.append(f"{size[a]}")
                break
            else :
                pass
    
    
    # List taille valide Taille
    i = 0
    i_mesure_Taille = 0
    tailleTailleValid  = []
    tailleFinal = 0
    
    for i in range (len(tailleHancheValid)):
        
        test_2 = df[tailleHancheValid[i]].iloc[1]
        #print (test_2)
        
        for i_b in range (len(test_2)) :
            
            TailleMesure = test_2[i_b]
            #print(TailleMesure)
            
            if TailleMesure == ludoTaille :           
               
                tailleTailleValid.append(f"{tailleHancheValid[i]}")
                break
            
    # List taille valide poitrine      
    i = 0
    taillePoitrine = []
    
    if len(tailleTailleValid) == 1 :
        
        print("It's a Match : ",tailleTailleValid[0]) 
        tailleFinal = tailleTailleValid[0]
        
        
    elif len(tailleTailleValid) > 1:
        
        for i in range (len(tailleTailleValid)):
            
            test_3 = df[tailleTailleValid[i]].iloc[0]
            
            for i_c in range (len(test_3)):
                
                Poitrine_mesure = test_3[i_c]
                
                if Poitrine_mesure == ludoPoitrine :
                    
                    taillePoitrine.append(f'{tailleTailleValid[i]}')
                    
        if  len(taillePoitrine) == 0:
                
            tailleFinal = tailleTailleValid[0]
                
        else :
            tailleFinal = taillePoitrine[0]
                   
    else :
        # print ('No Match §')  
        tailleFinal = 'No size match found'          
    
    
    
    return tailleFinal

def matching_taille (dataFrame):

   
    user_size = []
    
    global wording_list_order_ENG
    global wording_list_order_FR
    global wording_list_end_user_info_ENG
    global wording_list_product_info_ENG

    for c  in range (len(dataFrame.index))  :

        poitrine = dataFrame.loc[c]["Chest size (cm)"]
        taille = dataFrame.loc[c]["Waist size (cm)"]
        hanche = dataFrame.loc[c]["Hip size (cm)"]
        user_size.append(matchingFunc(poitrine,hanche,taille))
        c = c+1
   

    dataFrame.insert(loc = 8, column = "T-shirt ize", value = user_size)

    for i in range (len(dataFrame.index)) :
            
            
            if dataFrame.iloc[i,9] == 'No size match found':
          
                st.warning(f"No size detect for User {i+1}") 
        
    return dataFrame


def emptyTextError (my_input,my_indicator):

    if my_input == 0 or my_input == ' ' or my_input == '-' or my_input == None:
        st.warning(f'No {my_indicator} enterred')
    else :
        st.warning ("Hello")

# print (matchingFunc(89,74,78,'homme'))   

     
        
    
            
    
