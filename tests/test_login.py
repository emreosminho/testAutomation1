from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile

def test_google():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")  # Benzersiz profil dizini

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
