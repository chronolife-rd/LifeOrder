import streamlit as st
import json
import pandas as pd
myfamily = {
  "child0" : {
    "name" : "Emil",
    "year" : 2004,
    "nbChaussure" : 10,
    "typeChaussure" : "Basket"
  },
  "child1" : {
    "name" : "Tobias",
    "year" : 2007,
    "nbChaussure" : 1,
    "typeChaussure" : "Basket"
  },
  "child2" : {
    "name" : "Linus",
    "year" : 2011,
    "nbChaussure" : 12,
    "typeChaussure" : "Tong"
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011,
    "nbChaussure" : 10,
    "typeChaussure" : "Tong"
  }
}
a = 10

child4 = {

    "child4" : {
    "name" : f"{a}",
    "year" : 2011
  }

}

tets = [1,2,3,13,1]

st.write(tets[1])
#For excel File 

# df = pd.read_excel("ProductReference.xlsx")

nbChaussureBasket = 0
nbChaussureTong = 0

# print (myfamily[f"child0"]["nbChaussure"]+ myfamily[f"child1"]["nbChaussure"])

for i in range (len(myfamily)):
  

  if myfamily[f"child{i}"]["typeChaussure"] == "Basket":
     nbChaussureBasket = nbChaussureBasket + myfamily[f"child{i}"]["nbChaussure"]

  elif myfamily[f"child{i}"]["typeChaussure"] == "Tong":
    
     nbChaussureTong += myfamily[f"child{i}"]["nbChaussure"]

  else :
     pass
     

     
st.write("Nombre de basket : ", nbChaussureBasket)
st.write(nbChaussureTong)



myfamily.update(child4)

# print (myfamily["child2"]["name"])

# df = pd.DataFrame.from_dict(myfamily,orient="index")


yJson = {

    "id": f"{a}",
    "Genrder":"Mr",
    "Age":"90",
    }




def writejson  (newData, mainData):

    file_data = json.dumps(mainData)
    file_data["End User information"].append(newData)


# st.json(myfamily)
