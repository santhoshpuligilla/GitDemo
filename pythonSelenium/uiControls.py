from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Automation\webdriver\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option3":
        checkbox.click()
        assert checkbox.is_selected()


print(driver.find_element_by_id("displayed-text").is_displayed())
driver.find_element_by_id("hide-textbox").click()
print(driver.find_element_by_id("displayed-text").is_displayed())

driver.close()