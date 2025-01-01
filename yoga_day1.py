from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

class TestYoga:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def test_open_browser(self):
        self.driver.get("https://webfront-uat.yogamovement.com/")
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/button").click()
        print("Test 1: open browser success")

    def test_sing_up(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/div/div/nav[1]/ul/li[1]/a").click()
        time.sleep(1)
        user_email = "qa21@yopmail.com"
        self.driver.find_element(By.NAME, "email").send_keys(user_email)
        time.sleep(1)
        self.driver.find_element(By.NAME, "password").send_keys("123456", Keys.RETURN)
        time.sleep(2)

        #First Name
        self.driver.find_element(By.NAME, "firstname").send_keys("QA")
        time.sleep(2)

        #Last Name
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[1]/label/input").send_keys("Testing")
        time.sleep(2)

        #Email Check
        email = self.driver.find_element(By.NAME, "email")
        val = email.get_attribute("value")
        if val == user_email : print("Email Match")
        else : print("Not Email Match")

        #I Identify as *
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[4]/div/div/div[2]/div/div[1]/label/div/div").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[1]").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[2]/div[1]/input").send_keys("Myanmar")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[2]/div[4]/div[1]").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[2]/input").send_keys("93748329")

        #DOB
        self.driver.find_element(By.ID, "dob").click()
        time.sleep(2)

        #Year
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[2]/option[59]").click()

        Select(self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[2]")).select_by_value("1989")

        #year

        print("Test 2 : Sing Up Success")

    def main(self):
        self.test_open_browser()
        self.test_sing_up()
        time.sleep(10)


TestYoga().main()