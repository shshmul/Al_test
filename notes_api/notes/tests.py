from django.test import TestCase

# Create your tests here.
from django.urls import reverse

class Testview(TestCase):
    # Проверка создание юзера
    def test_register(self):
        self.user_data = {
            'username': '99972',
            'password': '123'
        }
        response = self.client.post('/api/register/', self.user_data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    # Проверка получение токена
    def test_get_token(self):
        # Регистрируем заново
        self.user_data = {
            'username': '99972',
            'password': '123'
        }
        response = self.client.post('/api/register/', self.user_data, content_type='application/json')

        # Проверка получение токена
        response = self.client.post('/api/token/', self.user_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        # print(response.data['access'])
        self.assertIn('refresh', response.data)

        # получение заметок
        token = response.data['access']
        headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}
        response1 = self.client.get('/api/notes/', **headers)
        # print(response1)
        self.assertEqual(response1.status_code, 200)





