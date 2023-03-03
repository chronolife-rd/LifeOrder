import pandas as pd

datamaindic2 = {
        0: {'EndUserID': 'ZEpxRz', 
            'Reference': {'CHQ-3-01', 'NEX-0014-LBL-09', 'USQ-0-01', 'NEX-TSH-1-01-1', 'PSS-0-01', 'ASE-0-01', 'NEX-0017-LBL-08'}, 
            'Description': {'Wireless Charger', 'USB cable for wireless charger', 'Power Supply', 'CST T-shirt Size 1', 'CST Quick Start Guide – FR', 'EU adaptor', 'CST Instruction for Use – FR'}, 
            'Quantity': {"1":1,"2":1,"3":1,"4":1,"5":1,"6":1}}, 
        1: {'EndUserID': 'ZEpxRz', 'Reference': 
            {'CHQ-3-01', 'NEX-0014-LBL-09', 'USQ-0-01', 'NEX-TSH-1-01-1', 'PSS-0-01', 'ASE-0-01', 'NEX-0017-LBL-08'}, 
            'Description': {'Wireless Charger', 'USB cable for wireless charger', 'Power Supply', 'CST T-shirt Size 1', 'CST Quick Start Guide – FR', 'EU adaptor', 'CST Instruction for Use – FR'}, 
            'Quantity': {"1":1,"2":1,"3":1,"4":1,"5":1,"6":1}}, 
        2: {'EndUserID': 'ZEpxRz', 'Reference': 
            {'CHQ-3-01', 'NEX-0014-LBL-09', 'USQ-0-01', 'NEX-TSH-1-01-1', 'PSS-0-01', 'ASE-0-01', 'NEX-0017-LBL-08'}, 
            'Description': {'Wireless Charger', 'USB cable for wireless charger', 'Power Supply', 'CST T-shirt Size 1', 'CST Quick Start Guide – FR', 'EU adaptor', 'CST Instruction for Use – FR'}, 
            'Quantity': {"1":1,"2":1,"3":1,"4":1,"5":1,"6":1}}}


def endUserListGenerator (endUserDic):
    end_user_list = []
    mainList = []

    df_endUserOrder = pd.DataFrame.from_dict(endUserDic)
    df_endUserOrderTranspose = df_endUserOrder.transpose()

    for enduser in range (len(datamaindic2)):
            refdic_1 = df_endUserOrderTranspose["Reference"][enduser]
            descriptionDic_1 = df_endUserOrderTranspose["Description"][enduser]
            quantityDic_1 = df_endUserOrderTranspose["Quantity"][enduser]

            reflist_1 = list(refdic_1)
            descriptionList_1 = list(descriptionDic_1)
            quantityList_1 = list(quantityDic_1)

            for i in range (len(quantityDic_1)) :
                    
                    end_user_list.append([reflist_1[i],descriptionList_1[i],quantityList_1[i]])

            mainList.append(end_user_list)

    return mainList

my_data = endUserListGenerator(datamaindic2)