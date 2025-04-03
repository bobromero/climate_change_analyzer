import unittest
import pandas as pd
import src.algorithms as algorithms


class TestAlgorithms(unittest.TestCase):
    def test_prep(self):
        data = {
            "Start Year": [2020, 2021, 2022],
            "Start Month": [1, 2, 3],
            "Latitude": [34.05, 36.16, 40.71],
            "Longitude": [-118.25, -115.15, -74.00],
            "Magnitude": [5.0, 6.0, 7.0],
        }
        df = pd.DataFrame(
            data,
        )
        result = algorithms.prep(df)
        self.assertIsNotNone(result)
        return result

    def test_pred(self):
        data = {
            "Start Year": [2020, 2021, 2022],
            "Start Month": [1, 2, 3],
            "Latitude": [34.05, 36.16, 40.71],
            "Longitude": [-118.25, -115.15, -74.00],
            "Magnitude": [5.0, 6.0, 7.0],
        }
        df = pd.DataFrame(
            data,
        )
        model = self.test_prep()

    def test_vis(self):
        # Add your test case for the vis function
        pass


if __name__ == "main":
    unittest.main()
