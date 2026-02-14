import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")        # Run without UI
    chrome_options.add_argument("--disable-gpu")  # Recommended for Windows
    # chrome_options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only capture screenshot if test failed
    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            screenshot = driver.get_screenshot_as_png()

            # Attach screenshot in Allure Report
            allure.attach(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
