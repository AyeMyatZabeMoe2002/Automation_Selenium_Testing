from time import time_ns

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import random
import time

class TestYoga:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def test_open_browser(self):
        self.driver.get("https://webfront-uat.yogamovement.com/")
        self.driver.maximize_window()
        time.sleep(2)
        #Box close
        self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/button").click()
        print("Test 1: open browser success")

    def test_sing_up(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/div/div/nav[1]/ul/li[1]/a").click()
        time.sleep(1)
        user_email = "qa"
        ram = [str(random.randint(0,9)) for i in range(3)]
        ra = "".join(ram)
        self.driver.find_element(By.NAME, "email").send_keys(user_email,ra,"@yopmail.com")
        time.sleep(1)
        self.driver.find_element(By.NAME, "password").send_keys("123456", Keys.RETURN)
        time.sleep(5)

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

        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[2]/input").send_keys("93748",ra)

        #DOB
        self.driver.find_element(By.ID, "dob").click()
        time.sleep(2)

        #Year
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[2]/option[59]").click()

        Select(self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[2]")).select_by_value("1989")
        time.sleep(2)

        #Month
        Select(self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[1]")).select_by_value("4")
        time.sleep(2)

        #Day
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/div[1]").click()
        time.sleep(2)

        #Country
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[5]/div/div[1]/div/div/div/div[2]/div").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[text()='Thailand']").click()
        time.sleep(5)


        #btn
        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[6]/div/button").click()


        print("Test 2 : Sing Up Success")


    def test_sing_in(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/div/div/nav[1]/ul/li[2]/a").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "email").send_keys("waiwai60@yopmail.com")
        time.sleep(2)
        self.driver.find_element(By.NAME, "password").send_keys("Phy123", Keys.RETURN)
        time.sleep(5)

        #Buy A Class Pack

        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div[2]/a[2]/div/button[1]").click()
        time.sleep(3)

        #All Access
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/ul/li[2]/a").click()
        time.sleep(2)

        #All Access Pass +
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/section[2]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/section[2]/div[2]/div[1]/div[4]/button").click()
        time.sleep(2)

        #Order Preview
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/form/button").click()
        time.sleep(3)

        img = "/Users/user/Desktop/data/Screenshot 2024-11-20 at 19.35.02.png"
        #image_upload
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/label/input").send_keys(img)
        time.sleep(2)

    def test_payment(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/button").click()
        time.sleep(5)

        js_code = """let element = document.querySelector("input[name='hidden']")
        element.disable = false
        return element"""

        iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe[name^='__privateStripeFrame'][title='Secure card number input frame']")
        time.sleep(2)
        self.driver.switch_to.frame(iframe)
        self.driver.execute_script(js_code)

        self.driver.find_element(By.NAME, "cardnumber").send_keys("4111111111111111")
        self.driver.switch_to.default_content()
        time.sleep(3)

        #Exp Date
        iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe[name^='__privateStripeFrame'][title='Secure expiration date input frame']")
        time.sleep(2)
        self.driver.switch_to.frame(iframe)
        self.driver.execute_script(js_code)

        self.driver.find_element(By.NAME, "exp-date").send_keys("12/26")
        self.driver.switch_to.default_content()
        time.sleep(2)

        #CVC
        iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe[name^='__privateStripeFrame'][title='Secure CVC input frame']")

        time.sleep(2)
        self.driver.switch_to.frame(iframe)
        self.driver.execute_script(js_code)

        self.driver.find_element(By.NAME, "cvc").send_keys("123")
        self.driver.switch_to.default_content()


    def main(self):
        self.test_open_browser()
        #self.test_sing_up()
        self.test_sing_in()
        self.test_payment()
        time.sleep(10)


TestYoga().main()