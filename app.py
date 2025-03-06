import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Personal Finance Guide")
    st.sidebar.header("User Input")
    
    # User Inputs
    income = st.sidebar.number_input("Monthly Income ($)", min_value=0.0, format="%.2f")
    expenses = st.sidebar.number_input("Total Monthly Expenses ($)", min_value=0.0, format="%.2f")
    savings = st.sidebar.number_input("Current Savings ($)", min_value=0.0, format="%.2f")
    investment_percentage = st.sidebar.slider("% of Savings for Investment", 0, 100, 30)
    
    # Calculations
    disposable_income = income - expenses
    investment_amount = (savings * investment_percentage) / 100
    savings_after_investment = savings - investment_amount
    
    # Display Financial Summary
    st.subheader("Financial Summary")
    st.write(f"**Disposable Income:** ${disposable_income:.2f}")
    st.write(f"**Planned Investment:** ${investment_amount:.2f}")
    st.write(f"**Savings After Investment:** ${savings_after_investment:.2f}")
    
    # Expense Visualization
    if expenses > 0:
        fig, ax = plt.subplots()
        labels = ["Savings", "Expenses"]
        values = [income - expenses, expenses]
        ax.pie(values, labels=labels, autopct='%1.1f%%', colors=['green', 'red'])
        ax.set_title("Income Distribution")
        st.pyplot(fig)
    
    # Investment Projection
    years = st.slider("Investment Growth Projection (Years)", 1, 20, 10)
    annual_return = st.slider("Expected Annual Return (%)", 1, 15, 7)
    
    investment_df = pd.DataFrame({
        'Year': range(1, years + 1),
        'Projected Value': [(investment_amount * ((1 + annual_return / 100) ** i)) for i in range(1, years + 1)]
    })
    
    st.subheader("Investment Projection")
    st.line_chart(investment_df.set_index('Year'))
    
    # Financial Tips
    st.subheader("Financial Tips")
    st.write("- Save at least 20% of your income.")
    st.write("- Diversify your investments.")
    st.write("- Track your expenses to avoid unnecessary spending.")
    st.write("- Invest in assets with long-term growth potential.")
    
if __name__ == "__main__":
    main()
