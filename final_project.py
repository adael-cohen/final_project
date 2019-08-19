# This program read and print the data from specific site using selenium
from selenium import webdriver
chrome_driver = webdriver.Chrome(executable_path="c:\\data\\webdriver\\chromedriver.exe")
chrome_driver.implicitly_wait(2)
chrome_driver.get("http://192.168.99.100:5000/")
# Read the data from the site
data = chrome_driver.find_element_by_xpath("/html/body").text
# Close the browser before ending the program
chrome_driver.close()
print(data)
