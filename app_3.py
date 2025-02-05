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
        print("Health Check Status Code is as expected (200)")

        self.assertEqual(response.get_json(), {"status": "ok"})
        print("Health Check response data is correct")

    def test_get_latest_order(self):
        response = self.app.get('/api/latest_order')
        print("Latest Order Response Status Code:", response.status_code)

        self.assertEqual(response.status_code, 200)
        print("Latest Order Status Code is as expected (200)")

        data = response.get_json()

        # Проверяем наличие всех ключей в ответе
        self.assertIn('order_id', data)
        print("Key 'order_id' is present in response")

        self.assertIn('date', data)
        print("Key 'date' is present in response")

        self.assertIn('status', data)
        print("Key 'status' is present in response")

        self.assertIn('items', data)
        print("Key 'items' is present in response")

        self.assertIn('total_amount', data)
        print("Key 'total_amount' is present in response")

        self.assertIn('delivery_address', data)
        print("Key 'delivery_address' is present in response")

        self.assertIn('payment_method', data)
        print("Key 'payment_method' is present in response")

        # Проверяем значения
        self.assertEqual(data['order_id'], "123456")
        print("Order ID is as expected")

        self.assertEqual(data['status'], "delivered")
        print("Order status is as expected")

        self.assertEqual(data['total_amount'], 159.97)
        print("Total amount is as expected")

        self.assertEqual(data['delivery_address']['city'], "Moscow")
        print("Delivery city is as expected")

        self.assertEqual(data['payment_method'], "credit_card")
        print("Payment method is as expected")

    def test_items_in_order(self):
        response = self.app.get('/api/latest_order')
        data = response.get_json()

        items = data['items']
        print("Number of items in order:", len(items))

        self.assertEqual(len(items), 2)  # Должно быть 2 товара
        print("Number of items is as expected (2)")

        # Проверяем первый товар
        self.assertEqual(items[0]['item_id'], "987654")
        print("First item ID is as expected")

        self.assertEqual(items[0]['name'], "Product 1")
        print("First item name is as expected")

        self.assertEqual(items[0]['quantity'], 2)
        print("First item quantity is as expected")

        self.assertEqual(items[0]['price'], 29.99)
        print("First item price is as expected")

        # Проверяем второй товар
        self.assertEqual(items[1]['item_id'], "654321")
        print("Second item ID is as expected")

        self.assertEqual(items[1]['name'], "Product 2")
        print("Second item name is as expected")

        self.assertEqual(items[1]['quantity'], 1)
        print("Second item quantity is as expected")

        self.assertEqual(items[1]['price'], 99.99)
        print("Second item price is as expected")


if __name__ == '__main__':
    unittest.main()