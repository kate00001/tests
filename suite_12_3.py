import unittest
from tests_12_3 import TournamentTest
from tests_12_3 import RunnerTest


suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

if __name__ == "__main__":
    runner.run(suite)
