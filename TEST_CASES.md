# Тест-кейсы для BankingProject

***
## TC_01.01 Проверка сообщения об успешном добавлении клиента

### Цель: Добавить клиента и проверить сообщение об успешном добавлении клиента
        
### Предусловие:
- Открыть браузер
            
### Шаги:
1. Открыть страницу https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager 
2. Нажать кнопку Add Customer
3. Дождаться появление формы Add Customer
4. Заполнить поле Post Code  (сгенерировать номер из 10 цифр)
5. Заполнить поле First Name (c учетом следующией логики: Post Code условно разбиваем на двузначные цифры (получится 
5 цифр), каждую цифру преобразовываем в букву английского алфавита по порядку от 0 до 25. 
Если цифра больше 25, то начинаем с 26 как с 0. Т.е. 0 - a, 26 - тоже a, 52 – тоже a, и т.д.)
6. Заполнить поле Last Name (сгенерировать рандомную фамилию)
7. Нажать кнопку Add Customer
8. Проверить сообщение об успешном добавлении клиента, сообщение должно содержать текст "Customer added successfully with customer id" и нажать кнопку ОК
       
### Постусловие:
- Удалить созданного клиента
            
### Ожидаемый результат:
- Новый клиент успешно добавлен в систему
- Появилось сообщение об успешном добавлении клиента, содержит текст "Customer added successfully with customer id"

***
# TC_01.02 Проверка данных созданного клиента с данными в таблице Customers

## Цель: Проверить данные созданного клиента с данными в таблице Customers

## Предусловие:
- Открыть браузер

## Шаги:
1. Открыть страницу https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager 
2. Нажать кнопку Add Customer
3. Дождаться появление формы Add Customer
4. Заполнить поле Post Code  (сгенерировать номер из 10 цифр)
5. Заполнить поле First Name (c учетом следующией логики: Post Code условно разбиваем на двузначные цифры (получится 
5 цифр), каждую цифру преобразовываем в букву английского алфавита по порядку от 0 до 25. 
Если цифра больше 25, то начинаем с 26 как с 0. Т.е. 0 - a, 26 - тоже a, 52 – тоже a, и т.д.)
6. Заполнить поле Last Name (сгенерировать рандомную фамилию)
7. Нажать кнопку Add Customer
8. В сообщении об успешном добавлении клиента нажать кнопку ОК
9. Перейти в Customers (нажать кнопку Customers)
10. Из таблицы Customers получить список клиентов
11. Проверить, что клиент с First_name, Last_name, Post_code введенными при добавлении клиента, отображается в таблице Customers
        
## Постусловие:
- Удалить созданного клиента

## Ожидаемый результат:
- Новый клиент успешно добавлен в систему
- В таблице Customers появилась строка (запись клиента) с First_name, Last_name, Post_code соответствующим введенным при создании клиента
***
# TC_01.03 Проверка данных созданного клиента с данными в dropdown меню в Open Account
## Цель: Проверить данные созданного клиента с данными в dropdown меню в Open Account

## Предусловие:
- Открыть браузер

## Шаги:
1. Открыть страницу https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager 
2. Нажать кнопку Add Customer
3. Дождаться появление формы Add Customer
4. Заполнить поле Post Code  (сгенерировать номер из 10 цифр)
5. Заполнить поле First Name (c учетом следующией логики: Post Code условно разбиваем на двузначные цифры (получится 
5 цифр), каждую цифру преобразовываем в букву английского алфавита по порядку от 0 до 25. 
Если цифра больше 25, то начинаем с 26 как с 0. Т.е. 0 - a, 26 - тоже a, 52 – тоже a, и т.д.)
6. Заполнить поле Last Name (сгенерировать рандомную фамилию)
7. Нажать кнопку Add Customer
8. В сообщении об успешном добавлении клиента нажать кнопку ОК
9. Нажать кнопку Open Account
10. Проверить, что в dropdown меню есть клиент с First_name, Last_name введенными при добавлении клиента

## Постусловие:
- Удалить созданного клиента

Ожидаемый результат:
- Новый клиент успешно добавлен в систему
- В dropdown меню есть клиент с First_name, Last_name введенными при добавлении клиента

***
# TC_01.04 Проверка сортировки строк таблицы Customers в обратном алфавитном порядке по First Name

## Цель: Проверить, сортировку по колонке First Name в обратном алфавитном порядке таблицы Customers

## Предусловие:
- Открыть браузер

## Шаги:
1. Открыть страницу https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list 
2. Нажать на First Name в таблице
3. Найти имена в таблице Customers
4. Проверить, что в таблице Customers значения в колонке First Name расположены в обратном алфавитном порядке

## Ожидаемый результат:
- В таблице Customers значения в колонке First Name расположены в обратном алфавитном порядке

***

# TC_01.05 Проверка сортировки строк таблицы Customers в алфавитном порядке по First Name

## Цель: Проверить, сортировкку по колонке First Name в алфавитном порядке таблицы Customers

## Предусловие:
- Открыть браузер

## Шаги:
1. Открыть страницу https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list 
2. Нажать на First Name в таблице
3. Нажать на First Name в таблице
3. Найти имена в таблице Customers
4. Проверить, что в таблице Customers значения в колонке First Name расположены в алфавитном порядке

## Ожидаемый результат:
- В таблице Customers значения в колонке First Name расположены в алфавитном порядке

***
# TC_01.06 Проверка удаления сustomers с длиной имени ближнему к среднему арифметическому длин всех имен в колонке First Name

## Цель: Проверить, удаление сustomers с First Name длина которого будет ближе к среднему арифметическому

## Предусловие:
- Открыть браузер

## Шаги:
1. Открыть страницу https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list 
2. Найти список Customers до удаления
3. Узнать длину каждого имени, затем найти среднее арифметическое получившихся длин
4. Удалить клиента(ов) с тем именем/именами, у которого(ых) длина будет ближе к среднему арифметическому
5. Найти имена в таблице Customers
6. Проверить, что количество записей в таблице Customers уменьшилось и соответствует ожидаемому

## Ожидаемый результат:
 - В таблице Customers удалены клиент(ы) с именем/именами, у которого(ых) длина будет ближе к 
    среднему арифметическому.
 - Количество записей в таблице Customers уменьшилось и соответствует ожидаемому
   