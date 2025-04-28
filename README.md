# 🚀 First Hands-On Selenium WebDriver Project

This project is my **first practice** using **Selenium WebDriver with Python**.  
It opens a Chrome browser, searches for a keyword on Google, clicks on a search result, and waits before closing the browser.

---

## 📚 Project Overview

- **Automation Tool**: Selenium WebDriver
- **Language**: Python
- **Browser**: Google Chrome
- **Driver**: ChromeDriver

---

## 🛠️ What This Script Does

1. Sets up ChromeDriver using Selenium.
2. Opens [Google](https://google.com).
3. Waits for the search bar to appear.
4. Types a keyword ("FACEBOOK") and hits the Enter key.
5. Waits for the search results to load.
6. Clicks on the search result link that mentions "Facebook".
7. Waits for 10 seconds on the page.
8. Closes the browser automatically.

---

## 🧩 Code Walkthrough

| Step | Description |
|:---|:---|
| `service = Service(executable_path="./chromedriver")` | Tell Selenium where the ChromeDriver file is located. |
| `driver = webdriver.Chrome(service=service)` | Launch Chrome using the service setup. |
| `driver.get("https://google.com")` | Open Google in the browser. |
| `WebDriverWait` | Wait until the Google search bar appears (max 10 seconds). |
| `input_element.send_keys("FACEBOOK" + Keys.ENTER)` | Type "FACEBOOK" and press Enter. |
| `driver.find_element(By.PARTIAL_LINK_TEXT, "Facebook")` | Find a link that partially matches "Facebook". |
| `link.click()` | Click on the Facebook link. |
| `time.sleep(10)` | Stay on the page for 10 seconds. |
| `driver.quit()` | Close the browser properly. |

---

## 📦 Requirements

- Python 3.x installed
- Install Selenium:

```bash
pip install selenium
