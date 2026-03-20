"""
### Description
Open the Shine registration page using Selenium WebDriver (https://www.shine.com/registration/).

Automate the process of uploading a resume file using Selenium.

Perform the following steps:
- Launch the browser and open the Shine registration page
- Locate the **Upload Resume** file input field
- Upload a resume file


### Expected Outcome
- The browser launches and opens the Shine registration page
- Resume file is uploaded successfully
- The uploaded file name is reflected in the UI
- Script executes without errors
"""


from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time

a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)
driver.implicitly_wait(10)
driver.get("https://www.shine.com/registration/")
driver.maximize_window()
driver.find_element(By.ID,"id_file").send_keys(r"C:\Users\Yash\YashResume.pdf")
time.sleep(7)
driver.quit()