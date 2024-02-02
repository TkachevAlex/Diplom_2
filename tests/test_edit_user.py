from json import loads
import allure
from data import Error


class TestEditUser:
    @allure.title('При изменении email авторизованного юзера, в ответе возвращается сообщение об успешном изменении данных')
    def test__edit_authorized_user__editing_user_email__email_is_editing(self, create_user):
        user = create_user
        user.data["email"] += '_new'
        response = user.edit_user(user.data, user)
        assert (response.status_code == 200) and (loads(response.text)['user']['email'] == user.data["email"])

    @allure.title('При изменении name авторизованного юзера, в ответе возвращается сообщение об успешном изменении данных')
    def test__edit_authorized_user__editing_user_name__name_is_editing(self, create_user):
        user = create_user
        user.data["name"] += '_new'
        response = user.edit_user(user.data, user)
        assert (response.status_code == 200) and (loads(response.text)['user']['name'] == user.data["name"])

    @allure.title(f'При изменении email неавторизованного юзера, в ответе возвращается ошибка 401: "{Error.AUTHORISED}"')
    def test__edit_unauthorized_user__editing_user_email__should_be_authorised(self, create_user):
        user = create_user
        user.data["email"] += '_new'
        response = user.edit_user(user.data)
        assert (response.status_code == 401) and (loads(response.text)['message'] == Error.AUTHORISED)

    @allure.title(f'При изменении name неавторизованного юзера, в ответе возвращается ошибка 401: "{Error.AUTHORISED}"')
    def test__edit_unauthorized_user__editing_user_name__should_be_authorised(self, create_user):
        user = create_user
        user.data["name"] += '_new'
        response = user.edit_user(user.data)
        assert (response.status_code == 401) and (loads(response.text)['message'] == Error.AUTHORISED)