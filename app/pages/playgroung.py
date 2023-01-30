import streamlit as st
import json
import pandas as pd
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
a = 10

child4 = {

    "child4" : {
    "name" : f"{a}",
    "year" : 2011
  }

}

#For excel File 

df = pd.read_excel("ProductReference.xlsx")

html_log = '''


  

'''

st.write(df.loc[5][0])

myfamily.update(child4)

print (myfamily["child2"]["name"])

df = pd.DataFrame.from_dict(myfamily,orient="index")


yJson = {

    "id": f"{a}",
    "Genrder":"Mr",
    "Age":"90",
    }




def writejson  (newData, mainData):

    file_data = json.dumps(mainData)
    file_data["End User information"].append(newData)


st.json(myfamily)
