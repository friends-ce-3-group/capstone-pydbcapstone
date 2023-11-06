from app import app
import json


@app.route('/api/cardsCatalog', methods=['GET'])
def cardsCatalog():
    data = [
        {
        "key": "farewell1",
        "category": "Farewell",
        "path": "farewell1.jpg",
        "backgroundColor": "#002744"
        },
        {
        "key": "birthday1",
        "category": "Birthday",
        "path": "birthday1.jpg",
        "backgroundColor": "#ffffff"
        },
        {
        "key": "wedding1",
        "category": "Wedding",
        "path": "wedding1.jpg",
        "backgroundColor": "#FFFFFF"
        },
        {
        "key": "anniversary1",
        "category": "Anniversary",
        "path": "anniversary1.jpg",
        "backgroundColor": "#FFFFFF"
        },
    ]

    response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')
    

    return response
