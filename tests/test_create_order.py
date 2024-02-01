from json import loads
import allure
from objects.order import Order
from services.generate_data import IngredientData


class TestCreateOrder:

    @allure.title('При передаче в ручку создания заказа токена юзера и ингридиентов с валидным кэшем происходит успешный заказ')
    def test__create_order__authorized_user_and_ingredients__status_code_is_200(self, setup):
        user = setup
        ingredients = IngredientData().generate_data()
        order = Order()
        response = order.create_order(ingredients, user)
        assert (response.status_code == 200) and (loads(response.text)['success'] == True)

    @allure.title('При передаче в ручку создания заказа токена юзера, в ответе возвращается ошибка 400: "Ingredient ids must be provided"')
    def test__create_order__authorized_user_and_none_ingredients__must_be_provided(self, setup):
        user = setup
        ingredients = []
        order = Order()
        response = order.create_order(ingredients, user)
        assert (response.status_code == 400) and (loads(response.text)['message'] == 'Ingredient ids must be provided')

    @allure.title('При передаче в ручку создания заказа ингридиентов с валидным кэшем происходит успешный заказ')
    def test__create_order__unauthorized_user_and_ingredients__status_code_is_200(self):
        ingredients = IngredientData().generate_data()
        order = Order()
        response = order.create_order(ingredients)
        assert (response.status_code == 200) and (loads(response.text)['success'] == True)

    @allure.title('При передаче в ручку создания заказа списка без ингредиентов, в ответе возвращается ошибка 400: "Ingredient ids must be provided"')
    def test__create_order__unauthorized_user_and_none_ingredients__must_be_provided(self):
        ingredients = []
        order = Order()
        response = order.create_order(ingredients)
        assert (response.status_code == 400) and (loads(response.text)['message'] == 'Ingredient ids must be provided')

    @allure.title('При передаче в ручку создания заказа токена юзера и ингридиентов с невалидным кэшем, в ответе возвращается ошибка 500')
    def test__create_order__authorized_user_and_bad_hash__status_code_is_500(self, setup):
        user = setup
        ingredients = IngredientData().generate_data()
        modified_ingredients = [ingredient + '_bad' for ingredient in ingredients]
        order = Order()
        response = order.create_order(modified_ingredients, user)
        assert response.status_code == 500

    @allure.title('При передаче в ручку создания заказа ингридиентов с невалидным кэшем, в ответе возвращается ошибка 500')
    def test__create_order__unauthorized_user_and_bad_hash__status_code_is_500(self):
        ingredients = IngredientData().generate_data()
        modified_ingredients = [ingredient + '_bad' for ingredient in ingredients]
        order = Order()
        response = order.create_order(modified_ingredients)
        assert response.status_code == 500
