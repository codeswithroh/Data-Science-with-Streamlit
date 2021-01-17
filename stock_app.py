import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
#### created by @codes_with_roh
""" )
# making a drop down menu for the user to select the stock he wants to see
stocks= st.selectbox("Stocks",["AAPL","GOOGL","TSLA"]) 

def selecting_stocks(stocks):

    #defining the ticker symbol => symbol used for trading
    tickersymbol= stocks

    #getting data on this ticker
    tickerData= yf.Ticker(tickersymbol)


    #getting the historical prices for this ticker
    tickerDf= tickerData.history(period="1d", start="2010-1-5", end="2020-1-5")

    # Open High Low Close Volume Dividends Stock Splits => these are the parameters we could watch
    #                                                      using the tickerDF.parameter
    if stocks=="AAPL":
        st.write("""
        ## Closing Price Of APPLE Stocks
        """)
        st.line_chart(tickerDf.Close)
        st.write("""
        ## Volume Price Of APPLE Stocks
        """)
        st.line_chart(tickerDf.Volume)
    elif stocks=="GOOGL":
        st.write("""
        ## Closing Price Of GOOGLE Stocks
        """)
        st.line_chart(tickerDf.Close)
        st.write("""
        ## Volume Price Of GOOGLE Stocks
        """)
        st.line_chart(tickerDf.Volume)
    elif stocks=="TSLA":
        st.write("""
        ## Closing Price Of TESLA Stocks
        """)
        st.line_chart(tickerDf.Close)
        st.write("""
        ## Volume Price Of TESLA Stocks
        """)
        st.line_chart(tickerDf.Volume)

selecting_stocks(stocks)