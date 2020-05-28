from selenium import webdriver


chrome_browser = webdriver.Chrome('./chromedriver')

# Maximize window.
chrome_browser.maximize_window()

# Get url.
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# Check if title browser is 'Selenium Easy Demo'.
print(f'Title is Ok: {"Selenium Easy Demo" in chrome_browser.title}')

# Get the button text.
button = chrome_browser.find_element_by_class_name('btn-default')
print(button.get_attribute('innerHTML'))
