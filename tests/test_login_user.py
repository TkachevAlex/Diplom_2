from json import loads
import allure


class TestLoginUser:
    @allure.title('При указании логина и пароля зарегистрированного пользователя, в ответе возвращается сообщение об успешной авторизации')
    def test__login_user__register_user__status_code_is_200(self, setup):
        user = setup
        response = user.login_user(user.data)
        assert (response.status_code == 200) and (loads(response.text)['success'] == True)

    @allure.title('При указании неверного логина зарегистрированного пользователя, в ответе возвращается ошибка 401: "email or password are incorrect"')
    def test__login_user__user_data_wrong_email__incorrect(self, setup):
        user = setup
        user.data['email'] += '_wrong'
        response = user.login_user(user.data)
        assert (response.status_code == 401) and (loads(response.text)['message'] == 'email or password are incorrect')

    @allure.title('При указании неверного пароля зарегистрированного пользователя, в ответе возвращается ошибка 401: "email or password are incorrect"')
    def test__login_user__user_data_wrong_password__incorrect(self, setup):
        user = setup
        user.data['email'] += '_wrong'
        response = user.login_user(user.data)
        assert (response.status_code == 401) and (loads(response.text)['message'] == 'email or password are incorrect')
