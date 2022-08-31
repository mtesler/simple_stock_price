import yfinance as yf
import streamlit as st
import pandas as pd

st.markdown("<h1 style='text-align: center; color: black;'>Simple Stock Price App</h1>",
            unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: black;'>Shown are the stock closing price and volume of selected company!</h2>", unsafe_allow_html=True)

# define the ticker symbol
ticker_symbol = st.text_input(
    'Please type a company stock ticker: ', 'AAPL')

# get data on this ticker
ticker_data = yf.Ticker(ticker_symbol)

# get the historical prices for this ticker
start_date = st.date_input(
    'Please select start date for chart data:')

end_date = st.date_input(
    'Please select end date for chart data:')

ticker_df = ticker_data.history(
    period='1d', start=start_date, end=end_date)

# create line charts
st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume)
