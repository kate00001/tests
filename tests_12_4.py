import logging
from for_tests_12_4 import Runner
import unittest

logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode="w",
    format="%(levelname)s: %(message)s",
    encoding="utf-8"
)

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """
        Тест метода walk
        """
        try:
            runner = Runner("TestRunner", -5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для объекта Runner: {e}")

    def test_run(self):
        """
        Тест метода run
        """
        try:
            runner = Runner(12345, 5)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")

