### pip install openpyxl and xlrd
import pandas as pd, numpy as np
from glob import glob

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import datetime
import numpy as np
from time import sleep
import pandas

start_date = datetime.date.fromisoformat('2019-07-01')
end_date = datetime.date.fromisoformat('2020-06-30')
date_range = pandas.date_range(start_date, end_date, freq='d')

try:
    chromedriver_PATH = r"C:\Users\hariiz\AppData\Local\Programs\Python\Python39\Scripts\Scripts\Hafiz\Selenium\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver_PATH)
    driver.implicitly_wait(3)
    driver.get("https://org.alldebitpay.com/adminUserAction/adminLogin.do")      
    driver.find_element(By.ID, "organId").send_keys("OID20171219500005")
    driver.find_element(By.ID, "loginName").send_keys("TripleA")
    driver.find_element(By.ID, "loginPassword").send_keys("tripleA123")
    sleep(7)
    driver.find_element(By.ID, "loginBtn").click()
    driver.get("https://org.alldebitpay.com/selectTradeAction/selectTrading.do")

    for date_series in date_range:
        date = date_series.date()
        date_string = date.strftime("%Y-%m-%d")
        start_date = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')[1]
        start_date.clear()
        start_date.send_keys(date_string)

        end_date = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')[3]
        end_date.clear()
        end_date.send_keys(date_string)
        
        driver.find_element(By.CSS_SELECTOR, 'option[value="3"]').click()
        driver.find_element(By.ID, "select").click()
        driver.find_element(By.CSS_SELECTOR, 'a[href="javascript:void(0);"]').click()
        field = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[class="l-btn-text"]')))
        field.click()

        filename = glob('D:\Downloads\Online+Transaction*.xls')[0]
        sheet_name = ''
        df = pd.read_excel(filename, engine = 'xlrd')
        col = df.columns

        #df.info()
        df.head()
        df.replace(np.nan, '', inplace=True)

        var1 = 'Transaction Amount'
        var2 = 'MDR&Others'
        var3 = 'Actual refund status'
        var4 = 'Pay Type'

        # refund status included
        value1 = df.sum(axis=0)[var1]
        value2 = df.sum(axis=0)[var2]

        paytype = df[var4][0] # loop to 5 -- df['Pay Type'].nunique()
        df_2 = df[df[var4]== paytype]
        value3 = df_2.sum(axis=0)[var1]
        value4 = df_2.sum(axis=0)[var2]
        paytype = ('-').join(paytype.split('-')[:2])

        month = date.strftime("%B")
        year = date.strftime("%Y")
        filename2 = f"dani-1{month} {year}.xlsx"
        op = pd.read_excel(filename2, engine = 'openpyxl')
        op.replace(np.nan, '', inplace=True)

        var1 = ' Transaction Amount '
        var2 = ' MDR&Others '
        var3 = ' Actual refund status '
        var4 = ' Pay Type '
        var5 = ' Txn Amount '

        #op.info()
        op.head()
        op.replace(np.nan, '', inplace=True)

        op_1 = op.T.set_index(2).T

        index = list(op_1.columns).index(var5)
        op_1.iloc[2+6,   index] = value1

        index = list(op_1.columns).index(var2)
        op_1.iloc[2+6,   index] = value2

        index = list(op_1.columns).index(paytype)
        op_1.iloc[1+6,   index] = value3
        op_1.iloc[1+6, index+1] = value4

        op_1.to_excel("output.xlsx", index = False)
        #op_1.to_excel("filename2", index = False)
except Exception as e:
    print(e)
    driver.quit()
