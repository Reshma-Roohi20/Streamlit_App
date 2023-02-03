
import streamlit as st
 
st.title("Calculator App using Streamlit")
 
# creates a horizontal line
st.write("Calculator")

# input 1
num1 = st.number_input(label="Enter first number")
 
# input 2
num2 = st.number_input(label="Enter second number")

st.write("Operation")
 
operation = st.radio("Select an operation to perform:",
                    ("Add", "Subtract", "Multiply", "Divide"))
