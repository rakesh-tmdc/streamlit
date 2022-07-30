import pandas as pd
import numpy as np

import streamlit as st
print("application running")
# Add a title
st.title('The Modern Data Company')
st.write('Owner of this App: Rakesh Vishvakarma')
st.write("Sample Table")

st.write(pd.DataFrame({
    'Age': [1, 2, 3, 4],
    'Weight': [10, 20, 30, 40]
}))

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])


option = st.sidebar.selectbox(
    'Which number do you like best?',
    [1, 2, 3, 4, 5, 6, 7])

st.write("Sample Chart: - {number:.0f}".format(number = option))
st.line_chart(chart_data)

left_column, right_column = st.columns(2)
pressed = left_column.button('Press here?')
if pressed:
    right_column.write("Woohoo!")

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)
print("Completed")