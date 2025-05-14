import allure

#Не получилось автоматизировать авторизацию до конца. Любой из способов требует подтверждение СМС-кодом.
#Кейс возможно воспроизвести только "помогаю" ввести код из смс
@allure.story('Успешная авторизация')
def test_successful_authorization(authorization):
    (authorization
     .open_authorization_page()
     .choose_address()
     .open_authorization_sidebar()
     .authorization_ya()
     .choose_address_2()
     .assert_successful_authorization())
