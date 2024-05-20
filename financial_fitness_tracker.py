# Financial Fitness Tracker 
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title="Financial Fitness Tracker", page_icon="💰", layout="centered", initial_sidebar_state="auto")

# Initialize session state
if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame(columns=['Date', 'Type', 'Category', 'Amount'])
if 'score' not in st.session_state:
    st.session_state['score'] = 0

# Function to add new transaction
def add_transaction():
    new_data = {'Date': date, 'Type': transaction_type, 'Category': category, 'Amount': amount}
    st.session_state['data'] = st.session_state['data'].append(new_data, ignore_index=True)
    update_score()

# Function to update financial fitness score
def update_score():
    expenses = st.session_state['data'][st.session_state['data']['Type'] == 'Expense']['Amount'].sum()
    income = st.session_state['data'][st.session_state['data']['Type'] == 'Income']['Amount'].sum()
    if income > 0:
        st.session_state['score'] = max(0, min(100, int((income - expenses) / income * 100)))

# Title
st.title("💰 Financial Fitness Tracker 💰")

# Input fields with some styling
st.sidebar.header("Add New Transaction")
date = st.sidebar.date_input("Date")
transaction_type = st.sidebar.selectbox("Type", ["Income", "Expense"])
category = st.sidebar.selectbox("Category", ["Salary", "Food", "Transportation", "Entertainment", "Others"])
amount = st.sidebar.number_input("Amount", min_value=0.0, format="%.2f")
if st.sidebar.button("Add Transaction"):
    add_transaction()
    st.sidebar.success("Transaction added!")

# Display data
st.subheader("📜 Transaction History")
st.dataframe(st.session_state['data'])

# Financial Fitness Score
st.subheader("💪 Your Financial Fitness Score")
score = st.session_state['score']
st.write(f"Score: {score}/100")
st.progress(score)

# Monthly Summary
st.subheader("📅 Monthly Summary")
summary = st.session_state['data'].groupby('Type')['Amount'].sum()
st.write(summary)

# Category Breakdown with fancy styling
st.subheader("📊 Category Breakdown")
if not st.session_state['data'].empty:
    category_data = st.session_state['data'][st.session_state['data']['Type'] == 'Expense']
    category_summary = category_data.groupby('Category')['Amount'].sum()
    fig, ax = plt.subplots()
    category_summary.plot(kind='pie', ax=ax, autopct='%1.1f%%', colors=plt.cm.Paired.colors, startangle=90)
    ax.set_ylabel('')
    ax.set_title('Expenses by Category')
    st.pyplot(fig)

# Savings Challenges
st.subheader("🎯 Savings Challenges")
st.write("Feature under development")

# Random Finance Tips and Trivia
st.subheader("💡 Finance Tips & Trivia")
tips = [
    "Did you know? The average American has over $38,000 in personal debt.",
    "Tip: Automate your savings to ensure you save a portion of your income every month.",
    "Trivia: The first credit card was introduced in 1950 by the Diners' Club.",
    "Tip: Track your expenses to find areas where you can cut back and save more.",
    "Did you know? Compound interest can significantly increase your savings over time."
]
st.info(np.random.choice(tips))

st.write("Developed using GenAI in less than 30 minutes!")
