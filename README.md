# Проект UI автотестов Python

<img width="1469" alt="image" src="https://github.com/user-attachments/assets/60d2b042-4a78-45d2-8d2f-8aa0e3313890" />

<img width="1470" alt="image" src="https://github.com/user-attachments/assets/8e8ec441-7f0c-4f68-8803-9339b27431ac" />




<h2 align="center"> Automation </h2>
<p align="center">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height='50'  width='50' />&nbsp;&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" height='60'  width='60' />&nbsp;&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" height='50'  width='50' />&nbsp;&nbsp;&nbsp;&nbsp;
<img alt="Static Badge" src="https://img.shields.io/badge/Selene-blue?style=for-the-badge" height='40'  width='80'>&nbsp;&nbsp;
<img src="https://molecula.gallerycdn.vsassets.io/extensions/molecula/allure-test-reports/1.1/1474455326332/Microsoft.VisualStudio.Services.Icons.Default" height='40'  width='40'/>


<h2 align="center"> Tools </h2>
<p align="center">
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"/>&nbsp;&nbsp;
<img src="https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=Jenkins&logoColor=white"/>&nbsp;&nbsp;
<img alt="Static Badge" src="https://img.shields.io/badge/Allure-green?style=for-the-badge">&nbsp;&nbsp;

### Что проверяем
* Авторизация
* Поиск товара
* Добавление товара в корзину
* Проверка контактной информации
&nbsp;
  ---
### Запуск автотестов

```
Для запуска тестов требуются креды доступа к виртуальной машине в Selenide
Данные хранятся в .env и не доступны публично
SELENOID_LOGIN
SELENOID_PASS
SELENOID_URL
```

### Локально
```
pytest .
pytest tests/
```

### Удаленно
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```
&nbsp;
  ---

### <img src="https://www.svgrepo.com/show/353929/jenkins.svg" height='60'  width='60'/> Запуск проекта в Jenkins

##### При нажатии на "Build Now" запустится проект.
<img width="1488" alt="Снимок экрана 2025-04-30 в 12 43 52" src="https://github.com/user-attachments/assets/b3f9b5e3-f96d-40f5-8cfa-c65cb8a124f7" />

#### Варианты запуска:
##### Выбирается папка откуда будут браться автотесты UI или API
##### Указывается версия браузера на котором будет происходить запуск
<img width="784" alt="Снимок экрана 2025-04-30 в 12 28 51" src="https://github.com/user-attachments/assets/6a6e3457-9d21-443b-8bd0-f956725fe981" />

##### При нажатии кнопки Build начнется сборка тестов и их прохождение, через виртуальную машину в Selenide
&nbsp;
  ---



<!-- Allure report -->

### <img src="https://molecula.gallerycdn.vsassets.io/extensions/molecula/allure-test-reports/1.1/1474455326332/Microsoft.VisualStudio.Services.Icons.Default" height='40'  width='40'/> Allure report

##### После прохождения тестов, результаты можно посмотреть в Allure отчете, где так же содержится ссылка на Jenkins
<img width="1499" alt="Снимок экрана 2025-04-30 в 12 32 10" src="https://github.com/user-attachments/assets/8d463e2a-da77-4125-ba0e-1163189885c8" />

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
<img width="1486" alt="Снимок экрана 2025-04-30 в 13 28 05" src="https://github.com/user-attachments/assets/a3e08dd1-2e99-496e-b23e-5cdd54ef8bb1" />


##### Во вкладке Suites находятся собранные тест кейсы, у которых описаны шаги и приложены логи, скриншот и видео о прохождении теста
<img width="1493" alt="Снимок экрана 2025-04-30 в 13 31 16" src="https://github.com/user-attachments/assets/cf6a0197-d4e4-4e4d-97a0-6bd67f80c924" />

##### Видео прохождение теста
![e8c2e75af098fa4ea979f2ce9d76d36c](https://github.com/user-attachments/assets/57baa622-411b-438e-9f1f-a5b5bdd98c90)

&nbsp;
  ---
  
### <img src="https://molecula.gallerycdn.vsassets.io/extensions/molecula/allure-test-reports/1.1/1474455326332/Microsoft.VisualStudio.Services.Icons.Default" height='40'  width='40'/> Интеграция с AllureTestOps
#### После запуска автотестов в jenkins, происходит передача запуска в раздел Launches AllureTestOps
<img width="1465" alt="Снимок экрана 2025-06-02 в 11 35 57" src="https://github.com/user-attachments/assets/00fad88d-58f9-40c3-8e3b-7fc3e1cf6d28" />

#### Автотесты передаются в систему AllureTestOps и имеют такую же иерархию как в основной папке tests репозитория
<img width="791" alt="Снимок экрана 2025-06-02 в 11 26 48" src="https://github.com/user-attachments/assets/ce191c06-9cb7-489a-a96d-c121a966ee04" />

&nbsp;
  ---

### <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Telegram_2019_Logo.svg/2048px-Telegram_2019_Logo.svg.png" height='40'  width='40'/> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах.
<img width="880" alt="Снимок экрана 2025-04-30 в 12 35 49" src="https://github.com/user-attachments/assets/b01cad29-8233-48a7-a0ea-41fa0accb8c8" />
