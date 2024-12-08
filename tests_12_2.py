import unittest
from for_tests_12_2 import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print(f"Test {key}: {result}")

    def test_race_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        TournamentTest.all_results[1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_race_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results[2] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_race_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results[3] = results
        self.assertTrue(results[max(results.keys())] == "Ник")


if __name__ == "__main__":
    unittest.main()
