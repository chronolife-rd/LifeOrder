import streamlit as st

import Orderform
import FileGenrator as fg
from tableOrderGenerator import EndUsersOrderGeneration
from OrderToPDF import order_to_PDF
myOrderNumberEndUser,TshirtQ,submit,dicOrder = Orderform.plotOrderInformation()


if ( int(dicOrder["NumberEndUser"]) > 0 ):
    
    EnduserFormSubmit,dicOrderDetail = Orderform.GetEndUserInformationEnglish(dicOrder)

    if EnduserFormSubmit :

        
        fg.DicToDataframePlot(dicOrder,dicOrderDetail)  

        mainDF,main_dic,maindic2 = EndUsersOrderGeneration(dicOrderDetail)        

        order_to_PDF(dicOrder,maindic2,'TestGarminStreamlit')
       
        with open("TestGarminStreamlit.pdf", "rb") as fp:
          st.download_button(
               '⬇️ Download Zip file',
               data= fp,
               file_name= f"TestGarminStreamlit.pdf"
          )






        
        
    





