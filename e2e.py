import sys

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_scores_service (app_url):
    driver_path = 'C:\\Windows\\System32\\chromedriver.exe'
    my_service = Service(driver_path)

    driver = webdriver.Chrome(service=my_service)

    try:
        # Open a webpage
        driver.get(app_url)

        score_element = driver.find_element(By.ID, 'score')
        score_number = int(score_element.text)

        # Close the browser
        driver.quit()

        # Check if score is a positive integer between 0 and 1000
        if 0 <= score_number <= 1000:
            return True
        else:
            return False

    except NoSuchElementException:
        # Print a custom error message if the page could not be loaded
        print(f"An error occurred (no such element or site")
        return False

    except:
        return False

def main_function():
    if test_scores_service("http://localhost:5000"):
        sys.exit(0)
    else:
        sys.exit(-1)

if __name__ == "__main__":
    print("The result is: ",main_function())