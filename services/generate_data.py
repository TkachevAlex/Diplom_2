from random import shuffle, randint
from faker import Faker
import requests
from urls import Urls


class UserData:
    def generate_data(self):
        user_data = {
            "email": Faker().email(),
            "password": Faker().password(),
            "name": Faker().first_name()
        }
        return user_data

class IngredientData:
    def generate_data(self):
        response = requests.get(Urls.BASE_URL + Urls.GET_INGREDIENTS_ENDPOINT)
        ingredients = [ingredient['_id'] for ingredient in response.json()['data']]
        return ingredients[: randint(1, len(ingredients))]

