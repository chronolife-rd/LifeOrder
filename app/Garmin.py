import streamlit as st

import Orderform
import FileGenrator as fg
import pandas as pd
from tableOrderGenerator import EndUsersOrderGeneration
import json

myOrderNumberEndUser,TshirtQ,submit,dicOrder = Orderform.plotOrderInformation()


if ( int(dicOrder["NumberEndUser"]) > 0 ):
    
    EnduserFormSubmit,dicOrderDetail = Orderform.GetEndUserInformationEnglish(dicOrder)

    if EnduserFormSubmit :

        
        fg.DicToDataframePlot(dicOrder,dicOrderDetail)  

        mainDF,main_dic,maindic2 = EndUsersOrderGeneration(dicOrderDetail)
        st.dataframe(mainDF)
        
        
        st.write(maindic2)

        print(maindic2)
    


        fg.downloadKorePDF(dicOrder,dicOrderDetail)
        fg.ClientFileGenerator(dicOrder,dicOrderDetail)

        fg.downloadZipFile(dicOrder,dicOrderDetail)




        
        
    





