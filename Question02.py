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



driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
wait=WebDriverWait(driver,10)
username=wait.until(EC.visibility_of_element_located((By.ID,'user-name')))
username.send_keys("standard_user")
password=wait.until(EC.visibility_of_element_located((By.ID,'password')))
password.send_keys("secret_sauce")
btn=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='login-button']")))
btn.click()
time.sleep(5)
title=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='title']")))
print("The title is :",title.text)
name=driver.find_elements(By.CLASS_NAME,"inventory_item_name ")
for i in range(len(name)):
    print(name[i].text)
price=driver.find_elements(By.XPATH,"//div[@class='inventory_item_price']")
for i in range(len(price)):
    print(price[i].text)
driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket").click()
time.sleep(5)
driver.close()

