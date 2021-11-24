
import streamlit as st
import numpy as np
import pandas as pd
import plotly_express as px

### Import data frame
data_raw = pd.read_csv("flavors_of_cacao.csv")

choco_data_raw = pd.read_csv("flavors_of_cacao.csv")
choco_data_raw.drop(['Specific Bean Origin\nor Bar Name', 'REF'], axis = 1, inplace = True)
newcol = ['Company', 'Year', 'Cocoa Percent', 'Location', 'Rating', 'Bean Type', 'Bean Origin']

df = choco_data_raw.rename(columns = dict(zip(choco_data_raw.columns, newcol)))
df['Cocoa Percent'] = df['Cocoa Percent'].replace('[%,]', '', regex=True).astype(float)
pd.options.display.float_format = "{:,.2f}".format # WHY: doesn't work????
df['Year'] = df['Year'].apply(lambda x: str(x))
# Try n error: clean data



### --- 'Home' page

col1, col2 = st.columns([2, 1])

with col1:
  st.write("""
  # Chocolate Bar Ratings
  
  #### This web app analyses **Chocolate Bar Ratings** dataset!
  
  Disclaimer:  
  This is a web app using python libraries for learning purpose only.
  """)

with col2:
  st.write("")
  st.write("")
  st.write("")
  st.image("https://cutt.ly/eTSXVJf")

st.write("")
st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html).')

show = st.checkbox('I agree the terms and conditions.')
st.write("")
st.write("")

if show:


### --- Sidebar layout

    st.sidebar.write(
       """Credits to:  
        - Ts. Dr. Yong Poh Yu  
        - Dr. Tan Yan Bin"""
    )
    st.sidebar.write(
       """For more info, please contact:  
       [Musfirah Muzamil](https://www.linkedin.com/in/musfirah-muzamil)"""
    )
    
    st.sidebar.write('')
    

    ### --- Sidebar selectbox
    option = st.sidebar.selectbox(
        'Select your page',
        ['Home', 'Dataset', 'Scatterplot', 'Histogram'])
    
    #### --- Option 'Home'
    if option=='Home':
      st.subheader('What is chocolate?')
      st.write('')
      st.video("https://www.youtube.com/watch?v=D3QjYCZ2-xs")
      st.write('')
      st.write(
        """**Learn more on**  
        - [Chocolate](https://www.scienceofcooking.com/chocolate/how-is-chocolate-made.htm)  
        - [History of Chocolate](https://www.history.com/topics/ancient-americas/history-of-chocolate)  
        - [Flavors of Cacao](http://flavorsofcacao.com/chocolate_database.html)
        """
      )

    #### --- Option 'Dataset'
    if option=='Dataset':
      st.subheader('Dataset')
      st.write(
          """Source:  
        Kaggle ([Chocolate Bar Ratings](https://www.kaggle.com/rtatman/chocolate-bar-ratings))"""
        )
      st.write('')
      show2 = st.checkbox('Display raw data.')
      if show2:
        st.write(data_raw)
        st.write("")      
      st.write(df)
      st.write('')
      st.write(df.describe())
      # WHY: Can’t adjust dataframes decimal places
      # Try n error: display top 5 uniques data based on columns

    #### --- Option 'Scatterplot'  
    if option=='Scatterplot':
      x_axis = st.sidebar.selectbox(
          'x-axis',options = list(df.columns))
      y_axis = st.sidebar.selectbox(
          'y-axis', options = list(df.columns))
      scatterplot = px.scatter(data_frame = df, x = x_axis, y = y_axis)
      st.plotly_chart(scatterplot)

    #### --- Option 'Histogram'    
    if option=='Histogram':
      x_axis = st.sidebar.selectbox(
          'x-axis', options = list(df.columns))
      y_axis = st.sidebar.selectbox(
          'y-axis', options = list(df.columns))
      histo = px.histogram(data_frame = df, x = x_axis, y = y_axis)
      st.plotly_chart(histo)
    
    # Try n error: Random forest, SVM, KNN