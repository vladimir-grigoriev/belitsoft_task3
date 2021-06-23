from selenium import webdriver

capabilities = {
    "browserName": "chrome",
    "browserVersion": "90.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

link = "http://localhost:8081/wd/hub"
driver_chrome = webdriver.Chrome
driver_selenoid = webdriver.Remote


driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

options = webdriver.ChromeOptions()
options.binary_location = binary_location

driver = webdriver.Chrome(
    executable_path=driver_location, chrome_options=options
)
