from selenium import webdriver
driver=webdriver
driver = webdriver.Chrome(r"C:\Users\Naina\PycharmProjects\SeleniumTest\Browers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element_by_name("q").send_keys("javatpoint")
time.sleep(3)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(3)
driver.close()
print("sample test case successfully completed")



