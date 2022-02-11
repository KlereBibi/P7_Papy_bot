""" this module is the fonctional test """

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_fonctionnal_application():
    
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.implicitly_wait(30)

    
    driver.get("http://127.0.0.1:5000/")

    
    search_field = driver.find_element(By.ID, "userText")
    search_field.clear()

    
    search_field.send_keys("Claire")
    search_field.submit()

    response = driver.find_element(By.CLASS_NAME, "papy").text

    expected_value = "Le Claire, Scott County, Iowa, United States of America"

    assert response == expected_value

    driver.close()
    