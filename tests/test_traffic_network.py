import unittest
from traffic import traffic_network

class TestTrafficNetwork(unittest.TestCase):
    def test_max_vehicle_flow(self):
        flow_value, _ = traffic_network.max_vehicle_flow()
        self.assertEqual(flow_value, 14)  # valeur attendue déterminée par calcul manuel

if __name__ == "__main__":
    unittest.main()
