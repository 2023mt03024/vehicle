from mockito import mock, verify
import unittest

from app import app
from initdb import initdb

class AppTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        initdb()

    @classmethod
    def tearDownClass(cls):
        initdb()

    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()
    
    def tearDown(self):
        self.ctx.pop()
    
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert 'OK' in response.get_data(as_text=True)

    def test_vehicle_exists(self):
        response = self.client.get("/vehicle?vehicle_number=TS07HR9551")
        assert response.status_code == 200
        assert 'RAMAKRISHNA KUMMARI' in response.get_data(as_text=True)

    def test_vehicle_not_exist(self):
        response = self.client.get("/vehicle?vehicle_number=TS07HR9561")
        assert response.status_code == 200
        assert 'Not Available' in response.get_data(as_text=True)
