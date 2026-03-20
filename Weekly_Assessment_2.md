## Practical Exercise 1

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

---



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

---


## Practical Exercise  3

### Title  
**Automate Resume Upload on Shine Registration Page**

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