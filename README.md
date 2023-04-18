<strong>Скрипт позволяет осуществлять управление приложением WhatsApp на виртуальном Android-устройстве, в частности, осуществлять регистрацию аккаунта, добавлять контакт
в телефонную книгу, создавать группу с добавлением требуемых контактов из телефонной книги, отправлять сообщение в группу/контакту</strong>

## Предустановка
Установить [JAVA](https://www.oracle.com/java/technologies/downloads/)  
Установить [AndroidStudio](https://developer.android.com/studio/install)  
Создать в AndroidStudio виртуальное Android-устройство и запустить его (Android virtual device, AVD)  
Установить приложение WhatsApp на AVD  
Установить и запустить [Appium-сервер](https://appium.io/docs/en/2.0/quickstart/install/)  
![image](https://user-images.githubusercontent.com/106806612/232790656-116a5e57-7e27-421d-9b61-d8aaa21cbc32.png)

## Установка
```ruby
$ git clone https://github.com/SofronovRoman/Appium_WhatsApp.git
$ cd Appium_WhatsApp
$ pip install -r requirements.txt
```

## Использование
```ruby
$ python main.py
```

## Примечание
В скрипте main.py продемонстрированы все возможности с только что установленным приложением WhatsApp. 
Если у вас уже осуществлена регистрация WhatsApp на AVD, то дальнейшую демонстрацию возможностей необходимо выполнять при
закомментированной строчке скрипта, реализующей регистрацию аккаунта.

## Источники
[Документация Appium](http://appium.io/docs/en/2.0/)  
[Appium python client](https://pypi.org/project/Appium-Python-Client/)  
[Appium inspector](https://github.com/appium/appium-inspector?ysclid=lgmbdvaa46176034047)  
[Appium python video](https://www.youtube.com/playlist?list=PLWIBmxdTr81dDEZRiNxoy55dIDWtMyOoc)  
