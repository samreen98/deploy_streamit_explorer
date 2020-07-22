import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# st.balloons()
# st.error('This is an error')
# st.info('This is a purely informational message')
# st.success('This is a success message!')

# my_placeholder = st.empty()
# my_placeholder.text("Hello world!")
# time.sleep(6)
# image = Image.open('/home/FRACTAL/samreen.khan/samreen/images/shoping.jpg')
# my_placeholder.image(image, caption='Sunrise by the mountains', use_column_width=True)

# st.help(pd.DataFrame)

df1 = pd.DataFrame(
np.random.randn(5, 4),
columns=('col %d' % i for i in range(4)))
my_table = st.table(df1)

df2 = pd.DataFrame(
np.random.randn(10, 4),
columns=('col %d' % i for i in range(4)))
my_table.add_rows(df2)

my_chart = st.line_chart(df1)
my_chart.add_rows(df2)


st.write("wowwwwwwwwwww")



    
    
    
    
    
# with st.spinner('Wait for it...'):
#     time.sleep(20)
#     st.success('Done!')
    
# df = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))

# st.dataframe(df.style.highlight_max(axis=1))
# arr = np.random.normal(1, 1, size=100)

# image = Image.open('/home/FRACTAL/samreen.khan/samreen/images/shoping.jpg')
# st.image(image, caption='Sunrise by the mountains', use_column_width=True)


# if st.button('Say hello'):
#     st.write('111Why hello there')
# # else:
# #     st.write('222Goodbye')

# agree = st.checkbox('I agree')

# if agree:
#     st.write('Great!')

# title = st.text_input('Movie title', 'name a movie')
# st.write('The current movie title is', title)

# number = st.number_input('Insert a number')
# st.write('The current number is ', number)


# txt = st.text_area('Text to analyze', '''
# ...     It was the best of times, it was the worst of times, it was
# ...     the age of wisdom, it was the age of foolishness, it was
# ...     the epoch of belief, it was the epoch of incredulity, it
# ...     was the season of Light, it was the season of Darkness, it
# ...     was the spring of hope, it was the winter of despair, (...)
# ...     ''')
# st.write('Sentiment:',txt)

# import datetime
# d = st.date_input("When's your birthday",datetime.date(2019, 7, 6))
# st.write('Your birthday is:', d)


# t = st.time_input('Set an alarm for', datetime.time(8, 45))
# st.write('Alarm is set for', t)

# uploaded_file = st.file_uploader("Choose a excel file", type="xlsx")
# if uploaded_file is not None:
# #     data = pd.read_csv(uploaded_file)
#     excel_data_df = pd.read_excel(uploaded_file, sheet_name='Sheet1')
#     st.write(excel_data_df)


# x = st.slider('xx')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (5.0, 75.0)
# )

# @st.cache  # 👈 This function will be cached
# def my_slow_function(arg1, arg2):
#     # Do something really slow in here!
#     return the_output

# # st.title("rrrrrrrrrrrrrrrrrrrrrr")
# # st.header("rrrrrrrrrrrrrrrrrrrrrrrrrr")
# # st.subheader("rrrrrrrrrrrrrrrrrrrrrrrr")
# # st.markdown('###### rrrrrrrrrrrrrrrrrrrrrrrr')
# # st.text('This is some text.')

# st.markdown('Streamlit is **_really_ cool**.')

# st.latex(r'''
# ...     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
# ...     \sum_{k=0}^{n-1} ar^k =
# ...     a \left(\frac{1-r^{n}}{1-r}\right)
# ...     ''')

# st.write('Hello, *World!* :sunglasses:')

# code1 = '''def hello():
# ...     print("Hello, Streamlit!")'''
# st.code(code1, language='python')


# st.title('My first app')
# st.write("Here's our first attempt at using data to create a table:")
# # st.write(pd.DataFrame({
# #     'first column': [1, 2, 3, 4,5,6],
# #     'second column': [10, 20, 30, 40,55,77]
# # }))

# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })
# df

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [100, 350] + [47.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     st.line_chart(chart_data)
    
# option = st.sidebar.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected:', option

# import time

# latest_iteration = st.empty()
# bar = st.progress(0)

# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.5)

# '...and now we\'re done!'

