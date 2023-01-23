import streamlit as st
import sys

sys.path.insert(0, '/app/pages')
from  AlgoMatch import matching_taille,generatorOrder,globalContractInformation

import EndUserClass

contract_type = 'Vente'

st.set_page_config(page_title="Commande Client")

number_endUser,contract_reference,contractor_name,contractor_company,contractor_phoneNumber = globalContractInformation(contract_type)

if int(number_endUser) > 0 :
    
    dataF,endUser_submite = EndUserClass.EndUserV2(2,10,contract_type).plotData(int(number_endUser))
    
    if endUser_submite :
        
        dataF_match = matching_taille(dataF)
       
        generatorOrder(dataF_match,contract_type,contract_reference,contractor_name,contractor_company,contractor_phoneNumber)


    
else :
    st.write("Please indicate the total number of end users")


