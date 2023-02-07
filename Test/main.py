import pandas as pd
import jinja2
import pdfkit
import streamlit as st

st.header("Hello Tableau PDF")

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
data_frames = pd.DataFrame(data)

st.dataframe(data)  


def ClientFileGenerator (data):
    
    name = "Hello"
    data_frames = pd.DataFrame(data)
      
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "Test/index.html"
    template = templateEnv.get_template(TEMPLATE_FILE)

    outputText = template.render(df=data_frames)
    html_file = open(name + '.html', 'w')
    html_file.write(outputText)
    html_file.close()
    pdfkit.from_file(name + '.html', name + '.pdf')

    with open(f"{name}.pdf","rb") as file :
        st.download_button("Tableau pdf",
                        data= file,
                        file_name="test.pdf",
                        
                        )
       
    

ClientFileGenerator(data)



