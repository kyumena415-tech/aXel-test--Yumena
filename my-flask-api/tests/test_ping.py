import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app

def test_ping():
    client = app.app.test_client()
    response = client.get('/api/ping')
    assert response.status_code == 200
    assert response.get_json() == {'pong': True}
