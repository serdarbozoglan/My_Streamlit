import os
import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt 
import seaborn as sns
from PIL import Image, ImageFilter, ImageEnhance

# Title
st.title("Iris EDA App")
st.header("Built with Streamlit")

# EDA
my_dataset = 'iris.csv'

# Fxn to Load DataSet
@st.cache(persist=True) # To run it from cache, to egt fast response
def explore_data(dataset):
    df = pd.read_csv(os.path.join(dataset))
    return df

data = explore_data(my_dataset)

if st.checkbox("Preview Dataset"):
    if st.button("Head"):
        st.write(data.head())
    elif st.button("Tail"):
        st.write(data.tail())
    else:
        st.write(data.head(2))

# Show Entire Dataset
if st.checkbox("Show Entire Dataset"):
    # st.write(data)
    st.dataframe(data)

# Show Column Names
if st.checkbox('Show Column Names'):
    st.write(data.columns)

# Show Dimensions
data_dim = st.radio('What dimension do you want to see?', ("Rows", "Columns", "All"))
if data_dim == 'Rows':
    st.text("Showing Rows")
    st.write(data.shape[0])

elif data_dim == "Columns":
    st.text("Showing Columns") 
    st.write(data.shape[1])

else:
    st.text("Showing Shape of Dataset")
    st.write(data.shape)
    # st.text('Rows    :', data.shape[0])
    # st.text('Columns :', data.shape[1])
    #st.write(data)

# if st.checkbox("Dataset Dimensions"):
#     st.text("Row Size   :", data.shape[0])
#     st.text("Column Size:", data.shape[1])

# Show Summary
if st.checkbox("Show Dataset Summary"):
    st.write(data.describe())

# Select a Column
col_option = st.selectbox("Select Column", ("sepal_length", "sepal_width", "petal_length", "petal_width", "species"))
if col_option=='sepal_length':
    st.write(data['sepal_length'])
elif col_option=='sepal_width':
    st.write(data['sepal_width'])
elif col_option=='petal_length':
    st.write(data['petal_length'])
elif col_option=='petal_width':
    st.write(data['petal_width'])
elif col_option == 'species':
    st.write(data['species'])
else:
    st.write('Select Column')

# Plotting (Bar)
if st.checkbox("Show Bar Plot w Matplotlib"):
    st.write(data.plot(kind='bar'))
    st.pyplot()

# Plotting (Correlation) 
if st.checkbox("Show Correlation Plot w Matplotlib"):
    plt.matshow(data.corr())
    st.pyplot()

# Plotting (Correlation) 
if st.checkbox("Show Correlation Plot w Seaborn"):
    st.write(sns.heatmap(data.corr()))
    st.pyplot()

# Group
if st.checkbox("Show Bar Group Plot"):
    v_group = data.groupby('species')
    st.bar_chart(v_group)

# Images
@st.cache
def load_image(img):
    img = Image.open(os.path.join(img))
    return img

species_type = st.radio('Select Species Type', ('Setosa', 'Versicolor', 'Virginica'))

if species_type=='Setosa':
    st.text("Setosa Image")
    st.image(load_image('imgs/iris_setosa.jpg'))
elif species_type=='Versicolor':
    st.text('Versicolor Image')
    st.image(load_image('imgs/iris_versicolor.jpg'))
elif species_type=='Virginica':
    st.text('Virginica Image')
    st.image(load_image('imgs/iris_virginica.jpg'))

# Show Image
if st.checkbox("Show Image/Hide Image"):
	my_image = load_image('iris_setosa.jpg')
	enh = ImageEnhance.Contrast(my_image)
	num = st.slider("Set Your Contrast Number",1.0,3.0)
	img_width = st.slider("Set Image Width",300,500)
	st.image(enh.enhance(num),width=img_width)


# About

if st.button("About App"):
	st.subheader("Iris Dataset EDA App")
	st.text("Built with Streamlit")
	st.text("Thanks to the Streamlit Team Amazing Work")



