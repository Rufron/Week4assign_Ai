# Requires: selenium, webdriver-manager
# pip install selenium webdriver-manager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login(url, username, password, expect_success=True):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Uncomment for headless mode (no browser UI)
    # options.add_argument("--headless")

    # ✅ Correct way to initialize Chrome now:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(1)
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)

        if expect_success:
            success = "logged into" in driver.page_source.lower()
            return success
        else:
            error_present = "invalid username" in driver.page_source.lower()
            return error_present
    finally:

        driver.save_screenshot("login_result.png")

        driver.quit()

if __name__ == "__main__":
    print(test_login("https://practicetestautomation.com/practice-test-login/", "student", "Password123", True))
    print(test_login("https://practicetestautomation.com/practice-test-login/", "baduser", "wrongpass", False))
