
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Atid_Store.Basic_Test.Locaters import *



def test_buy_store():
    driver = webdriver.Chrome()
    driver.get(atid_store_store_url)
    test_url = driver.current_url
    assert test_url == atid_store_new_url
    driver.maximize_window()
    driver.find_element(By.XPATH, click_store_button).click()
    store_title = driver.title
    assert store_title == 'Products – ATID Demo Store'
    time.sleep(3)
    driver.find_element(By.XPATH, click_store_product_item).click()
    time.sleep(3)
    driver.find_element(By.XPATH, click_addcart_store).click()
    time.sleep(3)
    driver.find_element(By.XPATH, click_store_view_cart).click()
    time.sleep(7)
    store_product = driver.find_element(By.XPATH, store_product_name ).text
    assert store_product == 'Anchor Bracelet'
    code_coupon_store = driver.find_element(By.XPATH, store_coupon_code)
    code_coupon_store.send_keys("jacob")
    time.sleep(3)
    code_coupon_store.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.close()



def test_buy_men():
    driver = webdriver.Chrome()
    driver.get(atid_store_store_url)
    new_atid_url = driver.current_url
    assert new_atid_url == atid_men_new_url
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH, click_men_button).click()
    men_title = driver.title
    assert men_title == 'Men – ATID Demo Store'
    time.sleep(3)
    driver.find_element(By.XPATH, click_product_item).click()
    time.sleep(3)
    driver.find_element(By.XPATH, click_add_cart).click()
    time.sleep(3)
    driver.find_element(By.XPATH, click_view_cart).click()
    time.sleep(7)
    men_product = driver.find_element(By.XPATH, insert_product_name).text
    assert men_product == 'ATID Blue Shoes'
    code_coupon = driver.find_element(By.XPATH,insert_coupon_code)
    code_coupon.send_keys("Sentayheu")
    time.sleep(3)
    code_coupon.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.close()



def test_buy_women():
    driver = webdriver.Chrome()
    driver.get(atid_store_women_url)
    test_url = driver.current_url
    assert test_url == atid_women_new_url
    driver.maximize_window()
    driver.find_element(By.XPATH, click_women_button).click()
    store_title = driver.title
    assert store_title == 'Women – ATID Demo Store'
    time.sleep(3)
    driver.find_element(By.XPATH, click_women_product_item).click()
    time.sleep(3)
    driver.find_element(By.XPATH, click_addcart_women).click()
    time.sleep(3)
    driver.find_element(By.XPATH, click_women_view_cart).click()
    time.sleep(7)
    store_product = driver.find_element(By.XPATH, women_product_name).text
    assert store_product == 'Basic Gray Jeans'
    code_coupon_store = driver.find_element(By.XPATH, women_coupon_code)
    code_coupon_store.send_keys("David")
    time.sleep(3)
    code_coupon_store.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.close()




def test_buy_women():
    driver = webdriver.Chrome()
    driver.get(atid_store_accessories_url)
    test_url = driver.current_url
    assert test_url == atid_accessories_new_url
    driver.maximize_window()
    driver.find_element(By.XPATH, click_accessories_button).click()
    store_title = driver.title
    assert store_title == 'Accessories – ATID Demo Store'
    time.sleep(3)
    driver.find_element(By.XPATH, click_accessories_product_item).click()
    time.sleep(3)
    driver.find_element(By.XPATH, click_addcart_accessories).click()
    time.sleep(3)
    driver.find_element(By.XPATH, click_accessories_view_cart).click()
    time.sleep(7)
    store_product = driver.find_element(By.XPATH, accessories_product_name).text
    assert store_product == 'Buddha Bracelet'
    code_coupon_store = driver.find_element(By.XPATH, accessories_coupon_code)
    code_coupon_store.send_keys("")
    time.sleep(3)
    code_coupon_store.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.close()


