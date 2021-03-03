pip install selenium

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

import time
t0= time.clock()

# create object for firefox options
options = Options()

base_url = 'https://in.tradingview.com/markets/stocks-india/market-movers-active/'


#invoke the webdriver
driver = webdriver.Firefox(executable_path = r'/Users/judhjitganguli/Downloads/geckodriver',
                          options = options)


driver.execute_script('document.body.style.MozTransform = "scale(0.5)";')
print('Log: zoomed out')
driver.get(base_url)
driver.execute_script('document.body.style.MozTransform = "scale(0.5)";')
delay = 5 #seconds

try:
        #find tab/button
        osiButton = driver.find_element_by_css_selector('.tv-screener-toolbar__favorites div div div:nth-child(8)')
        print('Log: button text: ' + osiButton.text)
        osiButton.click()
        print('Log: Button Clicked')
        WebDriverWait(driver, 9).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'th:nth-child(2) .js-head-title'), "OSCILLATORS RATING"))
  

        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')

        
        oscillator_df = pd.concat(pd.read_html(html))
        
        print("Log: --- Oscillator Dataframe Created ---")
        
        #print(oscillator_df)
        
        #Dataframe is ready 
        
        #To find Buy and sell calls based on RSI 
        
        #Low RSI - BUY
        
        buy_df = oscillator_df.copy()
        buy_df = buy_df.sort_values(by='RSI14', ascending=True)
        
        
        #Look at only 10 stocks with lowest RSI
        
        buy_df.drop(buy_df.tail(90).index, inplace = True)
        print("Log: BUY")
        print(buy_df)
        
        
        #High RSI - SELL
        
        sell_df = oscillator_df.copy()
        sell_df = sell_df.sort_values(by='RSI14', ascending=False)
        
        #Look at only 10 stocks with lowest RSI

        sell_df.drop(sell_df.tail(90).index, inplace = True)
        print("Log: SELL")
        print(sell_df)
       
    
        #export to .csv
        oscillator_df.to_csv(r"/Users/judhjitganguli/Desktop/Intraday_Trading/csv/technical_oscillator_03-03-2020.csv", encoding='utf-8')
        print("Log: .csv created")
        #export to .xls
        with pd.ExcelWriter(r"/Users/judhjitganguli/Desktop/Intraday_Trading/excel/technical_oscillator_03-03-2020.xlsx") as writer:
            oscillator_df.to_excel(writer, sheet_name='All_data')
            print("Log: Main sheet created")
            buy_df.to_excel(writer, sheet_name='Buy')
            print("Log: Buy sheet created")
            sell_df.to_excel(writer, sheet_name='Sell')
            print("Log: Sell sheet created")
            print("Log: .xlsx created")
        
except Exception as ex:
        print(ex)
    


t1 = time.clock() - t0
print("Time elapsed: ", t1) # CPU seconds elapsed (floating point)

# close the automated browser
driver.quit()