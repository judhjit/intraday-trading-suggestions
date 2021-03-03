#Intraday Trading Suggestions

Oscillator is one of the technical indicators which help in predicting calls for stocks.

There are a number of Oscillator indicators like MACD (Moving Average Convergence/Divergence), ROC (Rate of Change), RSI (Relative Strength Index), etc.

We use Relative Strength Index (RSI). RSI is a popular oscillator that measures the extent of recent price xhanges rto determine overbought ot oversold conditions in an instruments price. It has become one of the most trusted indicators for anyone planning to use oscillators to determine buy and sell points. 

There are thousands of stocks listed on the NSE and BSE. The aim of this exercise is to streamline the process of selecting the stocks where we invest. We are only interested in those which have high volumes. (We need high volumes cause it ensure our orders will be met and not calcelled.) 

And hence, we choose the Top 100 stocks which have the highest volume in a trading session. 

Link - https://in.tradingview.com/markets/stocks-india/market-movers-active/

It lists the 100 most active stocks in a day (trading session). 

Steps - 
1. Scraping oscillator-data from a website
2. Classifying the stocks based on RSI into buy and sell. 
3. Exporting into .csv or .xlsx


To scrape the oscillator data, we need the selenium webdriver to load the Most-Active-Stocks webpage, and then select Oscillator Data (it has a dynamic table).
Then we scrape the html using BeautifulSoup and then load the parsed_heml into a pandas dataframe.

We use basic pandas operations to find out the top 10 stocks with highest and lowest RSI. 

If the RSI is >80, the stock has been overbought and will see correction. And if the RSI<30, the stock has been oversold and will now be bought. 

In the list of top 10, if we spot any stock in the oversold or over bought range, we could trade the stock with a reasonable target. 
