# Начальная инструкция 
Сделано:
Тюлин Игорь, Костин Андрей - 19ПИ-2

Для запуска проекта откройте терминал и перейдя в папку с проектом выполните эти команды(если не работает замените pip на pip3 и python на python3): Для запуска проекта откройте терминал и перейдя в папку с проектом выполните эти команды: pip install -r requirements.txt

# Откройте новый терминал в папке с проектом и напишите:
python Controller.py

# Схема базы данных
![image](https://user-images.githubusercontent.com/57899934/121786283-91348200-cbc7-11eb-902a-754b98228236.png)

# Предметная область БД:

Таблица Orders:  
id - id заказа  
purchase_date - время покупки  
detail_id - id детали  
consumer_id - id покупателя  
quantity - количество деталей  

Таблица Orders Prices:  
id - id цены заказа  
price - цена заказа  

Таблица Details:  
id - id детали  
name - название детали  
cost - цена детали  

Таблица Cunsomers:  
id - id покупателя  
name - имя покупателя  
address - адрес покупателя  

# Ссылка на видео  
*ссылка - https://youtu.be/Bj7ROWgGy6M https://youtu.be/y7O_xnCuDvE
