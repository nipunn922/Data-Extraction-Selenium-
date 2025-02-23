import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import datetime


class SeekJobList:
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
    
    def enter_keyword(self, keyword):
        """Enter the desired keyword in the search field."""
        try:
            wait = WebDriverWait(self.driver, 10)
            keyword_field = wait.until(EC.presence_of_element_located((By.ID, "keywords-input")))
            keyword_field.clear()  # Clear any pre-filled text
            keyword_field.send_keys(keyword)  # Enter the keyword
            print(f"Searching for: {keyword}")
        except TimeoutException:
            print("Error: Keyword input field not found within the timeout period.")

    def select_location(self, location):
        """Select a location using the location input field."""
        try:
            time.sleep(1)
            wait = WebDriverWait(self.driver, 10)
            location_field = wait.until(EC.presence_of_element_located((By.ID, "SearchBar__Where")))
            location_field.clear()  # Clear any pre-filled text
            location_field.send_keys(location)  # Enter the location
            print(f"Location set to: {location}")
        except TimeoutException:
            print("Error: Location input field not found within the timeout period.")

    def click_seek_button(self):
        """Click the SEEK button to submit the search."""
        try:
            wait = WebDriverWait(self.driver, 10)
            seek_button = wait.until(EC.element_to_be_clickable((By.ID, "searchButton")))
            seek_button.click()
            print("SEEK button clicked successfully.")
        except TimeoutException:
            print("Error: SEEK button not clickable within the timeout period.")

    def extract_job_details(self):
        """Extract details from each job and return a list of dictionaries."""
        job_data_list = []
        try:
            # Locate all job titles on the page
            job_titles = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[data-testid='job-list-item-link-overlay']"))
            )
            print(f"Found {len(job_titles)} jobs on the page.")

            for i, job_title in enumerate(job_titles):
                try:
                    # Scroll into view and click the job link
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", job_title)
                    print(f"Clicking job {i + 1}: {job_title.text}")
                    job_title.click()
                    time.sleep(2)  # Wait for the job details page to load

                    # Initialize dictionary to store job details
                    job_data = {}

                    # Extract Job Title
                    try:
                        job_data['Job Title'] = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "a._17o675e0"))
                        ).text.strip()
                    except Exception:
                        job_data['Job Title'] = "N/A"

                    # Extract Company Name
                    try:
                        job_data['Company Name'] = self.driver.find_element(
                            By.CSS_SELECTOR, "span[data-automation='advertiser-name']"
                        ).text.strip()
                    except NoSuchElementException:
                        job_data['Company Name'] = "N/A"

                    # Extract Job Location
                    try:
                        job_data['Job Location'] = self.driver.find_element(
                            By.CSS_SELECTOR, "span[data-automation='job-detail-location']"
                        ).text.strip()
                    except NoSuchElementException:
                        job_data['Job Location'] = "N/A"

                    # Extract Job Category
                    try:
                        job_data['Category'] = self.driver.find_element(
                            By.CSS_SELECTOR, "span[data-automation='job-detail-classifications']"
                        ).text.strip()
                    except NoSuchElementException:
                        job_data['Category'] = "N/A"

                    # Extract Type of Work
                    try:
                        job_data['Type of Work'] = self.driver.find_element(
                            By.CSS_SELECTOR, "span[data-automation='job-detail-work-type']"
                        ).text.strip()
                    except NoSuchElementException:
                        job_data['Type of Work'] = "N/A"

                    # Extract Salary
                    try:
                        job_data['Salary'] = self.driver.find_element(
                            By.CSS_SELECTOR, "span[data-automation='job-detail-add-expected-salary']"
                        ).text.strip()
                    except NoSuchElementException:
                        job_data['Salary'] = "N/A"

                    # Extract Date Posted
                    try:
                        job_data['Date Posted'] = self.driver.find_element(
                            By.XPATH, "//span[contains(text(), 'Posted')]"
                        ).text.strip()
                    except NoSuchElementException:
                        job_data['Date Posted'] = "N/A"

                    # Add current timestamp
                    job_data['Date and Time of Extraction'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    # Extract Job Description
                    try:
                        job_data['Description'] = self.driver.find_element(
                            By.CSS_SELECTOR, "div[data-automation='jobAdDetails']"
                        ).text.strip()
                    except NoSuchElementException:
                        job_data['Description'] = "N/A"

                    # Add the extracted job data to the list
                    job_data_list.append(job_data)

                    # Print the extracted data for verification
                    print(f"Extracted Data for Job {i + 1}: {job_data}")

                except Exception as e:
                    print(f"Error clicking job {i + 1}: {e}")
                    break

            print("Completed extracting job details.")
            return job_data_list

        except TimeoutException:
            print("Error: No job titles found on the page.")
            return job_data_list

    def click_page_number(self, page_number):
        """
        Click a specific page number in pagination.
        :param page_number: The target page number to navigate to.
        :return: True if navigation is successful, False otherwise.
        """
        try:
            # Construct the selector dynamically for the page number
            page_selector = f"a[data-automation='page-{page_number}']"
            
            # Wait for the page number link to be clickable
            page_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, page_selector))
            )

            print(f"Navigating to page {page_number}...")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", page_link)
            time.sleep(1)  # Allow time for scrolling
            
            # Click the page link
            page_link.click()
            time.sleep(3)  # Allow the next page to load
            return True

        except TimeoutException:
            print(f"Error: Page {page_number} link not found. Pagination stopped.")
            return False

    def extract_all_pages(self, start_page=1, end_page=None):
        """
        Extract job details from a range of pages.
        :param start_page: The page number to start extraction.
        :param end_page: The page number to stop extraction.
        """
        all_job_data = []
        current_page = start_page

        while True:
            print(f"Processing page {current_page}...")
            # Extract job details from the current page
            job_data_list = self.extract_job_details()
            all_job_data.extend(job_data_list)

            # Check if we reached the end page
            if end_page and current_page >= end_page:
                print(f"Reached the specified end page: {end_page}.")
                break

            # Attempt to click on the next page
            success = self.click_page_number(current_page + 1)
            if not success:
                print("Pagination complete or page not found.")
                break

            current_page += 1

        print(f"Completed extracting data from pages {start_page} to {current_page}.")
        return all_job_data


if __name__ == "__main__":
    driver_path = "/Users/nipunnkhurana/Desktop/chromedriver/chromedriver-mac-arm64 3/chromedriver"
    navigator = SeekJobList(driver_path)
    
    try:
        navigator.start_browser()
        base_url = "https://www.seek.com.au/jobs?sortmode=ListedDate"
        navigator.navigate_to_url(base_url)
        navigator.enter_keyword("Graduate")
        navigator.select_location("Sydney")
        navigator.click_seek_button()
        # Extract job details from page 2 to page 5
        start_page = 1
        end_page = 30
        all_jobs = navigator.extract_all_pages(start_page=start_page, end_page=end_page)

        # Save extracted data to Excel in a specific folder
        output_folder = "/Users/nipunnkhurana/Desktop/chromedriver/Seek_Jobs"  # Change this to your desired folder
        os.makedirs(output_folder, exist_ok=True)  # Create the folder if it doesn't exist
        output_file = os.path.join(output_folder, "extracted_jobs_Graduate_Sydney(1-30)_2102.xlsx")

        df = pd.DataFrame(all_jobs)
        df.to_excel(output_file, index=False)
        print(f"Data saved to {output_file}")

    finally:
        print("Script execution complete.")
