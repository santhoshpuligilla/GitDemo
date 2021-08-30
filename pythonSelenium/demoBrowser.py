from selenium import webdriver

# browser exposes an executable file
driver = webdriver.Chrome(executable_path="C:\\Automation\webdriver\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")

print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/#/practice-project")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()
