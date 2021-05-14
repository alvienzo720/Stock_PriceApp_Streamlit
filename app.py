import streamlit as st  # Our GUI for the app
import pandas as pd 	# For reading our csv dat of tickers 
import yfinance as yf  	# Our Finance Api
import cufflinks as cf # for our graphs 
import datetime # date time 

# our app title
st.title("Stock App")

# app side bar 
st.sidebar.subheader("Check for a Stock")

# file with our stock sysmbols which is symbols.txt
ticker_file="symbols.txt"

# We use pandas as pd to read the contents of the symbols.txt file 
all_tickers = pd.read_csv(ticker_file)

# ticker dropdwon 
ticker = st.sidebar.selectbox('Stock Symbol', all_tickers)

# our start date by default
from_date = st.sidebar.date_input("From", datetime.date(2020, 1, 1))

# our end date by defualt
to_date = st.sidebar.date_input("To", datetime.datetime.now())

# we crate a variable to contain the ticker syembol and assign it to yfinance 
tickerdata = yf.Ticker(ticker)
# we create a variable to display our data
tickerInfoToPlot = tickerdata.history(period='1d', start=from_date, end=to_date)

# we create a dsiplay element which will dsiplay the stock name
stock_name = tickerdata.info['longName']

st.header(stock_name)

# we dsiplay the stock price summary in a table
st.header("Stock Price Summary")

st.write(tickerInfoToPlot)

# display the stock price Open graph 
st.header("Stock Open Graph")
st.line_chart(tickerInfoToPlot.Open)


# display the stock price Close graph 
st.header("Stock Close Graph")
st.line_chart(tickerInfoToPlot.Close)

# display the stock price Volume graph 
st.header("Stock Volume Graph")
st.line_chart(tickerInfoToPlot.Volume)

# here we use cufflinks to dssiplay a detailed stock analysis graph 
# our figure to be displayed using cufflinks and the various attributes 
qf = cf.QuantFig(tickerInfoToPlot,title='Full Stock Analysis',legend='top',name='GS')

# adding boilinger bands to the graph
qf.add_bollinger_bands()

# plotting the graph as a figure
fig = qf.iplot(asFigure=True)

# using streamlit to plot the charts
st.plotly_chart(fig)

# busines summary about any selcted stock 
business_details = tickerdata.info['longBusinessSummary']

st.header("**Stock History**")

st.info(business_details)

# st.write(tickerdata.info)




