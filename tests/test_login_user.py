from json import loads
import allure
from data import Error


class TestLoginUser:
    @allure.title('При указании логина и пароля зарегистрированного пользователя, в ответе возвращается сообщение об успешной авторизации')
    def test__login_user__register_user__status_code_is_200(self, create_user):
        user = create_user
        response = user.login_user(user.data)
        assert (response.status_code == 200) and (loads(response.text)['success'] == True)

    @allure.title(f'При указании неверного логина зарегистрированного пользователя, в ответе возвращается ошибка 401: "{Error.INCORRECT}"')
    def test__login_user__user_data_wrong_email__incorrect(self, create_user):
        user = create_user
        user.data['email'] += '_wrong'
        response = user.login_user(user.data)
        assert (response.status_code == 401) and (loads(response.text)['message'] == Error.INCORRECT)

    @allure.title(f'При указании неверного пароля зарегистрированного пользователя, в ответе возвращается ошибка 401: "{Error.INCORRECT}"')
    def test__login_user__user_data_wrong_password__incorrect(self, create_user):
        user = create_user
        user.data['email'] += '_wrong'
        response = user.login_user(user.data)
        assert (response.status_code == 401) and (loads(response.text)['message'] == Error.INCORRECT)
