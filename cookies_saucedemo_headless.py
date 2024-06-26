""""
Using python selenium automation and the URL https://www.saucedemo.com/ display the cookie created before login and
after login in the console.after you login into the dashboard of the portal kindly do the logout also
Verify that the cookies are being generated during the login process
"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Cookies_saucedemo:

    username = "standard_user"
    password = "secret_sauce"

    def __init__(self,url):
        self.url=url

        #Enable Headless Browsing on a Chrome Browser
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    #Load the URL page
    def get_url(self):
        #get the url
        self.driver.get(self.url)
        sleep(3)
        #Display the cookies before login
        print("Cookies Before Login")
        print(self.driver.get_cookies())

        if self.driver.current_url == "https://www.saucedemo.com/":
            return True
        else:
            return False
    #close the automation web page
    def shutdown(self):
        self.driver.quit()
        sleep(2)
        return None
    #validate the username input box
    def validate_username_input_box(self):
        username_input_box=self.driver.find_element(by=By.NAME, value="user-name")

        if username_input_box.is_displayed():
            sleep(2)
            return True
        else:

            return False
    #validate the password input box
    def validate_password_input_box(self):
        password_input_box = self.driver.find_element(by=By.ID, value="password")

        if password_input_box.is_displayed():
            sleep(2)
            return True
        else:
            return False
    #validate and login the URL and logout the URL
    def validate_submit_button(self):
        username_input_box = self.driver.find_element(by=By.NAME, value="user-name")
        password_input_box = self.driver.find_element(by=By.ID, value="password")
        submit_button = self.driver.find_element(by=By.XPATH, value="//*[@name='login-button']")

        if username_input_box.is_enabled() and password_input_box.is_enabled():
            username_input_box.send_keys(self.username)
            password_input_box.send_keys(self.password)
            sleep(2)

            #login to the page
            if submit_button.is_enabled():
                submit_button.click()
                print("Current URL :", self.driver.current_url)

                #Display the cookies after login
                print("Cookies after login")
                print(self.driver.get_cookies())
                sleep(2)
                return self.driver.current_url

            else:
                  return False


    def validate_logout_button(self):
        if self.driver.current_url == "https://www.saucedemo.com/inventory.html":
            menu_button=self.driver.find_element(by=By.XPATH, value="//*[@id='react-burger-menu-btn']")
            logout = self.driver.find_element(by=By.XPATH, value="//*[@id='logout_sidebar_link']")

            #logout the page
            if menu_button.is_enabled():
                menu_button.click()
                sleep(2)
                logout.click()

                #Display the cookies after logout
                print("cookies after logout")
                print(self.driver.get_cookies())
                return self.driver.current_url
            else:
                return False


if __name__ == "__main__":
    cookies=Cookies_saucedemo("https://www.saucedemo.com/")
    cookies.get_url()
    cookies.validate_username_input_box()
    cookies.validate_password_input_box()
    cookies.validate_submit_button()
    cookies.validate_logout_button()
    cookies.shutdown()




