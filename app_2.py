import unittest
from app import app  # Импортируем наше Flask приложение


class TestHandlers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True

    def test_health_check(self):
        response = self.app.get('/api/healthcheck')
        print("Health Check Response Status Code:", response.status_code)
        print("Health Check Response Data:", response.get_json())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_get_latest_order(self):
        response = self.app.get('/api/latest_order')
        print("Latest Order Response Status Code:", response.status_code)

        data = response.get_json()

        # Проверяем наличие всех ключей в ответе
        self.assertIn('order_id', data)
        self.assertIn('date', data)
        self.assertIn('status', data)
        self.assertIn('items', data)
        self.assertIn('total_amount', data)
        self.assertIn('delivery_address', data)
        self.assertIn('payment_method', data)

        # Проверяем значения
        self.assertEqual(data['order_id'], "123456")
        self.assertEqual(data['status'], "delivered")
        self.assertEqual(data['total_amount'], 159.97)
        self.assertEqual(data['delivery_address']['city'], "Moscow")
        self.assertEqual(data['payment_method'], "credit_card")

    def test_items_in_order(self):
        response = self.app.get('/api/latest_order')
        data = response.get_json()

        items = data['items']
        print("Number of items in order:", len(items))
        self.assertEqual(len(items), 2)  # Должно быть 2 товара

        # Проверяем первый товар
        self.assertEqual(items[0]['item_id'], "987654")
        self.assertEqual(items[0]['name'], "Product 1")
        self.assertEqual(items[0]['quantity'], 2)
        self.assertEqual(items[0]['price'], 29.99)

        # Проверяем второй товар
        self.assertEqual(items[1]['item_id'], "654321")
        self.assertEqual(items[1]['name'], "Product 2")
        self.assertEqual(items[1]['quantity'], 1)
        self.assertEqual(items[1]['price'], 99.99)


if __name__ == '__main__':
    unittest.main()
