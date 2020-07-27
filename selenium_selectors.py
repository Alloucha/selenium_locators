
# 1. Submit filled test form https://demoqa.com/text-box


from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.find_element_by_css_selector('#userName').send_keys('Yulia Alloucha')
driver.find_element_by_css_selector('#userEmail').send_keys('pomelochka@gmail.com')
driver.find_element_by_css_selector('#currentAddress').send_keys('Ukraine, Kharkiv')
driver.find_element_by_css_selector('#permanentAddress').send_keys('Ukraine, Kharkiv')
driver.find_element_by_css_selector('#submit').click()
driver.quit()

# 2. Click on [Code in it] button after selecting new Category
# https://testpages.herokuapp.com/styled/basic-ajax-test.html

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://testpages.herokuapp.com/styled/basic-ajax-test.html")
desctop = Select(driver.find_element_by_css_selector('#combo1'))
desctop.select_by_index(1)
driver.find_element_by_css_selector('.styled-click-button').click()
driver.quit()

# 3. Print all text in Lorem/Ipsum/Dolor columns
# https://the-internet.herokuapp.com/challenging_dom#delete

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/challenging_dom#delete")
lorem_ipsum_dolor = driver.find_elements_by_css_selector('tbody tr')
for rows in lorem_ipsum_dolor:
    print(rows.find_element_by_css_selector('td:nth-child(1)').text)

for rows in lorem_ipsum_dolor:
    print(rows.find_element_by_css_selector('td:nth-child(2)').text)

for rows in lorem_ipsum_dolor:
    print(rows.find_element_by_css_selector('td:nth-child(3)').text)
driver.quit()
