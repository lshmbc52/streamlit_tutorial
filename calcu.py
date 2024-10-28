import streamlit as st

def calcu4(x,y,operation):
    if operation == "add": 
        return x + y

    elif operation =="sub":
        return x -y
    elif operation ==  "mul": 
        return x *y
    elif operation == "div": 
        if y == 0:
            return "0으로 나눌 수 없음"
        else:
            return x / y 

    

st.title("계산기")

num1 = st.number_input("첫번째 숫자 입력")
num2 = st.number_input("두번째 숫자 입력")

operation = st.selectbox("연산선택",("add","sub","mul","div"))

result=calcu4(num1,num2,operation)

st.write(f'"result",{result}')


