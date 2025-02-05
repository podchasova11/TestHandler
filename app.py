from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/latest_order', methods=['GET'])
def get_latest_order():
    order = {
        "order_id": "123456",
        "date": "2024-07-27T12:34:56Z",
        "status": "delivered",
        "items": [
            {
                "item_id": "987654",
                "name": "Product 1",
                "quantity": 2,
                "price": 29.99
            },
            {
                "item_id": "654321",
                "name": "Product 2",
                "quantity": 1,
                "price": 99.99
            }
        ],
        "total_amount": 159.97,
        "delivery_address": {
            "street": "123 Main St",
            "city": "Moscow",
            "postal_code": "101000",
            "country": "Russia"
        },
        "payment_method": "credit_card"
    }

    return jsonify(order)


if __name__ == '__main__':
    app.run(debug=True)
