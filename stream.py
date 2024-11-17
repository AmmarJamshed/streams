#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

# Import the profit calculation function
def calculate_profit(cost_price, selling_price):
    profit_or_loss = selling_price - cost_price
    if profit_or_loss > 0:
        return f"Profit: {profit_or_loss} units"
    elif profit_or_loss < 0:
        return f"Loss: {-profit_or_loss} units"
    else:
        return "No Profit, No Loss"

# Streamlit App
def main():
    st.title("Profit Calculator")
    
    st.write("Enter the cost price and selling price to calculate profit or loss.")
    
    # Input fields
    cost_price = st.number_input("Cost Price", min_value=0.0, step=0.01)
    selling_price = st.number_input("Selling Price", min_value=0.0, step=0.01)
    
    if st.button("Calculate Profit"):
        result = calculate_profit(cost_price, selling_price)
        st.write(result)

if __name__ == "__main__":
    main()


# In[ ]:




