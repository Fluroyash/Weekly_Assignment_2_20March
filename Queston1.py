"""
## Practical Exercise 2

### Title
**Automate SauceDemo Login and Product Page with Explicit Waits and Verification**

### Description
Open the SauceDemo website using Selenium WebDriver (https://www.saucedemo.com/).

Implement the login flow and product page interactions using **Explicit Waits** to ensure elements are properly loaded and interactable.

Perform the following steps:
- Wait for the **Username** field to be clickable and enter `"standard_user"`
- Wait for the **Password** field to be clickable and enter `"secret_sauce"`
- Wait for the **Login** button to be clickable and click on it
- After login, wait for the **Products title** to be visible
- Capture and print the page title text

Continue with product page actions:
- Find ALL product names and print each name
- Find ALL product prices and print each price
- Click on the fourth product’s **Add to cart** button


Use **WebDriverWait** along with **Expected Conditions** for synchronization.

Students should ensure that:
- Explicit waits are used for each interaction step
- No `sleep()` is used in the script
- At least **2 different locator strategies** are used (ID, CSS Selector, XPath, Class Name, etc.)
- Proper comments are added explaining locator usage

### Expected Outcome
- The browser launches and opens the SauceDemo website
- Login is performed successfully using explicit waits
- The **"Products"** page is displayed after login
- Page title is printed as **Products**
- All product names and prices are printed in the console
- First product is added to cart
- Script executes without timing issues
"""


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)

driver.get("https://www.saucedemo.com")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

wait.until(EC.element_to_be_clickable((By.ID, "user-name"))).send_keys("standard_user")
wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("secret_sauce")
wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
print("Page Title:", title.text)

names = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
print("\nProduct Names:")
for n in names:
    print(n.text)

prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
print("\nProduct Prices:")
for p in prices:
    print(p.text)

buttons = driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
buttons[3].click()

print("\n4th product added to cart")
driver.quit()

