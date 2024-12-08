import unittest
from for_tests_12_1 import Runner
from for_tests_12_2 import Tournament


def skip_if_frozen(func):
    """
    Пропускаем тест, если он заморожен is_frozen == True.
    """

    def wrapper(self, *args, **kwargs):
        if getattr(self, "is_frozen", False):
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            return func(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_race_usain_and_nick(self):
        tournament = Tournament(90, Runner("Усэйн", 10), Runner("Ник", 3))
        results = tournament.start()
        self.assertTrue(results[max(results.keys())] == "Ник")

    @skip_if_frozen
    def test_race_andrey_and_nick(self):
        tournament = Tournament(90, Runner("Андрей", 9), Runner("Ник", 3))
        results = tournament.start()
        self.assertTrue(results[max(results.keys())] == "Ник")

    @skip_if_frozen
    def test_race_usain_andrey_and_nick(self):
        tournament = Tournament(90, Runner("Усэйн", 10), Runner("Андрей", 9),
                                Runner("Ник", 3))
        results = tournament.start()
        self.assertTrue(results[max(results.keys())] == "Ник")

