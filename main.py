import streamlit as st 
import numpy as np 
import plotly.graph_objects as go 

st.sidebar.header("Website Settings")
variables = ["x1" , "x2" , "x3"]

defualtEquation1 = "6x1+3x2+3x3=14"
defualtEquation2 = "8x1+5x2+3x3=19"
defualtEquation3 = "5x1+3x2+4x3=11"

if st.button("Create Random Linear Equations"):
    defualtEquation1 = ("+".join([f"{i}{x}" for i , x in zip(np.random.randint(low = 1, high = 10 , size = 3) , variables)if i!= 0]) + "=" + str(int(np.random.randint(low = 10, high = 20 , size = 1))))
    defualtEquation2 = ("+".join([f"{i}{x}" for i , x in zip(np.random.randint(low = 1, high = 10 , size = 3) , variables)if i!= 0]) + "=" + str(int(np.random.randint(low = 10, high = 20 , size = 1))))
    defualtEquation3 = ("+".join([f"{i}{x}" for i , x in zip(np.random.randint(low = 1, high = 10 , size = 3) , variables)if i!= 0]) + "=" + str(int(np.random.randint(low = 10, high = 20 , size = 1))))


# Get user inputs
L1  = st.text_input("First Equation : " , value=defualtEquation1)
L2 = st.text_input("Second Equation : " , value=defualtEquation2)
L3  = st.text_input("Third Equation : " , value=defualtEquation3)



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
                 title = dict(text = "Simple Linear Graph", font = dict(size = 26)),
                 xaxis = dict(title = "X", linecolor = "#909497"),
                 yaxis = dict(title = "Y", tickformat = ",", linecolor = "#909497"),
                 margin = dict(t = 100, r = 80, b = 80, l = 120),
                 height = 720,
                 width = 900)


st.plotly_chart(fig)        

c1 , c2 , c3 = (i.strip()[0] if i.strip()[0] != "" else 0 for i in L1.split("+"))
c4 , c5 , c6 = (i.strip()[0] if i.strip()[0] != "" else 0 for i in L2.split("+"))
c7 , c8 , c9 = (i.strip()[0] if i.strip()[0] != "" else 0 for i in L3.split("+"))

y1  = (L1.split("=")[1])
y2  = (L2.split("=")[1])
y3  = (L3.split("=")[1])

st.write("Current Matrix")
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
    # for k in range(n+1):
    #     matrix[i][k] = matrix[i][k] / scale_factor

    # Subtract the scaled current row from other rows to make the elements above the diagonal equal to 0
    for j in range(i):
        ratio = matrix[j][i]

        for k in range(n+1):
            matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]


st.write("Result")

st.write(f"""
         [{int(matrix[0][0])} , {int(matrix[0][1])} , {int(matrix[0][2])}] = {round(matrix[0][3] , 2)}\n
         [{int(matrix[1][0])} , {int(matrix[1][1])} , {int(matrix[1][2])}] = {round(matrix[1][3] , 2)}\n
         [{int(matrix[2][0])} , {int(matrix[2][1])} , {int(matrix[2][2])}] = {round(matrix[2][3] , 2)}
         """)
