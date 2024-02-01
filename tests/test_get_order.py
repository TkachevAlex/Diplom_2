from json import loads
import allure
from objects.order import Order
from objects.user import User
from services.generate_data import IngredientData


class TestGetOrder:
    @allure.title('При запросе заказов авторизованного пользователя выводится список заказов')
    def test__get_order__authorized_user__order_is_getting(self, setup):
        user = setup
        order = Order()
        ingredients = IngredientData().generate_data()
        order.create_order(ingredients, user)
        response = user.get_order(user)
        assert (response.status_code == 200) and (loads(response.text)['success'] == True)

    @allure.title('При запросе заказов неавторизованного пользователя, в ответе возвращается ошибка 401: "You should be authorised"')
    def test__get_order__unauthorized_user__should_be_authorised(self):
        user = User()
        response = user.get_order()
        assert (response.status_code == 401) and (loads(response.text)['message'] == 'You should be authorised')
