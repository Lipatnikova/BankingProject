# task_ui
_Практикум SDET: задание UI_


![Python Version](https://img.shields.io/badge/python-3.10-blue)
[![dependency - selenium](https://img.shields.io/badge/dependency-selenium-blue?logo=selenium&logoColor=white)](https://pypi.org/project/selenium)
[![dependency - pytest](https://img.shields.io/badge/dependency-pytest-blue?logo=pytest&logoColor=white)](https://pypi.org/project/pytest)
[![dependency - Faker](https://img.shields.io/badge/dependency-Faker-blue)](https://pypi.org/project/Faker)
[![dependency - allure-pytest](https://img.shields.io/badge/dependency-allure--pytest-blue?logo=qameta&logoColor=white)](https://pypi.org/project/allure-pytest)

Тест-кейсы: [ТЕСТ-КЕЙСЫ](https://github.com/Lipatnikova/BankingProject/blob/task_ui/TEST_CASES.md)

ALLURE REPORT: [![Allure-report](https://img.shields.io/badge/Allure%20Report-deployed-green)](https://lipatnikova.github.io/task_ui/)

Status of Last Deployment: [![XYZ_BANK](https://github.com/Lipatnikova/BankingProject/actions/workflows/xyz_bank_push.yml/badge.svg?branch=)](https://github.com/Lipatnikova/BankingProject/actions/workflows/xyz_bank_push.yml)

## Как работать с репозиторием в Git Actions:

- Перейти во вкладку Actions репозитория. 
- Выбрать All workflows -> Automated tests with Allure ("This workflow has a workflow_dispatch event trigger"). 
- Нажать на кнопку Run workflow и выбрать Choose target: "ui". 
- Нажать на кнопку Run workflow.

## Как работать с репозиторием на ПК:

1. Склонировать репозиторий `git clone "Clone using the web URL"`.
2. Перейти в директорию проекта.
3. Создать виртуальное окружение `python -m venv venv`.
4. Активировать виртуальное окружение для Windows: `venv\Scripts\activate.bat`; для Linux и MacOS: `source venv/bin/activate`.
5. Установить зависимости `pip install -r requirements.txt`.
6. Запустить тесты:
6. 1. Чтобы запустить тесты использовать команду `pytest -s -v`.
6. 2. Чтобы запустить тесты  с генерацией отчета Allure использовать команду `pytest -s -v --alluredir allure-results`.
6. 3. Чтобы запустить тесты  **параллельно** с генерацией отчета Allure использовать команду `pytest -s -v -n=2 --alluredir allure-results`.
7. Просмотреть отчет Allure `allure serve allure-results`.


## Задание для Python:

1. Составить подробные тест-кейсы по чек-листу из 3 кейсов, описанном далее.
2. На Python (рекомендуется использовать версию 3.10) создать проект UI-автотестов по тест-кейсам Кейсы также прикрепить в данный проект (в формате 
текстового файла с использованием Markdown).
3. В проекте использовать:
- Selenium Webdriver (желательно использовать браузер Chrome).
- Тестовый фреймворк Python – pytest.
4. Результаты на проверку оформить в виде Merge Request/Pull Request (!!!) ветки в которой 
вы вели разработку в главную на Gitlab/GitHub.
5. Дополнительное задание №1: Реализовать формирование отчетов Allure.
6. Дополнительное задание №2: Реализовать параллельный запуск тестов.
7. Дополнительное задание №3: Реализовать запуск в системе CI/CD.
