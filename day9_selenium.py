from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRenovationTest:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def test_open_browser(self):
        self.driver.get("https://web-staging.renonation.sg/")
        self.driver.maximize_window()
        print("Test 1 : ", " Open Browser Success")

    def test_login(self):

        mobile_text_box = "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/fieldset/div/div/input"
        mobile_btn = "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/button"
        otp_input_path = "/html/body/div/div/div[3]/div/div/form[2]/div/div/fieldset/div/div[2]/input"
        otp_path = "/html/body/div/div/div[3]/div/div/form[2]/div/div/fieldset/div/div[2]/ul/li"

        otp_code = ["2", "3", "2", "3", "2", "3"]

        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/header/div/div[2]/div/button[2]").click()

        self.driver.find_element(By.XPATH, mobile_text_box).send_keys("831")
        self.driver.find_element(By.XPATH, mobile_btn).click()
        invalid = self.driver.find_element(By.CSS_SELECTOR, ".flex-1.text-sm.text-error").text
        self.driver.find_element(By.XPATH, mobile_text_box).clear()
        self.driver.find_element(By.XPATH, mobile_text_box).send_keys("83116503")
        self.driver.find_element(By.XPATH, mobile_btn).click()
        time.sleep(2)

        #OTP Code

        self.driver.find_element(By.XPATH, otp_input_path).send_keys("".join(otp_code))

        for i,otp in enumerate(otp_code, start=1):
            li_path = f"{otp_path}[{i}]"
            otp_element = self.driver.find_element(By.XPATH, li_path)
            self.driver.execute_script("arguments[0].textcontent = arguments[1];", otp_element, otp_code)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/form[2]/div/div/button").click()
        print(invalid)
        print("Test 2 : ", "Login Success")




    def test_main(self):


        self.test_open_browser()
        self.test_login()


TestRenovationTest().test_main()