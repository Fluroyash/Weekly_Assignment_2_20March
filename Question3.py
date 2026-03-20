"""
### Title

**Automate Data Extraction from Pro Kabaddi Standings**

### Description

Open the Pro Kabaddi website using Selenium WebDriver (https://www.prokabaddi.com/)
Navigate to the **Standings** section and locate the team **Jaipur Pink Panthers** in the points table.

Identify and extract the following details for the team:

* Matches Played
* Won
* Lost
* Score Difference (Diff)
* Points

Use appropriate locator strategies such as **XPath / CSS Selectors** to fetch the data dynamically from the table.

Students should ensure that:

* The browser opens successfully.
* Navigation to the standings page is completed.
* The correct team row (**Jaipur Pink Panthers**) is identified.
* All required values are extracted correctly.

### Expected Outcome

* The browser launches and opens the Pro Kabaddi website.
* The Standings page is displayed.
* The row corresponding to **Jaipur Pink Panthers** is located.
* Matches Played, Won, Lost, Diff, and Points are successfully fetched.
* The extracted values are printed in the console.
"""

from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)


driver.implicitly_wait(10)
driver.get("https://www.prokabaddi.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@href='https://www.prokabaddi.com/standings']").click()
driver.find_element(By.XPATH,"(//div[@class='row-head'])[8]")
match=driver.find_element(By.XPATH,"(//p[@class='count'])[36]")
print("Match Played : ",match.text)
won=driver.find_element(By.XPATH,"(//p[@class='count'])[37]")
print("Matches won:",won.text)
lost=driver.find_element(By.XPATH,"(//p[@class='count'])[38]")
print("Matches Lost : ",lost.text)
scorediff=driver.find_element(By.XPATH,"(//p[@class='count'])[39]")
print("Score difference",scorediff.text)
points=driver.find_element(By.XPATH,"(//p[@class='count'])[40]")
print("Points",points.text)
driver.quit()