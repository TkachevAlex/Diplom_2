from services.generate_data import UserData
from urls import Urls
import requests


class User:
    def __init__(self):
        self.data = {'accessToken': None,
                     'email': '',
                     'password': '',
                     'name': ''}

    def create_user(self, user_data=None):
        if user_data is None:
            self.data.update(UserData().generate_data())
        response = requests.post(Urls.BASE_URL + Urls.CREATE_USER_ENDPOINT, data=self.data)
        if response.status_code == 200:
            self.data['accessToken'] = response.json()['accessToken']
        return response

    def delete_user(self):
        if self.data['accessToken']:
            headers = {'Authorization': self.data['accessToken']}
            response = requests.delete(Urls.BASE_URL + Urls.DELETE_USER_ENDPOINT, headers=headers)
            return response

    def login_user(self, user_data):
        response = requests.post(Urls.BASE_URL + Urls.LOGIN_USER_ENDPOINT, data=user_data)
        return response

    def edit_user(self, user_data, user=None):
        if user:
            headers = {'Authorization': self.data['accessToken']}
        else:
            headers = ''
        response = requests.patch(Urls.BASE_URL + Urls.EDIT_USER_ENDPOINT, data=user_data, headers=headers)
        return response

    def get_order(self, user=None):
        if user:
            headers = {'Authorization': self.data['accessToken']}
        else:
            headers = ''
        response = requests.get(Urls.BASE_URL + Urls.GET_ORDER_ENDPOINT, headers=headers)
        return response

