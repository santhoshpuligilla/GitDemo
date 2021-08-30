# Js DOM can access any elements on web page just like how selenium does
# selenium has a method to execute javascript code in it


from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Automation\webdriver\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").get_attribute("value"))

print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopButton = driver.find_element_by_css_selector("a[href*=shop]")
driver.execute_script('arguments[0].click();',shopButton)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

# driver.close()