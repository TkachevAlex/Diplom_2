from json import loads
import allure
from data import Error
from objects.user import User
from services.generate_data import UserData


class TestCreateUser:
    @allure.title('При передаче в ручку регистрации реквизитов нового пользователя происходит успешная регистрация')
    def test__create_user__unique_user__status_code_is_200(self):
        user = User()
        response = user.create_user()
        user.delete_user()
        assert (response.status_code == 200) and (loads(response.text)['success'] == True)

    @allure.title(f'При попытке повторной регистрации, в ответе возвращается ошибка 403: "{Error.ALREADY_EXISTS}"')
    def test__create_user__duplicate_user__user_already_exists(self, create_user):
        user = create_user
        response = user.create_user(user.data)
        assert (response.status_code == 403) and (loads(response.text)['message'] == Error.ALREADY_EXISTS)

    @allure.title(f'При попытке регистрации без указания email, в ответе возвращается ошибка 403: "{Error.EMPTY_FIELDS}"')
    def test__create_user__user_data_without_email__required_fields(self):
        user = User()
        user.data = UserData().generate_data()
        user.data['email'] = ''
        response = user.create_user(user.data)
        assert (response.status_code == 403) and (loads(response.text)['message'] == Error.EMPTY_FIELDS)

    @allure.title(f'При попытке регистрации без указания password, в ответе возвращается ошибка 403: "{Error.EMPTY_FIELDS}"')
    def test__create_user__user_data_without_password__required_fields(self):
        user = User()
        user.data = UserData().generate_data()
        user.data['password'] = ''
        response = user.create_user(user.data)
        assert (response.status_code == 403) and (loads(response.text)['message'] == Error.EMPTY_FIELDS)

    @allure.title(f'При попытке регистрации без указания name, в ответе возвращается ошибка 403: "{Error.EMPTY_FIELDS}"')
    def test__create_user__user_data_without_name__required_fields(self):
        user = User()
        user.data = UserData().generate_data()
        user.data['name'] = ''
        response = user.create_user(user.data)
        assert (response.status_code == 403) and (loads(response.text)['message'] == Error.EMPTY_FIELDS)
