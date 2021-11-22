import streamlit as st
import numpy as np
import pandas as pd
import plotly_express as px

data_raw = pd.read_csv("flavors_of_cacao.csv")

choco_data_raw = pd.read_csv("flavors_of_cacao.csv")
choco_data_raw.drop(['Specific Bean Origin\nor Bar Name', 'REF'], axis = 1, inplace = True)
newcol = ['Company', 'Year', 'Cocoa Percent', 'Location', 'Rating', 'Bean Type', 'Bean Origin']

choco_data = choco_data_raw.rename(columns = dict(zip(choco_data_raw.columns, newcol)))

col1, col2 = st.columns([2, 1])

with col1:
  st.write("""
  # Chocolate Bar
  
  #### This web app displays the variables that affect the **Chocolate Bar Ratings**!
  
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
if show:
    
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
    
    option = st.sidebar.selectbox(
        'Select your page',
        ['Home', 'Dataset', 'Scatterplot', 'Random Forest'])
    
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

    if option=='Dataset':
      st.subheader('Dataset')
      st.write(
          """Source:  
        Kaggle ([Chocolate Bar Ratings](https://www.kaggle.com/rtatman/chocolate-bar-ratings))"""
        )
      st.write('')
      show = st.checkbox('Display raw data.')
      if show:
        st.write(data_raw)
        st.write("")      
      st.write(choco_data)
      st.write('')
      st.write(choco_data.describe())
      st.write(
          """References: [[1](https://mguideng.github.io/2018-10-13-chocolate-ratings-p1/)],[[2](https://www.kaggle.com/baghern/what-s-in-a-rating-chocolate-modeling)]
          """
      )
    
    if option=='Scatterplot':
      x_axis = st.sidebar.selectbox(
          'x-axis',
          options = list(choco_data.columns))
      y_axis = st.sidebar.selectbox(
          'y-axis',
          options = list(choco_data.columns))
      scatterplot = px.scatter(data_frame = choco_data, x = x_axis, y = y_axis)
      st.plotly_chart(scatterplot)
