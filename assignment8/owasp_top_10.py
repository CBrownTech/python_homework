import csv
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

os.chdir(os.path.dirname(os.path.abspath(__file__)))

PROJECT_URL = "https://owasp.org/www-project-top-ten/"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options,
)

try:
    driver.get(PROJECT_URL)

    top10_link = driver.find_element(
        By.XPATH,
        "//a[contains(@href,'owasp.org/Top10/2025')]",
    )
    driver.get(top10_link.get_attribute("href"))

    vulnerability_links = driver.find_elements(
        By.XPATH,
        "//ol/li/a[contains(@href,'/Top10/2025/A')]",
    )

    results = []
    for link in vulnerability_links:
        results.append(
            {
                "title": link.text.strip(),
                "href": link.get_attribute("href"),
            }
        )

    print(results)

    with open("owasp_top_10.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["title", "href"])
        for item in results:
            writer.writerow([item["title"], item["href"]])

    print(f"\nWrote {len(results)} rows to owasp_top_10.csv")
finally:
    driver.quit()
