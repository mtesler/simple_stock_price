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
