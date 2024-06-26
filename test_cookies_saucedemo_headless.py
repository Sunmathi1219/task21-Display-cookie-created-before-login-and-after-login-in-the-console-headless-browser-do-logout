""""
Test Headless browser and display the cookies
"""

from cookies_saucedemo_headless import Cookies_saucedemo
import pytest

url="https://www.saucedemo.com/"
cookies=Cookies_saucedemo(url)

def test_get_url():
    assert cookies.get_url() == True
    print("Success : The webpage url is loaded successfully")

def test_validate_username_input_box():
    assert cookies.validate_username_input_box() == True
    print("Success : Input box is displayed successfully")

def test_validate_password_input_box():
    assert cookies.validate_password_input_box() == True
    print("Success : Password box is displayed successfully")

def test_validate_submit_button():
    assert cookies.validate_submit_button() == "https://www.saucedemo.com/inventory.html"
    print("SUCCESS : Login is Success with {username} & {password}".format(username=cookies.username,
                                                                           password=cookies.password))

def test_validate_logout_button():
    assert cookies.validate_logout_button() == "https://www.saucedemo.com/"
    print("Success : Logout is success")

def test_shutdown():
    assert cookies.shutdown() == None
    print("Success : URL webpage has closed successfully")

