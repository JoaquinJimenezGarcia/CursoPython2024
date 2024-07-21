from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(10)
browser.get("https://github.com")

link = browser.find_element(By.LINK_TEXT, "Sign in")
link.click()

user_input = browser.find_element(By.ID, "login_field")
password_input = browser.find_element(By.ID, "password")

user_input.send_keys("helloworld")
password_input.send_keys("hello_world_pass")
password_input.send_keys(Keys.RETURN)

if browser.find_element(By.CLASS_NAME, "flash-error"):
    print("Wrong user or password")
else:
    profile = browser.find_element(
        By.CLASS_NAME,
        "css-truncate.css-truncate-target.ml-1"
    )

    label = profile.get_attribute("innerHTML")

    assert "JoaquinJimenezGarcia" in label


browser.quit()