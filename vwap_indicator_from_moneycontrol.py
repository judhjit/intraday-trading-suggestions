from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime

options = Options()

def VWAP_indicator(base_urls):
    for i in base_urls:  
        driver = webdriver.Firefox(executable_path = r'/Users/judhjitganguli/Downloads/geckodriver', options = options)
        driver.get(i)
        delay = 5 #seconds
        now = datetime.now()
        
        print("Date and time : ", now)
    
        stock_name = driver.find_element_by_xpath(('//div[@id="stockName"]/h1'))
        stock_price = driver.find_element_by_xpath(('//div[@id="nsecp"]'))
        vwap = driver.find_element_by_xpath(('//div[@id="stk_overview"]/div/div/div[2]/table/tbody/tr[1]/td[2]'))    
          
        print("VWAP" + vwap.text)
        print("Name : " + stock_name.text")
        print("Stock Price " + stock_price.get_attribute("rel"))
        
        if stock_price.get_attribute("rel") > vwap.text:
            print ("BULLISH")
        else:
            print("BEARISH")
            
        driver.quit()

#Add all moneycontrol stock links you want the VWAP analysis for

base_urls = ["https://www.moneycontrol.com/india/stockpricequote/auto-lcvshcvs/tatamotors/TM03", "https://www.moneycontrol.com/india/stockpricequote/retail/adityabirlafashionretail/PFR"]

VWAP_indicator(base_urls)