import pandas as pd

datamaindic2 = {
        1: {'EndUserID': 'ZEpxRz', 
            'Reference': {'CHQ-3-01', 'NEX-0014-LBL-09', 'USQ-0-01', 'NEX-TSH-1-01-1', 'PSS-0-01', 'ASE-0-01', 'NEX-0017-LBL-08'}, 
            'Description': {'Wireless Charger', 'USB cable for wireless charger', 'Power Supply', 'CST T-shirt Size 1', 'CST Quick Start Guide – FR', 'EU adaptor', 'CST Instruction for Use – FR'}, 
            'Quantity': {1,1,1,1,1,1}}, 
        2: {'EndUserID': 'ZEpxRz', 'Reference': 
            {'CHQ-3-01', 'NEX-0014-LBL-09', 'USQ-0-01', 'NEX-TSH-1-01-1', 'PSS-0-01', 'ASE-0-01', 'NEX-0017-LBL-08'}, 
            'Description': {'Wireless Charger', 'USB cable for wireless charger', 'Power Supply', 'CST T-shirt Size 1', 'CST Quick Start Guide – FR', 'EU adaptor', 'CST Instruction for Use – FR'}, 
            'Quantity': {1,1,1,1,1,1}}, 
        3: {'EndUserID': 'ZEpxRz', 'Reference': 
            {'CHQ-3-01', 'NEX-0014-LBL-09', 'USQ-0-01', 'NEX-TSH-1-01-1', 'PSS-0-01', 'ASE-0-01', 'NEX-0017-LBL-08'}, 
            'Description': {'Wireless Charger', 'USB cable for wireless charger', 'Power Supply', 'CST T-shirt Size 1', 'CST Quick Start Guide – FR', 'EU adaptor', 'CST Instruction for Use – FR'}, 
            'Quantity': {1,1,1,1,1,1}}}



df_data  = {       
            # "EndUserId":" EZPs23",
            "Reference":["NEX -TSH-1-01-A32","NEX -TSH-1-01-A34","NEX -TSH-1-01-A36"],
            "Description":['CST T-shirt Size 32','CST T-shirt Size 24','CST T-shirt Size 36'],
            "Quantity": [2,3,1]
   }
end_user_list = []

df_datamaindic2 = pd.DataFrame.from_dict(datamaindic2)

df_datamaindic2_traspose = df_datamaindic2.transpose()

refdic_1 = df_datamaindic2_traspose["Reference"][1]
refdic_1 = df_datamaindic2_traspose["Reference"][1]
descriptionDic_1 = df_datamaindic2_traspose["Description"][1]
quantityDic_1 = df_datamaindic2_traspose["Quantity"][1]

reflist_1 = list(refdic_1)
descriptionList_1 = list(descriptionDic_1)
quantityList_1 = list(quantityDic_1)


for i in range (6) :
        
        end_user_list.append([reflist_1[i],descriptionList_1[i],quantityList_1[i]])
        # end_user_list.append(descriptionList_1[i])
        # end_user_list.append(quantityList_1[i])