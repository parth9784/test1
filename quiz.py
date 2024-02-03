from idlelib import window

import streamlit as st
import time as t
st.header("Hi! Welcome to the Quiz")
st.subheader("This Quiz is of 10 Marks and all the Questions are Compulsory.")
st.subheader("All the Best !!")
ans=["6","4","JAVAC","Process","Blind Carbon copy","rm","False","Disk OS","I m ok","Scope Resolution Operator"]
ls=[]
st.subheader("Question 1.")
st.write("Guess the Correct Output.")
code='''
   ls=[2,2,3,1,6,1,3]
   a=0
   for i in ls:
        a=a^i   (xor);
    print(a)    
   '''
st.code(code,language="python")
q1=st.radio("Options:",options=("0","1","6","None of the above"),index=None)
ls.append(q1)

st.subheader("Question 2.")
st.write("What is name of compiler of java ?")
q2=st.radio("Options:",options=("JVM","JAVAC","JDBC","JAVACOMPILER"),index=None)
ls.append(q2)

st.subheader("Question 3.")
st.write("The ‘P’ in CPU stands for …")
q3=st.radio("Options:",options=("Process","Program","Progress","Plain"),index=None)
ls.append(q3)

st.subheader("Question 4.")
st.write("While sending an email, you add one or more recipients, but in order to keep their identity secret to main addressee, you keep them in ‘BCC;’ BCC stands for …")
q4=st.radio("Options:",options=("Black Carbon copy","Blind Carbon copy","Black Creative copy","Blind Creative copy"),index=None)
ls.append(q4)
st.subheader("Question 5.")
st.write("What command is used to remove files?")
q5=st.radio("Options:",options=("rm","rmdir","del","rem"),index=None)
ls.append(q5)

st.subheader("Question 6.")
st.write("Adding a derived class to a base class requires fundamental changes to the base class ?")
q6=st.radio("Options:",options=("True","False"),index=None)
ls.append(q6)
st.subheader("Question 7.")
st.write("DOS stands for? ")
q7=st.radio("Options:",options=("Display OS","Disk OS","Disc OS","Dew OS"),index=None)
ls.append(q7)
text1='''
#include <iostream>
using namespace std;

int main() {
    bool ok = true;
    // Try to guess with if condition  \
    
    if (!ok && true) 
        cout << "I am ok" << endl;
    return 0;
}'''
st.subheader("Question 8.")
st.code(text1,language="C++")
q8=st.radio("Options:",options=("False","I m ok","True","NOTA"),index=None)
ls.append(q8)

st.subheader("Question 9.")
st.write("What is :: in C++?")
q9=st.radio("Options:",options=("Resolution Operator","Scope Defining Operator","Scope Resolution Operator","NOTA"),index=None)
ls.append(q9)

st.subheader("Question 10.")
st.write("What size of a vector became in memory is it currently contain 2 element and you add 1 more element in it? ")
q10=st.radio("Options:",options=("8","2","3","4"),index=None)
ls.append(q10)

but = st.button("Submit")
if but:
    st.write("We are computing your result please wait.")
    bar = st.progress(0)
    for i in range(100):
        t.sleep(0.01)
        bar.progress(i + 1)
    t.sleep(1)

    # Calculate the score only after the submit button has been pressed
    marks = 0
    for i in ls:
        if str(i) in ans:
            marks = marks + 1

    # Display the score only after the submit button has been pressed
    st.subheader("Your score is " + str(marks))

