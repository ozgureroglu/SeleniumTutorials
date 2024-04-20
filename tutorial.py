# from selenium import webdriver

# PATH="/Users/ozgur/Development/Code/PYTHON/SELENIUM/chromedriver-mac-arm64/chromedriver"
# driver = webdriver.Chrome(PATH)
# driver.get("https://google.com")    


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

PATH="/Users/ozgur/Development/Code/PYTHON/SELENIUM/chromedriver-mac-arm64/chromedriver"

# Setup Chrome options
options = Options()
options.add_argument("--start-maximized")  # Open the browser in maximized mode

# Set up the service using ChromeDriverManager to handle the driver executable
service = Service(executable_path=PATH)

# Initialize the driver with the appropriate service and options
driver = webdriver.Chrome(service=service, options=options)

# Your code, e.g., to open a web page
driver.get("https://www.google.com")

# Close the driver; do not use if you want to keep the browser open
driver.quit()
