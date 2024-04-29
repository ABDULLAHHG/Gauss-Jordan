import streamlit as st 
import numpy as np 
import plotly.graph_objects as go 

st.sidebar.header("Website Settings")
variables = ["x1" , "x2" , "x3"]

defualtEquation1 = ("+".join([f"{i}{x}" for i , x in zip(np.random.randint(low = 1, high = 10 , size = 3) , variables)if i!= 0]) + "=" + str(int(np.random.randint(low = 10, high = 20 , size = 1))))
defualtEquation2 = ("+".join([f"{i}{x}" for i , x in zip(np.random.randint(low = 1, high = 10 , size = 3) , variables)if i!= 0]) + "=" + str(int(np.random.randint(low = 10, high = 20 , size = 1))))
defualtEquation3 = ("+".join([f"{i}{x}" for i , x in zip(np.random.randint(low = 1, high = 10 , size = 3) , variables)if i!= 0]) + "=" + str(int(np.random.randint(low = 10, high = 20 , size = 1))))

c1 , c2 , c3 = (i.strip()[0] if i.strip()[0] != "" else 0 for i in defualtEquation1.split("+"))
c4 , c5 , c6 = (i.strip()[0] if i.strip()[0] != "" else 0 for i in defualtEquation2.split("+"))
c7 , c8 , c9 = (i.strip()[0] if i.strip()[0] != "" else 0 for i in defualtEquation3.split("+"))
y1  = (defualtEquation1.split("=")[1])
y2  = (defualtEquation2.split("=")[1])
y3  = (defualtEquation3.split("=")[1])



x1 = np.arange(10)
x2 = np.arange(10)
x3 = np.arange(10)
result1 = eval("+".join([f"{i[0]} *{i[1:3]}"  for i in defualtEquation1.split("+")]))

fig = go.Figure()


fig.add_trace(go.Scatter(x = x1, y = result1,
                        mode = "lines" , 
                        ))


fig.update_layout(
                 font = dict(color = "#909497", size = 18),
                 title = dict(text = "Longitude VS Latitude", font = dict(size = 26)),
                 xaxis = dict(title = "Longitude", linecolor = "#909497"),
                 yaxis = dict(title = "Latitude", tickformat = ",", linecolor = "#909497"),
                 margin = dict(t = 100, r = 80, b = 80, l = 120),
                 height = 720,
                 width = 900)


st.plotly_chart(fig)        


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
         [{c1} , {c2} , {c3}] = {y1}\n
         [{c4} , {c5} , {c6}] = {y2}\n
         [{c7} , {c8} , {c9}] = {y3}
         """)


n = 3 

matrix = [[int(c1) , int(c2) , int(c3) , int(y1)],
          [int(c4) , int(c5) , int(c6) , int(y2)],
          [int(c7) , int(c8) , int(c9) , int(y3)]]
# Applying Gauss Jordan Elimination for upper matrix
for i in range(n):
    if matrix[i][i] == 0:
        st.error('Divide by zero detected!')

    # Scale the current row to make the diagonal element equal to 1
    scale_factor = matrix[i][i]
    for k in range(n+1):
        matrix[i][k] = matrix[i][k] / scale_factor

    # Subtract the scaled current row from other rows to make the elements below the diagonal equal to 0
    for j in range(i+1, n):
        ratio = matrix[j][i]

        for k in range(n+1):
            matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]


# Applying Gauss Jordan Elimination for lower matrix
for i in range(n):
    if matrix[i][i] == 0:
        st.error('Divide by zero detected!')

    # Scale the current row to make the diagonal element equal to 1
    scale_factor = matrix[i][i]
    for k in range(n+1):
        matrix[i][k] = matrix[i][k] / scale_factor

    # Subtract the scaled current row from other rows to make the elements above the diagonal equal to 0
    for j in range(i):
        ratio = matrix[j][i]

        for k in range(n+1):
            matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

# Obtaining Solution

# for i in range(n):
#     matrix[i] = matrix[i][n]/matrix[i][i]


st.write(f"""
         [{int(matrix[0][0])} , {int(matrix[0][1])} , {int(matrix[0][2])}] = {matrix[0][3]}\n
         [{int(matrix[1][0])} , {int(matrix[1][1])} , {int(matrix[1][2])}] = {matrix[1][3]}\n
         [{int(matrix[2][0])} , {int(matrix[2][1])} , {int(matrix[2][2])}] = {matrix[2][3]}
         """)
