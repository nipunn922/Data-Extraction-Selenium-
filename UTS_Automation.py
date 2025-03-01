import os
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class SeleniumNavigator:
    def __init__(self, driver_path):
        """Initialize the Selenium WebDriver."""
        self.driver_path = driver_path
        self.driver = None

    def start_browser(self):
        """Set up and start the WebDriver."""
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # Open browser in full-screen
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        print("Browser started successfully.")

    def navigate_to_url(self, url):
        """Navigate to a specified URL."""
        if self.driver is None:
            print("Error: Browser is not started. Call 'start_browser' first.")
            return
        self.driver.get(url)
        print(f"Navigated to {url}")

    def click_uts_login_button(self):
        """Click the UTS Login button."""
        try:
            uts_login_button = self.driver.find_element(By.CLASS_NAME, "btn-primary")
            uts_login_button.click()
            time.sleep(1)
            print("UTS Login button clicked successfully.")
        except NoSuchElementException:
            print("Error: UTS Login button not found on the page.")

    def fill_user_id(self, user_id):
        """Fill in the USER ID in the login input field."""
        try:
            user_id_field = self.driver.find_element(By.ID, "input27")
            user_id_field.clear()  # Clear any pre-filled text
            user_id_field.send_keys(user_id)  # Enter the USER ID
            print(f"Filled USER ID: {user_id}")
        except NoSuchElementException:
            print("Error: USER ID input field not found on the page.")

    def click_next_button(self):
        """Click the 'Next' button after entering login details."""
        try:
            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button-primary"))
            )
            next_button.click()
            print("Next button clicked successfully.")
        except NoSuchElementException:
            print("Error: 'Next' button not found on the page.")

    def fill_password(self, password):
        """Fill in the password in the login input field."""
        try:
            password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "input58"))
            )
            password_field.clear()
            password_field.send_keys(password)
            print("Password entered successfully.")
        except NoSuchElementException:
            print("Error: Password input field not found on the page.")

    def click_sign_in_button(self):
        """Click the 'Sign In' button."""
        try:
            sign_in_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button-primary"))
            )
            sign_in_button.click()
            print("Sign In button clicked successfully.")
        except NoSuchElementException:
            print("Error: Sign In button not found on the page.")

    def click_receive_code_button(self):
        """Click the 'Receive a code via SMS' button."""
        try:
            receive_code_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@value='Receive a code via SMS']"))
            )
            receive_code_button.click()
            print("Clicked the 'Receive a code via SMS' button successfully.")
        except NoSuchElementException:
            print("Error: 'Receive a code via SMS' button not found on the page.")

    def fill_otp(self):
        """Prompt the user for OTP and fill it into the OTP input field."""
        try:
            otp = input("Please enter the OTP you received: ")
            otp_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "input100"))
            )
            otp_field.clear()
            otp_field.send_keys(otp)
            print("OTP entered successfully.")
        except NoSuchElementException:
            print("Error: OTP input field not found on the page.")

    def click_submit_button(self):
        """Click the final 'Sign In' submit button."""
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@value='Sign In']"))
            )
            submit_button.click()
            print("Submit button clicked successfully.")
        except NoSuchElementException:
            print("Error: Submit button not found on the page.")

    def click_jobs_and_opportunities(self):
        """Click the 'Jobs and Opportunities' link."""
        try:
            jobs_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Jobs and opportunities"))
            )
            jobs_link.click()
            print("Clicked 'Jobs and Opportunities' link.")
        except NoSuchElementException:
            print("Error: 'Jobs and Opportunities' link not found.")

    def click_opportunity_type_button(self):
        """Click the 'Opportunity Type' button."""
        try:
            opportunity_type_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "typeOfWork"))
            )
            opportunity_type_button.click()
            print("Clicked 'Opportunity Type' button.")
        except NoSuchElementException:
            print("Error: 'Opportunity Type' button not found.")

    def select_any_option(self):
        """Select the 'Any' option from the dropdown menu."""
        try:
            any_option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//li[@role='presentation']/a[text()='Any']"))
            )
            any_option.click()
            print("Selected the 'Any' option.")
        except NoSuchElementException:
            print("Error: 'Any' option not found in the dropdown menu.")

    def click_search_button(self):
        """Click the 'Search' button."""
        try:
            search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "MpyzvluuSLiRel6YERiE"))
            )
            search_button.click()
            print("Clicked the 'Search' button successfully.")
        except NoSuchElementException:
            print("Error: 'Search' button not found on the page.")

    def click_load_more_seven_times(self):
        """Click the 'Load more results' button exactly 7 times."""
        try:
            for i in range(7):
                try:
                    load_more_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'job-search-results-list-load-more')]/button[@type='button' and contains(@class, 'btn btn-primary')]"))
                    )
                    load_more_button.click()
                    print(f"Clicked 'Load more results' button ({i + 1}/7).")
                    time.sleep(2)  # Allow time for new results to load
                except NoSuchElementException:
                    print("Error: 'Load more results' button not found. Stopping clicks.")
                    break
        except Exception as e:
            print(f"An error occurred while clicking 'Load more results': {e}")

    def extract_job_details(self):
        """Extract details from each job and return a list of dictionaries."""
        job_data_list = []
        try:
            job_titles = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "JoirwlVRON4KeFSOTWva"))
            )
            print(f"Found {len(job_titles)} job titles.")

            for i, job_title in enumerate(job_titles):
                try:
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", job_title)
                    print(f"Clicking job title {i + 1}: {job_title.text}")
                    job_title.click()
                    time.sleep(2)  # Wait for the job details page to load

                    # Extract the required details
                    job_data = {}

                    # Job Title
                    try:
                        job_data['Job Title'] = job_title.text.strip()  # Extract the job title
                    except Exception:
                        job_data['Job Title'] = "N/A"

                    # Name of the Company
                    try:
                        job_data['Name of the Company'] = self.driver.find_element(By.CLASS_NAME, "n6kS1cbw9MMsmuMHJNiw").text
                    except NoSuchElementException:
                        job_data['Name of the Company'] = "N/A"
                    time.sleep(1)

                    # Website
                    try:
                        website_element = self.driver.find_element(By.XPATH, "//a[contains(@class, 'btn btn-default') and text()='Website']")
                        job_data['Website'] = website_element.get_attribute("href")
                    except NoSuchElementException:
                        job_data['Website'] = "N/A"
                    time.sleep(1)

                    # Type of Opportunity
                    try:
                        opportunity_type = self.driver.find_element(By.XPATH, "//dl//dt[text()='Opportunity types']/following-sibling::dd//li").text
                        job_data['Type of Opportunity'] = opportunity_type
                    except NoSuchElementException:
                        job_data['Type of Opportunity'] = "N/A"
                    time.sleep(1)

                    # Expected Commencement
                    try:
                        expected_commencement = self.driver.find_element(By.XPATH, "//dl//dt[text()='Expected commencement']/following-sibling::dd").text
                        job_data['Expected Commencement'] = expected_commencement
                    except NoSuchElementException:
                        job_data['Expected Commencement'] = "N/A"
                    time.sleep(1)

                    # Residency Requirements
                    try:
                        residency_requirement = self.driver.find_element(By.XPATH, "//dl//dt[text()='Residency requirement']/following-sibling::dd").text
                        job_data['Residency Requirements'] = residency_requirement
                    except NoSuchElementException:
                        job_data['Residency Requirements'] = "N/A"
                    time.sleep(1)

                    # Date Posted
                    try:
                        date_posted = self.driver.find_element(By.XPATH, "//dl//dt[text()='Posted']/following-sibling::dd//span").text
                        job_data['Date Posted'] = date_posted
                    except NoSuchElementException:
                        job_data['Date Posted'] = "N/A"
                    time.sleep(1)

                    # Employer's Reference Code
                    try:
                        reference_code = self.driver.find_element(By.XPATH, "//dl//dt[text()=\"Employer's reference code\"]/following-sibling::dd").text
                        job_data["Employer's Reference Code"] = reference_code
                    except NoSuchElementException:
                        job_data["Employer's Reference Code"] = "N/A"
                    time.sleep(1)

                    # Closing Date
                    try:
                        closing_date = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Applications close on')]/span").text
                        job_data['Closing Date'] = closing_date
                    except NoSuchElementException:
                        job_data['Closing Date'] = "N/A"
                    time.sleep(1)

                    # Add extracted data to the list
                    job_data_list.append(job_data)

                    # Print the extracted data for verification
                    print(f"Extracted Data for Job {i + 1}: {job_data}")

                except Exception as e:
                    print(f"Error clicking job title {i + 1}: {e}")
                    break

            print("Completed extracting job details.")
            return job_data_list
        except NoSuchElementException:
            print("Error: No job titles found on the page.")
            return job_data_list
        
    def save_to_excel(self, job_data_list, folder_path):
        """Save the job details to an Excel file in the specified folder."""
        if job_data_list:
            os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist
            excel_file = os.path.join(folder_path, "job_details(161224).xlsx")  # Combine folder and file name
            df = pd.DataFrame(job_data_list)  # Convert list of dictionaries to a DataFrame
            df.to_excel(excel_file, index=False)  # Save to Excel
            print(f"Job details successfully saved to {excel_file}")
        else:
            print("No job data to save.")


