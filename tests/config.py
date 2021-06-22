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
