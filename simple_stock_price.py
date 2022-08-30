import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of selected company!

""")

# define the ticker symbol
ticker_symbol = st.text_input(
    'Selected company: ', 'AAPL')

# get data on this ticker
ticker_data = yf.Ticker(ticker_symbol)

# get the historical prices for this ticker
start_date = st.date_input(
    'Please select a start date')

end_date = st.date_input(
    'Please select a end date')

ticker_df = ticker_data.history(
    period='1d', start=start_date, end=end_date)

# create line charts
st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume)