# Usage Example
if __name__ == "__main__":
    driver_path = "/Users/nipunnkhurana/Desktop/chromedriver/chromedriver-mac-arm64/chromedriver"
    folder_path = "/Users/nipunnkhurana/Desktop/chromedriver/UTS jobs data"
    navigator = SeleniumNavigator(driver_path)
    navigator.start_browser()

    url = "https://careerhub.uts.edu.au/students/login?ReturnUrl=%2f"
    navigator.navigate_to_url(url)

    navigator.click_uts_login_button()
    navigator.fill_user_id("nipunn.khurana@student.uts.edu.au")  # Replace with your USER ID
    navigator.click_next_button()
    navigator.fill_password("**********")  # Replace with your password
    navigator.click_sign_in_button()
    navigator.click_receive_code_button()
    navigator.fill_otp()  # Prompted input for OTP
    navigator.click_submit_button()

    navigator.click_jobs_and_opportunities()
    navigator.click_opportunity_type_button()
    navigator.select_any_option()
    navigator.click_search_button()

    print("\nRepeating the Opportunity Type Selection...")
    navigator.click_opportunity_type_button()
    navigator.select_any_option()

    print("\nClicking 'Load more results' button 6 times...")
    navigator.click_load_more_seven_times()

    print("\nExtracting job details...")
    job_data_list = navigator.extract_job_details()

    # Print the collected job data
    print("\nExtracted Job Data:")
    for job_data in job_data_list:
        print(job_data)

    # Save the job data to Excel
        navigator.save_to_excel(job_data_list, folder_path)

    
