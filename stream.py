#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

# Function to calculate profit or loss and cost as a percentage of profit
def calculate_profit(cost_price, selling_price):
    profit_or_loss = selling_price - cost_price
    if profit_or_loss > 0:
        profit_percentage = (cost_price / profit_or_loss) * 100  # Calculate cost as a percentage of profit
        return f"Profit: {profit_or_loss} units", f"Cost as Percentage of Profit: {profit_percentage:.2f}%"
    elif profit_or_loss < 0:
        return f"Loss: {-profit_or_loss} units", None
    else:
        return "No Profit, No Loss", None

# Streamlit App
def main():
    st.title("Profit Calculator")
    
    st.write("Enter the cost price and selling price to calculate profit or loss and cost as a percentage of profit.")
    
    # Input fields for cost and selling price
    cost_price = st.number_input("Cost Price", min_value=0.0, step=0.01, format="%.2f")
    selling_price = st.number_input("Selling Price", min_value=0.0, step=0.01, format="%.2f")
    
    # Handle the calculation
    if st.button("Calculate Profit"):
        if cost_price > 0 and selling_price >= 0:  # Basic validation
            profit_result, profit_percentage_result = calculate_profit(cost_price, selling_price)
            st.write(profit_result)
            
            # Show percentage of cost as a part of profit if there is a profit
            if profit_percentage_result:
                st.write(profit_percentage_result)
        else:
            st.write("Please enter valid cost and selling prices.")

# Run the main app only if this file is being executed directly
if __name__ == "__main__":
    main()


# In[ ]:




