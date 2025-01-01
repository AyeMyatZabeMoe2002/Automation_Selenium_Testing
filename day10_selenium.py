from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


class TestRenovationTest:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def test_open_browser(self):
        self.driver.get("https://web-staging.renonation.sg/")
        self.driver.maximize_window()
        print("Test 1 : ", " Open Browser Success")

    def test_login1(self):

        mobile_text_box = "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/fieldset/div/div/input"
        mobile_btn = "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/button"
        otp_input_path = "/html/body/div/div/div[3]/div/div/form[2]/div/div/fieldset/div/div[2]/input"
        otp_path = "/html/body/div/div/div[3]/div/div/form[2]/div/div/fieldset/div/div[2]/ul/li"

        otp_code = ["2", "3", "2", "3", "2", "3"]

        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/header/div/div[2]/div/button[2]").click()

        self.driver.find_element(By.XPATH, mobile_text_box).send_keys("831")
        self.driver.find_element(By.XPATH, mobile_btn).click()
        invalid = self.driver.find_element(By.CSS_SELECTOR, ".flex-1.text-sm.text-error").text
        #self.driver.find_element(By.XPATH, mobile_text_box).clear()
        self.driver.find_element(By.XPATH, mobile_text_box).send_keys("16503")
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

    def test_login(self):
        mobile_text_box = "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/fieldset/div/div/input"
        mobile_number_next = "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/button"

        #Login btn
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/header/div/div[2]/div/button[2]").click()

        #mobile number
        self.driver.find_element(By.XPATH, mobile_text_box).send_keys("831")
        self.driver.find_element(By.XPATH, mobile_number_next).click()

        #Error Message
        invalid = self.driver.find_element(By.CSS_SELECTOR, ".flex-1.text-sm.text-error").text

        #mobile number
        self.driver.find_element(By.XPATH, mobile_text_box).send_keys("16503")
        self.driver.find_element(By.XPATH, mobile_number_next).click()
        time.sleep(2)
        #OTP Code
        self.driver.find_element(By.NAME, "otp").send_keys("232323", Keys.RETURN)


        print(invalid)
        print("Test 2 : ", "Login Success")

    def test_login_verify(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/header/div/div[2]/div/div[2]/div/div[1]/div/span").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/header/div/div[2]/div/div[2]/div/div[2]/a[1]/div/div/div").click()

        #URL Verify
        my_profile_url = "https://web-staging.renonation.sg/my-profile"
        url = self.driver.current_url
        if my_profile_url == url : print("Login Success!")
        else: print("Login Fail!")

    def test_logout(self):
        #profile click
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/header/div/div[2]/div/div[2]/div/div/div/span").click()

        #Logout Click
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/header/div/div[2]/div/div[2]/div/div[2]/div").click()

        #Logout btn
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[2]/form/div/div/button[2]").click()
        time.sleep(2)
        #self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div/svg").click()
        print("Test 4 : ", "Logout Success!")

    def test_sing_up(self):

         mobile_text_box = "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/fieldset/div/div/input"

         self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/header/div/div[2]/div/button[2]").click()
         self.driver.find_element(By.XPATH, mobile_text_box).send_keys("8311")

         #Random Number

         phone_number = str([random.randint(0,9) for i in range(4)])
         time.sleep(2)
         self.driver.find_element(By.XPATH, mobile_text_box).send_keys(phone_number)

         self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/button").click()
         time.sleep(2)

         #OTP Code
         self.driver.find_element(By.NAME, "otp").send_keys("232323", Keys.RETURN)

    def test_step_one(self):
        time.sleep(2)
        self.driver.find_element(By.ID, "firstName").send_keys("QA")
        time.sleep(2)
        self.driver.find_element(By.ID, "lastName").send_keys("Testing")

        time.sleep(2)
        email = "qa"
        num = [random.randint(0,9) for i in range(2)]
        num = "".join(str(x) for x in num)
        self.driver.find_element(By.ID, "email").send_keys(email, num, "@21.com")

        #btn Click
        self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div[2]/div/div[2]/button").click()
        print("Test 4: ", "Step One Complete")


    def test_main(self):
        self.test_open_browser()
        #self.test_login1()
        #self.test_login()
        #self.test_login_verify()
        #self.test_logout()
        self.test_sing_up()
        self.test_step_one()
        time.sleep(10)

TestRenovationTest().test_main()


# import random
#
# email ="QA"
#
# num = [random.randint(0,9) for i in range(2)]
#
# str = "".join(str(x) for x in num)
#
# print(str)
