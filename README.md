# Проект UI автотестов Python

<img width="1469" alt="image" src="https://github.com/user-attachments/assets/60d2b042-4a78-45d2-8d2f-8aa0e3313890" />

<img width="1470" alt="image" src="https://github.com/user-attachments/assets/8e8ec441-7f0c-4f68-8803-9339b27431ac" />

<img width="427" alt="image" src="https://github.com/user-attachments/assets/b0c98ecc-ad41-4af8-bf6f-935eb38cb776" />





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

##### При нажатии кнопки Build начнется сборка тестов и их прохождение, через виртуальную машину в Selenide
<img width="1464" alt="image" src="https://github.com/user-attachments/assets/25d08582-c7ff-40de-a1ab-98fcd9eb9e03" />

&nbsp;
  ---
<!-- Allure report -->

### <img src="https://molecula.gallerycdn.vsassets.io/extensions/molecula/allure-test-reports/1.1/1474455326332/Microsoft.VisualStudio.Services.Icons.Default" height='40'  width='40'/> Allure report

##### После прохождения тестов, результаты можно посмотреть в Allure отчете, где так же содержится ссылка на Jenkins
<img width="1469" alt="image" src="https://github.com/user-attachments/assets/60d2b042-4a78-45d2-8d2f-8aa0e3313890" />

##### Во вкладке Suites находятся собранные тест кейсы, у которых описаны шаги и приложены логи, скриншот и видео о прохождении теста
<img width="1470" alt="image" src="https://github.com/user-attachments/assets/8e8ec441-7f0c-4f68-8803-9339b27431ac" />

&nbsp;
  ---

### <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Telegram_2019_Logo.svg/2048px-Telegram_2019_Logo.svg.png" height='40'  width='40'/> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах.
<img width="427" alt="image" src="https://github.com/user-attachments/assets/b0c98ecc-ad41-4af8-bf6f-935eb38cb776" />
