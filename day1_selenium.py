from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def log_in(): 
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.ID,"password").send_keys("secret_sauce", Keys.ENTER)
    time.sleep(2)
    text = driver.find_element(By.CLASS_NAME,"title").text
    print(text)
    time.sleep(2)
    driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
    time.sleep(2)
    driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div").click()
    time.sleep(2)
    text =  driver.find_element(By.CSS_SELECTOR,".inventory_details_name.large_size").text
    print(text)
    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div[1]/div[4]/div[2]/a/div").click()
    time.sleep(2)
    text = driver.find_element(By.CSS_SELECTOR,".inventory_details_name.large_size").text
    print(text)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
    time.sleep(2)
    driver.find_element(By.ID,"checkout").click()
    time.sleep(2)
    driver.find_element(By.ID,"first-name").send_keys("Testing")
    time.sleep(2)
    driver.find_element(By.ID,"last-name").send_keys("Testing")
    time.sleep(2)
    driver.find_element(By.ID,"postal-code").send_keys("1111")
    time.sleep(2)
    driver.find_element(By.ID,"continue").click()
    time.sleep(2)
    total_amount = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div[2]/div[8]").text
    print(total_amount)
    time.sleep(2)
    driver.find_element(By.ID,"finish").click()
    time.sleep(2)
    check_out = driver.find_element(By.CLASS_NAME,"title").text
    print(check_out)
    time.sleep(2)
    complete = driver.find_element(By.CLASS_NAME,"complete-header").text
    print(complete)
log_in()
