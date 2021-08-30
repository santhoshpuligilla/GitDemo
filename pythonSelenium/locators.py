from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Automation\webdriver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()

# driver.find_element_by_name("name").send_keys("Rahul")
driver.find_element_by_css_selector("input[id='twotabsearchtextbox']").send_keys("iPhone 12")
driver.find_element_by_css_selector("input[id='nav-search-submit-button']").click()

driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").clear()
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("Samsung M21")
driver.find_element_by_xpath("//input[@id='nav-search-submit-button']").click()
#driver.find_element_by_css_selector("//*[contains(@id,'searchtext')]").clear()
