import pandas
import streamlit
streamlit.title("Fruit Smoothies")
streamlit.header("Smoothie Menu")
streamlit.text("Blueberry and milk")
streamlit.text("Grapes")
streamlit.text("Banana milkshake")
streamlit.text("Strawberry Chocolate")
streamlit.text("Double chocolate")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
