import requests
from urls import Urls


class Order:

    def create_order(self, ingredients, user=None):
        if user:
            headers = {'Authorization': user.data['accessToken']}
        else:
            headers = ''
        data = {'ingredients': ingredients}
        response = requests.post(Urls.BASE_URL + Urls.CREATE_ORDER_ENDPOINT, headers=headers, data=data)
        return response

