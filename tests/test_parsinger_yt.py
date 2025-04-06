from selenium import webdriver
from selenium.webdriver.common.by import By

def test_result_text():
    driver = webdriver.Chrome()
    driver.get('https://parsinger.ru/selenium/3/3.2.3/index.html')
    button_start = driver.find_element(By.ID, "showTextBtn")
    button_start.click()
    password_text = driver.find_element(By.ID, "text1")
    password_field = driver.find_element(By.ID, "userInput")
    password_field.send_keys(password_text.text)
    button_check = driver.find_element(By.ID, "checkBtn")
    button_check.click()
    result = driver.find_element(By.ID,"text2")

    assert result.text == "G00D-J0B-T0M-P0W3R"