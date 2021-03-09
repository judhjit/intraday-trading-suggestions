from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime
import threading

options = Options()

def VWAP_indicator(base_urls):
        driver = webdriver.Firefox(executable_path = r'/Users/judhjitganguli/Downloads/geckodriver', options = options)
        driver.get(base_urls)
        delay = 5 #seconds
        now = datetime.now()
        
        print("Date and time : ", now)
    
        stock_name = driver.find_element_by_xpath(('//div[@id="stockName"]/h1'))
        stock_price = driver.find_element_by_xpath(('//div[@id="nsecp"]'))
        vwap = driver.find_element_by_xpath(('//div[@id="stk_overview"]/div/div/div[2]/table/tbody/tr[1]/td[2]'))    
          
        print("VWAP" + vwap.text)
        print("Name : " + stock_name.text)
        print("Stock Price " + stock_price.get_attribute("rel"))
        
        if stock_price.get_attribute("rel") > vwap.text:
            print ("BULLISH")
        else:
            print("BEARISH")
            
        driver.quit()

#Add all moneycontrol stock links you want the VWAP analysis for

import threading

if __name__ == "__main__": 
    # creating thread 
    # add all moneycontrol stock links you want the VWAP analysis for
    t1 = threading.Thread(target=VWAP_indicator, args=("https://www.moneycontrol.com/india/stockpricequote/auto-lcvshcvs/tatamotors/TM03",)) 
    t2 = threading.Thread(target=VWAP_indicator, args=("https://www.moneycontrol.com/india/stockpricequote/retail/adityabirlafashionretail/PFR",)) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 

    print("Done")
  