import time

from appium.webdriver.common.appiumby import AppiumBy


class Actions:
    def __init__(self, driver):
        self.driver = driver
        self.__KEY_CODE = {0: 7, 1: 8, 2: 9, 3: 10, 4: 11, 5: 12, 6: 13, 7: 14, 8: 15, 9: 16}

    def registration(self, phone_number, registration_name):
        if self.__check_number(phone_number):
            pass
        else:
            print('Номер должен содержать только цифры. Измените формат вводимых данных!')
            return False
        try:
            self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/next_button").click()
        except:
            pass
        self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/eula_accept").click()
        self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/registration_cc").clear().click()
        for i in range(len(str(phone_number))):
            digit = int(str(phone_number)[i:i + 1])
            self.driver.press_keycode(self.__KEY_CODE[digit])
        self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/registration_submit").click()
        time.sleep(2)
        self.driver.find_element(AppiumBy.ID, "android:id/button1").click()
        print('---Запрошен код подтверждения для завершения регистрации---')
        code = input('Введите код регистрации: ')
        self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/verify_sms_code_input").send_keys(code)
        time.sleep(2)
        self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/submit").click()
        self.driver.find_element(AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element(AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/registration_name").send_keys(registration_name)
        self.driver.find_element(AppiumBy.ID, 'com.whatsapp:id/fabText')
        print(f'Регистрация аккаунта WhatsApp на номер "{phone_number}" с именем "{registration_name}" завершена')

    def __find_phone_code(self, phone_number):
        try:
            self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/search_src_text").click()
            for i in range(4):
                digit = int(str(phone_number)[i:i+1])
                self.driver.press_keycode(self.__KEY_CODE[digit])
                self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/country_code")
        except:
            self.driver.press_keycode(67)
            self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/country_code").click()
        return i

    def __send_message(self):
        try:
            self.driver.find_element(AppiumBy.ID, 'com.whatsapp:id/fabText').click()
        except:
            self.driver.find_element(AppiumBy.ID, 'com.whatsapp:id/fab').click()

    def __check_number(self, phone_number):
        if str(phone_number).isdigit():
            return True
        else:
            return False

    def add_contact(self, phone_number, name):
        if self.__check_number(phone_number):
            pass
        else:
            print('Номер должен содержать только цифры. Измените формат вводимых данных!')
            return False
        self.__send_message()
        self.driver.find_elements(AppiumBy.ID, "com.whatsapp:id/contactpicker_row_name")[1].click()
        self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/first_name_field").send_keys(name)
        self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/country_code_field").click()
        self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/menuitem_search").click()
        code_len = self.__find_phone_code(phone_number)
        number = int(str(phone_number)[code_len:])
        self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/phone_field").send_keys(number)
        self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/keyboard_aware_save_button").click()
        self.driver.find_elements(AppiumBy.ID, "com.whatsapp:id/contactpicker_row_name")[1]
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]').click()
        print(f'Контакт "{name}" с номером телефона "{phone_number}" был добавлен в телефонную книгу')

    def send_message(self, name, message):
        self.__send_message()
        time.sleep(2)
        self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/menuitem_search").click()
        self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/search_src_text").send_keys(name)
        self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/contactpicker_row_name").click()
        self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/entry").send_keys(message)
        self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/send").click()
        self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/whatsapp_toolbar_home").click()
        print(f'Сообщение "{message}" для контакта "{name}" было отправлено')

    def create_new_group(self, list_of_contacts: list, subject: str):
        self.__send_message()
        self.driver.find_elements(AppiumBy.ID, "com.whatsapp:id/contactpicker_row_name")[0].click()
        time.sleep(2)
        self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/menuitem_search").click()
        contacts_in_group = []
        for item in list_of_contacts:
            self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/search_src_text").send_keys(item)
            try:
                self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/chat_able_contacts_row_name").click()
                contacts_in_group.append(item)
            except:
                print(f'Контакт "{item}" отсутствует в телефонной книге')
            self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/search_src_text").clear()
        if contacts_in_group:
            self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/next_btn").click()
            self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/group_name").send_keys(subject)
            self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/ok_btn").click()
            time.sleep(2)
            try:
                print(self.driver.find_element(AppiumBy.ID, "android:id/message").text)
                self.driver.find_element(AppiumBy.ID, "android:id/button2").click()
            except:
                pass
            self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/whatsapp_toolbar_home").click()
            print(f'Группа "{subject}" создана')
        else:
            print('Контакты отсутствуют в телефонной книге')
            self.driver.find_element(AppiumBy.ID, "com.whatsapp:id/search_back").click()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up").click()














