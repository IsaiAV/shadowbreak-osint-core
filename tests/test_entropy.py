import unittest
from shadowbreak.entropy_utils import compute_entropy, narrative_drift

class TestEntropyFunctions(unittest.TestCase):
    def test_entropy_basic(self):
        self.assertAlmostEqual(compute_entropy("a a b"), 0.9183, places=3)

    def test_entropy_zero(self):
        self.assertEqual(compute_entropy("repeat repeat repeat"), 0.0)

    def test_narrative_drift(self):
        t1 = "Everything is fine and calm."
        t2 = "I can't sleep. I'm scared. They're watching me."
        drift = narrative_drift(t1, t2)
        self.assertGreater(drift, 0)

if __name__ == '__main__':
    unittest.main()
