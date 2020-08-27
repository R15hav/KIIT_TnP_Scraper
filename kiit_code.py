
#---------------Imports-----------------------------
import os
import csv
from datetime import date
import requests
from bs4 import BeautifulSoup 
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class scrape:
    def __init__(self):
        self.pay_load=[]
        self.notice_list=[]
        self.new_notice=[]
        self.driver=None
        self.wait=None
        self.today = date.today()
        self.date= self.today.strftime("%d-%b-%Y")

    #----------------------------------Starting Selenium to login---------------------------------
    def start_sel(self):
        self.driver=webdriver.Firefox(executable_path="Your geko driver location/path") # For eg:-D:\python\Automation proj\selenium_driver\geckodriver.exe
        self.driver.get("https://kiittnp.in/ea19b38134d463acc8c7b66744a481847ab4b/login.html")

        self.wait=WebDriverWait(self.driver,500)
        self.wait.until(lambda driver: self.driver.find_element_by_id('pwd'))

    #-------------------------------------------Login---------------------------------------------
    def login(self):
        self.driver.find_element_by_id('usr').send_keys("Enter your id") #Enter your id here
        self.driver.find_element_by_id('pwd').send_keys('Enter your password') #Enter your password
        self.driver.find_element_by_id('login').click()
        
        self.wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="main-notice"]/section/div/div/div[1]/div/div[3]/a/button'))

        new_url=self.driver.window_handles[0]
        self.driver.switch_to.window(new_url)

    #-------------------------------------------- Parsing -----------------------------------------
    def parse(self):
        html=self.driver.page_source
        self.driver.quit()
        soup=BeautifulSoup(html,"html.parser")
        post=soup.findAll(class_='user row')

        for i in post:
            if self.date in i.find(id="badge-post").get_text():
                self.notice_list.append(i)

    #--------------------------------------getting values to csv file-------------------------------
    def get_values(self):
        if os.stat('notice.csv').st_size == 0:
            with open("notice.csv","a",newline='') as file:
                csv_writer=csv.writer(file)
                for p in self.notice_list:
                    self.pay_load.append([p.find(id="badge-post").get_text(),p.find(id="heading").get_text(),p.find(id="expires").get_text()])
                    csv_writer.writerow([p.find(id="badge-post").get_text(),p.find(id="heading").get_text(),p.find(id="expires").get_text()])
            file.close()
        else:
            with open("notice.csv") as file:
                csv_reader=csv.reader(file)
                read=list(next(csv_reader))
            try:
                x=read.index(self.notice_list[0].find(id="heading").get_text())
                self.pay_load='No new notice'
            except ValueError:
                with open("notice.csv") as file:
                    csv_reader=csv.reader(file)
                    row=list(next(csv_reader))
                self.pay_load=[]
                for p in self.notice_list:
                    if self.date in p.find(id="badge-post").get_text():
                        try:
                            row.index(p.find(id="heading").get_text())
                            break
                        except ValueError:
                            self.new_notice.append([p.find(id="badge-post").get_text(),p.find(id="heading").get_text(),p.find(id="expires").get_text()])
                            self.pay_load.append([p.find(id="badge-post").get_text(),p.find(id="heading").get_text(),p.find(id="expires").get_text()])
                with open("notice.csv") as file:
                    csv_reader=csv.reader(file)
                    for row in csv_reader:
                        self.new_notice.append(row)
                f=open("notice.csv","w+")
                f.close()
                with open("notice.csv","a",newline='') as file:
                    csv_writer=csv.writer(file)
                    for i in self.new_notice:
                        csv_writer.writerow(i)
                file.close()  
        return self.pay_load                         

