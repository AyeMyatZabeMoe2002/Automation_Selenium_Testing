from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class SwagTest: 

    def __init__(self): 
        self.driver = webdriver.Firefox()

    def open_browser(self):
        self.driver.get("https://www.saucedemo.com")
        print("Test 1: Open browser success")

    def login_test(self): 
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(2)
        self.driver.find_element(By.ID,"password").send_keys("secret_sauce",Keys.ENTER)
        print("Test 2: Login Success")
        time.sleep(2)

    def check_page_go(self): 
        ps = self.driver.page_source
        print("Test 3: Inventory Page Arrived " if "Products" in ps else "Wrong Page")
        time.sleep(2)

    def add_to_cart(self): 
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(2)
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie").click()
        time.sleep(2)
        print("Test 4: Add Items to Cart")
        time.sleep(2)
        
    def remove_item(self): 
        self.driver.find_element(By.ID,"remove-sauce-labs-backpack").click()
        time.sleep(2)
        print("Test 5: Remove Item from Cart")
    
    def view_order_item(self): 
        self.driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
        time.sleep(2)
        print("Test 6: View Order Item")

    def check_cart_page(self): 
        ps = self.driver.page_source
        print("Test 7: Item Cart Page Arrived" if "Your Cart" in ps else "Wrong Page!")

    def remove_item_from_cart(self): 
        self.driver.find_element(By.ID,"remove-sauce-labs-bolt-t-shirt").click()
        time.sleep(2)
        print("Test 8: Remove Item from Cart")

    def check_out(self): 
        self.driver.find_element(By.ID,"checkout").click()
        time.sleep(2)
        print("Test 9: Click Check Out Button")
    
    def check_check_out_page_go(self): 
        ps = self.driver.page_source
        print("Test 10: Checkout Success" if "Checkout: Your Information" in ps else "Not Success Checkout")

    def check_out_information(self): 
        self.driver.find_element(By.ID,"first-name").send_keys("QA")
        time.sleep(2)
        self.driver.find_element(By.ID,"last-name").send_keys("Testing")
        time.sleep(2)
        self.driver.find_element(By.ID,"postal-code").send_keys("111111")
        time.sleep(2)
        self.driver.find_element(By.ID,"continue").click()
        time.sleep(2)
        print("Test 11: Checkout Information Successful!")
    
    def checkout_payment(self): 
        item_total  = self.driver.find_element(By.CLASS_NAME,"summary_subtotal_label").text
        tax_total   = self.driver.find_element(By.CLASS_NAME,"summary_tax_label").text
        total_price = self.driver.find_element(By.CLASS_NAME,"summary_total_label").text
        print("Item total: ", item_total)
        print("Tax: ", tax_total)
        print("Total: ",total_price)
        print("Test 12: Payment Successful!")

    def finish(self): 
        self.driver.find_element(By.ID,"finish").click()
        time.sleep(2)
        ps = self.driver.page_source
        print("Text 13: Finish Page Arrived" if "Thank you for your order!" in ps else "Wrong Page!")


    def main(self): 
        self.open_browser()
        self.login_test()
        self.check_page_go()
        self.add_to_cart()
        self.remove_item()
        self.view_order_item()
        self.check_cart_page()
        self.remove_item_from_cart()
        self.check_out()
        self.check_check_out_page_go()
        self.check_out_information()
        self.checkout_payment()
        self.finish()

SwagTest().main()


