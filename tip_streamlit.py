# importing the libraries 

import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

# importing the dataset

data=pd.read_csv("tip.csv")

#sidebar 

st.sidebar.header("Choose a insight")
choice = st.sidebar.radio("",options = ["Which meal of the day tends to bring in the most tips?", 
                                   "Who tends to leave bigger tips, and during which meal do they usually do it?",
                                   "What’s the connection between the tip and the total bill?",
                                   "What time do people usually stop by the restaurant?",
                                   "What day do we usually get the most tips?",
                                   "What is the probability that individuals prefer dining on specific days of the week?",
                                   "Do smokers tend to give higher tips?"])

if choice == "Which meal of the day tends to bring in the most tips?":
    sns.violinplot(data = data, x = "time", y ="tip", palette="Dark2")
    plt.title("Time vs Tip ", size = 18)
    plt.show()
    st.pyplot(plt)
    st.header("Conclusion :")
    st.write("During dinner, we usually get some extra tips!")
    
elif choice == "Who tends to leave bigger tips, and during which meal do they usually do it?":
    sns.violinplot(data = data , x ="time", y ="tip", hue = "sex", palette= "Dark2")
    plt.title("Time v/s Tip", size = 18)
    plt.show()  
    st.pyplot(plt)
    st.header("Conclusion :")
    st.write("Men usually leave a bit more in tips during dinner!")
    
elif choice == "What’s the connection between the tip and the total bill?":
    sns.scatterplot(data=data, x= "total_bill", y ="tip", palette= "Dark2")
    plt.title("Tip v/s Total Bill", size = 18)
    plt.show()
    st.pyplot(plt)
    st.header("Conclusion :")
    st.write("When the total bill goes up, it’s great to see that tips tend to go up too! It really shows how a higher bill often comes with a more generous tip.")
    
elif choice == "What time do people usually stop by the restaurant?":
    sns.barplot(data=data, x = "time", y ="size", palette="Dark2")
    plt.title("Time v/s Size", size = 18)
    plt.show()
    st.pyplot(plt)
    st.header("Conclusion :")
    st.write("At dinner, we typically get two groups of people coming to the restaurant.")
    
elif choice == "What day do we usually get the most tips?":
    sns.violinplot(data = data, x = "day", y ="tip", palette = "Dark2")
    plt.title("day v/s tip ", size = 18)
    plt.show()
    st.pyplot(plt)
    st.header("Conclusion :")
    st.write("Saturdays are the busiest days, and restaurants usually get the most tips. It looks like a lot of people enjoy dining in the restaurant on the weekends!")
    
elif choice == "What is the probability that individuals prefer dining on specific days of the week?":
    sns.violinplot(data = data, x = "day", y ="size", palette = "Dark2")
    plt.title("Day v/s Size", size =18 )
    plt.show()
    st.pyplot(plt)
    st.header("Conclusion :")
    st.write("On Sundays, the probability of customers is 2.")
    st.write("On Saturdays, the probability of customers is 2.")
    st.write("On Thursdays, the probability of customers is 2.")
    st.write("On Fridays, the probability of customers is 2.")
    
elif choice == "Do smokers tend to give higher tips?":
    sns.violinplot(data = data, x = "smoker", y ="tip", palette = "Dark2")
    plt.title("Smokers v/s Tip ", size =18)
    plt.show()
    st.pyplot(plt)
    st.header("Conclusion :")
    st.write("Yes, smokers tend to leave more tips, but probability of non-smokers is more in the restaurant.")
   
    

