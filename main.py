from appium import webdriver
from WhatsApp import Actions


def driver_settings():
    desired_cap = {
    "platformName": "Android",
    "noReset": "true",
    "fullReset": "false",
    "unicodeKeyboard": "true",
    "resetKeyboard": "true",
    "appium:appPackage": "com.whatsapp",
    "appium:appActivity": "com.whatsapp.Main"
  }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    driver.implicitly_wait(3)
    return driver


def main():
    driver = driver_settings()
    action = Actions(driver)
    action.registration(77477777777, 'Bug')
    action.add_contact(77777777777, 'Joomla3')
    action.create_new_group(['Bamboo', 'Joomla1', 'Joomla3', 'Wordpress'], 'Super heroes')
    action.send_message('me', "Hello!")


if __name__ == '__main__':
    main()
