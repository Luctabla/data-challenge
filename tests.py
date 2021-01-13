from app import app
import unittest
import json
import config


class CountryTestCase(unittest.TestCase):
    def test_countries_by_indicator(self):
        client = app.test_client(self)
        response = client.get("/countries_by/?indicator=HS_LEB&index_value=20")
        self.assertEqual(response.status_code, config.HTTP_200_OK)
        self.assertEqual(json.loads(response.data),
        {"2547":"Australia","2548":"Austria","2549":"Belgium","2550":"Canada","2551":"Czech Republic"})

if __name__ == "__main__":
    unittest.main()