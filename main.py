import streamlit as st 
import numpy as np 

st.sidebar.header("Website Settings")
variables = ["x" , "y" , "z"]

defualtEquation1 = "+".join([f"{i}{x}" for i , x in zip(np.random.randint(10, size = 3) , variables)if i!= 0])
defualtEquation2 = "+".join([f"{i}{x}" for i , x in zip(np.random.randint(10, size = 3) , variables)if i!= 0])
defualtEquation3 = "+".join([f"{i}{x}" for i , x in zip(np.random.randint(10, size = 3) , variables)if i!= 0])

c1 , c2 , c3 = (i.strip()[0] if i.strip()[0] != "" else 0 for i in defualtEquation1.split("+"))
c4 , c5 , c6 = (i.strip()[0] if i.strip()[0] != "" else 0 for i in defualtEquation2.split("+"))
c7 , c8 , c9 = (i.strip()[0] if i.strip()[0] != "" else 0 for i in defualtEquation3.split("+"))


#c1 , c2 , c3 = st.columns(3)
#c4, c5, c6 = st.columns(3)
#c7, c8, c9 = st.columns(3)

#c1_input = c1.text_input("a11", value=4)
#c2_input = c2.text_input("a12", value=3)
#c3_input = c3.text_input("a13", value=2) 
#c4_input = c4.text_input("a21", value=500)
#c5_input = c5.text_input("a22", value=100)
#c6_input = c6.text_input("a23", value="15")
#c7_input = c7.text_input("a31", value=500)
#c8_input = c8.text_input("a32", value=100)
#c9_input = c9.text_input("a33", value="15")

# Get user inputs
L1  = st.text_input("First Equation : " , value=defualtEquation1)
L2 = st.text_input("Second Equation : " , value=defualtEquation2)
L3  = st.text_input("Third Equation : " , value=defualtEquation3)

st.write(f"""
         [{c1} , {c2} , {c3}]\n
         [{c4} , {c5} , {c6}]\n
         [{c7} , {c8} , {c9}]
         """)
