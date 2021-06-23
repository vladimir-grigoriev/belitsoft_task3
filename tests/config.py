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

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.binary_location = binary_location

driver = webdriver.Chrome(
    executable_path=driver_location, options=chrome_options
)
