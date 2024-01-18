from selenium import webdriver

driver = webdriver.Chrome()


driver.maximize_window()
driver.get("https://www.futurepedia.io/ai-tools")
driver.implicitly_wait(1000)


print(driver.title)
print(driver.current_url)


driver.close()