import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google! 

""")

# define the ticker symbol
ticker_symbol = 'GOOGL'

# get data on this ticker
ticker_data = yf.Ticker(ticker_symbol)

# get the historical prices for this ticker
ticker_df = ticker_data.history(
    period='1d', start='2020-01-01', end='2022-08-29')
