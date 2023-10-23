import pandas
import streamlit
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("Fruit Smoothies")
streamlit.header("Smoothie Menu")
streamlit.text("Blueberry and milk")
streamlit.text("Grapes")
streamlit.text("Banana milkshake")
streamlit.text("Strawberry Chocolate")
streamlit.text("Double chocolate")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruityvice(this_fruit_choice):
	fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
	fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
	return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
	fruit_choice = streamlit.text_input('What fruit would you like information about?')
	if not fruit_choice:
		streamlit.error("Please select a fruit to get information.")
	else:
		streamlit.dataframe(get_fruityvice(fruit_choice))
except URLError as e:
	streamlit.error()
	
streamlit.stop()
streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
	with my_cnx.cursor() as my_cur:
		my_cur.execute("SELECT * from pc_rivery_db.public.fruit_load_list")
		return my_cur.fectchall()

if streamlit.button('Get Fruit Load List'):
	my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
	my_data_rows=get_fruit_load_list()
	streamlit.dataframe(my_data_rows)	

def insert_row_snowflake(new_fruit):
	with my_cnx.cursor() as my_cur:
		my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from lit')")
		return "Thanks for adding"+new_fruit
	
my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to list'):
	my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
	streamlit.text(insert_row_snowflake(my_fruit))


