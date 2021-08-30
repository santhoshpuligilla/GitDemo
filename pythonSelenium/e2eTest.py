from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Automation\webdriver\chromedriver_win32\chromedriver.exe")
driver.get("https://amazon.in")
driver.maximize_window()

driver.find_element_by_id("twotabsearchtextbox").send_keys("iphone 12")
driver.find_element_by_id("nav-search-submit-button").click()
driver.find_element_by_css_selector("span[")
