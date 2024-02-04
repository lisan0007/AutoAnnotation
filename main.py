import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def sleeping3sec(func):
    def wrapper():
        time.sleep(3)
        print("Waiting 3 sec before executing the function")
        result = func()
        time.sleep(3)
        print("Waiting 3 sec after executing the function")
        return result
    return wrapper


def sleeping1sec(func):
    def wrapper():
        time.sleep(1)
        print("Waiting 1 sec before executing the function")
        result = func()
        time.sleep(1)
        print("Waiting 1 sec after executing the function")
        return result
    return wrapper


# Specify the path to the GeckoDriver executable
gecko_driver_path = "/bin/geckodriver"  # Replace with the actual path

# Set Firefox options and set the executable path
options = Options()
options.binary_location = "/usr/bin/firefox"  # Replace with the actual path

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(executable_path=gecko_driver_path, options=options)
driver.get("https://annotation.dotkom.io")  # Make sure to use the correct URL

# Find the email and password input fields by their IDs
email_input = driver.find_element("id", "Email")  # Replace with the actual ID
password_input = driver.find_element("id", "Password")  # Replace with the actual ID

# Enter your email and password
email_input.send_keys("lisunsarker@gmail.com")
password_input.send_keys("Lisun@123")

# Submit the form (you may need to adjust this part based on the actual form structure)
password_input.submit()
time.sleep(3)

# After completing your actions on the current page, go to the specified URL
new_url = "https://annotation.dotkom.io/projectannotation/ProjectCommentAnnotationBeta?projectId=0c277d79-f261-44a5-84a4-4db588e3009c&commentId="
driver.get(new_url)
time.sleep(2)

# Close the browser at the end of the script

"""
will be making 4 changes
1. making dropdown POST
2. selecting FROM date
3. selecting TO date
4. set keyword for a specific post
"""


@sleeping3sec
def keywordtype():
    # 1. We are making dropdown POST
    dropdown_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "keywordType")))
    dropdown = Select(dropdown_element)
    dropdown.select_by_value("post")
    print("1. Successfully selected post from DropDown")


def setDate():
    # 2. selecting FROM date
    from_date_input = driver.find_element("id", "fromDate")
    to_date_input = driver.find_element("id", "toDate")
    keyword_search_input = driver.find_element("id", "keywordSearch")

    # Set the desired dates
    from_date_input.send_keys("2024-01-20")
    to_date_input.send_keys("2024-02-05")

    # 3. Set keyword for a specific post
    keyword_search_input.send_keys("#BoycottBkash")

    # 4. Click the filters button
    filters_button = driver.find_element("id", "btnfilter")
    filters_button.click()
    time.sleep(10)


@sleeping1sec
def brand():
    element = driver.find_element_by_class_name("select2-container")
    # Click on the element
    element.click()
    print("clicking to Select Brand")
    input_element = driver.find_element_by_id("s2id_autogen1_search")

    # Send keys to the input element
    input_element.send_keys("Bkash")

    # Press Enter
    input_element.send_keys(Keys.RETURN)


@sleeping1sec
def sentiment():
    element_s = driver.find_element_by_id("s2id_S")

    # Click on the element
    element_s.click()
    text_field_element = driver.find_element_by_id("s2id_autogen2_search")

    # Send keys to the text field element
    text_field_element.send_keys("Negative")

    # Press Enter
    text_field_element.send_keys(Keys.RETURN)
    print("Selected sentiment Properly")


def category():
    element_category = driver.find_element_by_id("s2id_categoryId")

    # Click on the element
    element_category.click()
    # s2id_autogen3_search
    text_field_element = driver.find_element_by_id("s2id_autogen3_search")

    # Send keys to the text field element
    text_field_element.send_keys("Brand")

    # Press Enter
    text_field_element.send_keys(Keys.RETURN)
    print("Selected Category Properly")
    time.sleep(2)


def subcategory(subcategory_text):
    # Locate the category dropdown element
    element_category = driver.find_element_by_id("s2id_subcategoryId")

    # Click on the category dropdown to open it
    element_category.click()

    # Build a dynamic XPath for the subcategory option based on its text content
    xpath_expression = f'//div[@class="select2-result-label" and text()="{subcategory_text}"]'

    # Wait for the specific subcategory option to be clickable
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_expression))
    )

    # Click on the subcategory option
    element.click()

    print(f"Selected SubCategory '{subcategory_text}' Properly")


def emotion():
    # s2id_E
    # s2id_autogen5_search
    element_category = driver.find_element_by_id("s2id_E")

    # Click on the element
    element_category.click()
    # s2id_autogen3_search
    text_field_element = driver.find_element_by_id("s2id_autogen5_search")

    # Send keys to the text field element
    text_field_element.send_keys("Angry")

    # Press Enter
    text_field_element.send_keys(Keys.RETURN)
    print("Selected Emotion Properly")


@sleeping1sec
def loyalty():

    # s2id_ProfileTagId
    # s2id_autogen7_search

    element_category = driver.find_element_by_id("s2id_ProfileTagId")

    # Click on the element
    element_category.click()
    # s2id_autogen3_search
    text_field_element = driver.find_element_by_id("s2id_autogen7_search")

    # Send keys to the text field element
    text_field_element.send_keys("Hater")

    # Press Enter
    text_field_element.send_keys(Keys.RETURN)
    print("Selected Emotion Properly")


def update():
    button_element = driver.find_element_by_id("btnUpdate")

    # Click on the element
    button_element.click()


keywordtype()
setDate()

brand()
sentiment()
category()
subcategory("Associated")
emotion()
loyalty()
update()

for _ in range(50):
    time.sleep(5)
    category()
    time.sleep(2)
    subcategory ( "Associated" )
    update()
