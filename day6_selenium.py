from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def write_report_txt(test="",msg="", file_name = "report.txt"):
    with open(file_name, "a") as f:
        if test:
            f.write(f"Test : {test}\nMessage: {msg}\n{"="*30}\n")
        else:
            f.write(f"{msg}\n")

class SwagTest:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_browser(self):
        self.driver.get("https://www.saucedemo.com/")
        write_report_txt("Test 1: Open browser Success")


    def login_test(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce", Keys.ENTER)
        write_report_txt("Test 2: Login Success")
        time.sleep(2)


    def check_page_go(self):
        ps = self.driver.page_source
        write_report_txt("Test 3 : inventory Page Arrived " if "Products" in ps else "Wrong Page")

    def add_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        time.sleep(2)
        write_report_txt("Test 4 : Add Item to Cart")


    def remove_item(self):
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        time.sleep(2)
        write_report_txt("Test 5 : Remove 1 item")

    def view_order_item(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)
        write_report_txt("Test 6 : View Order Item")

    def check_cart_page_go(self):
        ps = self.driver.page_source
        time.sleep(2)
        write_report_txt("Test 7 : Cart Page Arrived " if "Your Cart" in ps else "Wrong Page!")

    def remove_item_from_cart(self):
        self.driver.find_element(By.ID, "remove-sauce-labs-onesie").click()
        time.sleep(2)
        write_report_txt("Test 8: Remove item from cart - Cart Page")

    def check_out(self):
        self.driver.find_element(By.ID, "checkout").click()
        write_report_txt("Test 9 : Click Check Out Button")

    def check_checkout_page_go(self):
        ps = self.driver.page_source
        time.sleep(2)
        write_report_txt("Test 10 : Checkout Page Arrived " if "Checkout: Your Information" in ps else "Wrong Page!")

    def check_out_information(self):
        self.driver.find_element(By.ID, "first-name").send_keys("QA")
        time.sleep(2)
        self.driver.find_element(By.ID, "last-name").send_keys("Testing")
        time.sleep(2)
        self.driver.find_element(By.ID, "postal-code").send_keys("11111")
        time.sleep(2)
        self.driver.find_element(By.ID, "continue").click()
        write_report_txt("Test 11 : Checkout Continue Success!")

    def check_payment(self):
        item_total = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
        tax_total = self.driver.find_element(By.CLASS_NAME, "summary_tax_label").text
        total_price = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        write_report_txt("Item Total : ", item_total)
        write_report_txt("Tax Price : ", tax_total)
        write_report_txt("Total Price : ", total_price)
        write_report_txt("Test 12 : Payment Success!")

    def finish(self):
        self.driver.find_element(By.ID, "finish").click()
        time.sleep(2)
        ps = self.driver.page_source
        write_report_txt("Test 13 : Finish Page Arrived " if "Thank you for your order!" in ps else "Wrong Page!")


    def main(self):
        self.open_browser()
        self.login_test()
        self.check_page_go()
        self.add_to_cart()
        self.remove_item()
        self.view_order_item()
        self.check_cart_page_go()
        self.remove_item_from_cart()
        self.check_out()
        self.check_checkout_page_go()
        self.check_out_information()
        self.check_payment()
        self.finish()

SwagTest().main()


#JSON JavaScript Object Notation

import json

# with open("student.json", "r") as f:
#     data = json.load(f)
#     data = json.dumps(data)
#     w = open("student.txt", "w")
#     w.write(data)
#     w.close()

# test1 = {
#     "name":  "Maung Maung",
#     "age": 26,
#     "Subjects": ["HTML", "CSS", "JavaScript", "Python", "Java", "PHP", "Nodejs"],
#     "phone": 9596664589,
#     "address" : "Rangoon, Burma."
# }


# print(type(test1))
#
# result = json.dumps(test1)
#
# print(result)
# print(type(result))


