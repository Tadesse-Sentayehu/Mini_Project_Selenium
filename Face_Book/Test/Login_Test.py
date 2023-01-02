import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Face_Book.Basic_Test.Login_Locaters import *


def test_login_fb_both_null():
    driver = webdriver.Chrome()
    driver.get(get_facebook_url)
    driver.maximize_window()
    time.sleep(3)
    insert_Phone_Number = driver.find_element(By.XPATH, click_input_email)
    insert_Phone_Number.send_keys('')
    time.sleep(3)
    insert_password = driver.find_element(By.XPATH, click_input_password)
    insert_password.send_keys('')
    time.sleep(2)
    driver.find_element(By.XPATH, login_button).click()
    time.sleep(4)
    null_filed = driver.find_element(By.XPATH, page_both_null).text
    print(null_filed)
    driver.maximize_window()
    time.sleep(4)
    driver.close()

def test_login_fb_invalid_email_password():
    driver = webdriver.Chrome()
    driver.get(get_facebook_url)
    invalid_field = driver.current_url
    assert invalid_field == get_facebook_erl_new
    driver.maximize_window()
    time.sleep(3)
    insert_Phone_number = driver.find_element(By.XPATH, click_input_email)
    insert_Phone_number.send_keys('0866535636')
    time.sleep(3)
    insert_password = driver.find_element(By.XPATH, click_input_password)
    insert_password.send_keys('gsvgjhg')
    time.sleep(2)
    driver.find_element(By.XPATH, login_button).click()
    time.sleep(4)
    wrong_pass_email = driver.find_element(By.XPATH, invalid_password_and_email)
    print(wrong_pass_email)
    driver.maximize_window()
    time.sleep(4)
    driver.close()



def test_login_fb_invalid_email():

    driver = webdriver.Chrome()
    driver.get(get_facebook_url)
    invalid_email = driver.current_url
    assert invalid_email == get_facebook_erl_new
    driver.maximize_window()
    time.sleep(3)
    insert_Phone_number = driver.find_element(By.XPATH, click_input_email)
    insert_Phone_number.send_keys('0866535636')
    time.sleep(3)
    insert_password = driver.find_element(By.XPATH, click_input_password)
    insert_password.send_keys('david16#')
    time.sleep(2)
    driver.find_element(By.XPATH, login_button).click()
    time.sleep(4)
    driver.find_element(By.XPATH,page_email_invalid)
    # error_email = driver.current_url
    # assert error_email == page_email_invalid_new
    driver.close(4)
    time.sleep(4)
    driver.close()


def test_login_email_password_valid():

    driver = webdriver.Chrome()
    driver.get(get_facebook_url)
    valid_login = driver.current_url
    assert valid_login == get_facebook_erl_new
    driver.maximize_window()
    time.sleep(3)
    insert_Phone_number = driver.find_element(By.XPATH, click_input_email)
    insert_Phone_number.send_keys('0559477424')
    time.sleep(3)
    insert_password = driver.find_element(By.XPATH, click_input_password)
    insert_password.send_keys('david16#')
    time.sleep(2)
    driver.find_element(By.XPATH, login_button).click()
    time.sleep(4)
    driver.get(page)
    driver.maximize_window()
    time.sleep(4)
    driver.close()


def test_login_fb_invalid_password():

    driver = webdriver.Chrome()
    driver.get(get_facebook_url)
    invalid_password = driver.current_url
    assert invalid_password == get_facebook_erl_new
    driver.maximize_window()
    time.sleep(3)
    insert_Phone_number = driver.find_element(By.XPATH, click_input_email)
    insert_Phone_number.send_keys('0559477424')
    time.sleep(3)
    insert_password = driver.find_element(By.XPATH, click_input_password)
    insert_password.send_keys('ghfhfjjf')
    time.sleep(2)
    driver.find_element(By.XPATH, login_button).click()
    time.sleep(2)
    error_password = driver.find_element(By.XPATH, page_invalid_password).text
    print(error_password)
    time.sleep(5)
    driver.close()




