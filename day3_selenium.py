from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time

class ParaBank: 
    
    def __init__(self):
        self.driver = webdriver.Firefox()

    def open_browser(self): 
        self.driver.get("https://parabank.parasoft.com/")
        self.driver.maximize_window()
        print("Test 1: Open Page Success")
        
    def register(self): 
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div/p[2]/a").click()
        time.sleep(3)
        print("Test 2: Click to Register Button")
        self.driver.find_element(By.ID,"customer.firstName").send_keys("AyeMyat")
        time.sleep(3)
        self.driver.find_element(By.ID,"customer.lastName").send_keys("ZabeMoe")
        time.sleep(3)
        self.driver.find_element(By.ID,"customer.address.street").send_keys("On Nut")
        time.sleep(3)
        self.driver.find_element(By.ID,"customer.address.city").send_keys("Bangkok")
        time.sleep(3)
        self.driver.find_element(By.ID,"customer.address.state").send_keys("Thailand")
        time.sleep(3)
        self.driver.find_element(By.ID,"customer.address.zipCode").send_keys("11111")
        time.sleep(3)
        self.driver.find_element(By.ID,"customer.phoneNumber").send_keys("0638191525")
        time.sleep(3)
        self.driver.find_element(By.ID,"customer.ssn").send_keys("12/ktn(N)145778")
        time.sleep(3)
        self.driver.find_element(By.ID,"customer.username").send_keys("AyeMyat")
        time.sleep(3)
        self.driver.find_element(By.ID,"customer.password").send_keys("123456")
        time.sleep(3)
        self.driver.find_element(By.ID,"repeatedPassword").send_keys("123456",Keys.ENTER)
        time.sleep(3)
        print("Test 3: Regsiter Information Successfully")
    
    def login(self): 
        self.driver.find_element(By.NAME,"username").send_keys("AyeMyat")
        time.sleep(3)
        print("Test 4: Username Compelete!")
        self.driver.find_element(By.NAME,"password").send_keys("123456",Keys.ENTER)
        time.sleep(3)
        print("Test 5: Password Complete")
        print("Test 6: Login Successfully")
      
    def check_overview(self): 
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/ul/li[2]/a").click()
        time.sleep(3)
        print("Test 7: Account Overview Link Open")
        account = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[1]/a").text
        time.sleep(3) 
        balance = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]").text
        time.sleep(3)
        account_overview = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[3]").text
        time.sleep(3)
        print("Account: ",account)
        print("Balance: ",balance)
        print("Account Overview: ",account_overview)
        print("Test 8: Account Overview Succesfully!")

    def main(self): 
        self.open_browser()
        self.register()
        self.login()
        self.check_overview()


ParaBank().main()