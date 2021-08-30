from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Automation\webdriver\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element_by_css_selector("#name").send_keys("Option3")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()