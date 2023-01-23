import streamlit as st

import AlgoMatch
import EndUserClass


contract_type = 'Location'

st.set_page_config(page_title="Commande Client")

number_endUser,contract_reference,contractor_name,contractor_company,contractor_phoneNumber = AlgoMatch.globalContractInformation(contract_type)

if int(number_endUser) > 0 :
    
    dataF,endUser_submite = EndUserClass.EndUserV2(2,10,contract_type).plotData(int(number_endUser))
    
    if endUser_submite :
        
        dataF_match = AlgoMatch.matching_taille(dataF)
        AlgoMatch.generatorOrder(dataF_match,contract_type,contract_reference,contractor_name,contractor_company,contractor_phoneNumber)
    
else :

    st.warning("No End User selected")

