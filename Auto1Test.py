
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

#Initializing Firefox web browser
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

#open website
driver.get("https://www.autohero.com/de/search/")
driver.maximize_window()

#Volkswagen
driver.find_element_by_id("carMakeFilter").click()
driver.find_element_by_css_selector("input[data-qa-selector='905']").click()
time.sleep(3)

#Golf
driver.find_element_by_xpath("//input[@data-qa-selector-value = 'Golf']").click()

#Select Max Mileage 25000 KM
driver.find_element_by_id("basicFilter").click()
beliebig = driver.find_element_by_id("rangeEnd")
dropdown_1 = Select(beliebig)
dropdown_1.select_by_index(2)
driver.find_element_by_id("basicFilter").click()
time.sleep(5)

driver.close()



