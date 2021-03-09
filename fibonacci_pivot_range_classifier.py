from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime

options = Options()

def pivot_points_fetch(base_urls):
    for i in base_urls:  
        driver = webdriver.Firefox(executable_path = r'/Users/judhjitganguli/Downloads/geckodriver', options = options)
        driver.get(i)
        delay = 5 #seconds
        now = datetime.now()
        
        print("Date and time : ", now)
        
        stock_name = driver.find_element_by_xpath(('//div[@id="stockName"]/h1'))
        stock_price = float(driver.find_element_by_xpath(('//div[@id="nsecp"]')).get_attribute("rel"))
        
        r1 = float(driver.find_element_by_xpath(('//div[@id="techan_daily"]/div/div/div[2]/div/div/table/tbody/tr[2]/td[2]')).text)
        r2 = float(driver.find_element_by_xpath(('//div[@id="techan_daily"]/div/div/div[2]/div/div/table/tbody/tr[2]/td[3]')).text)
        r3 = float(driver.find_element_by_xpath(('//div[@id="techan_daily"]/div/div/div[2]/div/div/table/tbody/tr[2]/td[4]')).text)
        
        Pivot_point = float(driver.find_element_by_xpath(('//div[@id="techan_daily"]/div/div/div[2]/div/div/table/tbody/tr[2]/td[5]')).text)

        s1 = float(driver.find_element_by_xpath(('//div[@id="techan_daily"]/div/div/div[2]/div/div/table/tbody/tr[2]/td[6]')).text)
        s2 = float(driver.find_element_by_xpath(('//div[@id="techan_daily"]/div/div/div[2]/div/div/table/tbody/tr[2]/td[7]')).text)
        s3 = float(driver.find_element_by_xpath(('//div[@id="techan_daily"]/div/div/div[2]/div/div/table/tbody/tr[2]/td[8]')).text)

        #vwap = driver.find_element_by_xpath(('//div[@id="stk_overview"]/div/div/div[2]/table/tbody/tr[1]/td[2]'))    
          
        print("Name : " + stock_name.text)
        print("Pivot Fibonacci ")
        print(Pivot_point)
        print("Price ")
        print(stock_price)
        
        if stock_price > r3:
            print("Above R3")
        if (stock_price < r3 and stock_price >r2):
            print("Between R2 and R3")
        if stock_price < r2 and stock_price >r1:
            print("Between R1 and R2")
        
        if stock_price < r1 and stock_price > Pivot_point:
            print("Between R1 and Pivot")
        
        if stock_price < Pivot_point and stock_price >s1:
            print("Between S1 and Pivot")
        if stock_price < s1 and stock_price >s2:
            print("Between S1 and S2")
        if stock_price < s2 and stock_price > s3:
            print("Between S2 and S3")
        if stock_price < s3:
            print("Below S3")

            
        driver.quit()

base_urls = ["https://www.moneycontrol.com/india/stockpricequote/auto-lcvshcvs/tatamotors/TM03"]

pivot_points_fetch(base_urls)