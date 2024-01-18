from selenium import webdriver

driver = webdriver.Edge()


driver.maximize_window()
driver.get("https://www.futurepedia.io/ai-tools")
driver.implicitly_wait(1000)


print(driver.title)
print(driver.current_url)

driver.close()