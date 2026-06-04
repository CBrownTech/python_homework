import json
import os

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

os.chdir(os.path.dirname(os.path.abspath(__file__)))

URL = (
    "https://durhamcounty.bibliocommons.com/v2/search"
    "?query=learning%20spanish&searchType=smart"
)

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options,
)

try:
    driver.get(URL)

    entries = driver.find_elements(By.CSS_SELECTOR, "li.cp-search-result-item")
    results = []

    for entry in entries:
        title = entry.find_element(
            By.CSS_SELECTOR, "h3.cp-title span.title-content"
        ).text

        author_links = entry.find_elements(By.CSS_SELECTOR, "a.author-link")
        authors = [link.text.strip() for link in author_links if link.text.strip()]
        author = "; ".join(authors)

        format_div = entry.find_element(By.CSS_SELECTOR, "div.cp-format-info")
        format_year = format_div.find_element(
            By.CSS_SELECTOR, "span.display-info-primary"
        ).text

        results.append(
            {
                "Title": title,
                "Author": author,
                "Format-Year": format_year,
            }
        )

    df = pd.DataFrame(results)
    print(df)

    df.to_csv("get_books.csv", index=False, encoding="utf-8")

    with open("get_books.json", "w", encoding="utf-8") as json_file:
        json.dump(results, json_file, indent=4)

    print(f"\nWrote {len(results)} records to get_books.csv")
    print(f"Wrote {len(results)} records to get_books.json")
finally:
    driver.quit()
