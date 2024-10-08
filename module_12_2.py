from unittest import TestCase
from runner_and_tournament import Runner, Tournament


class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.r_1 = Runner("Усейн", 10)
        self.r_2 = Runner("Андрей", 9)
        self.r_3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            formatted_result = '{' + ', '.join(f'{place}: {runner}' for place, runner in result.items()) + '}'
            print(formatted_result)

    def test_1(self):
        tournament = Tournament(90,  self.r_1, self.r_3)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")

    def test_2(self):
        tournament = Tournament(90, self.r_2, self.r_3)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")

    def test_3(self):
        tournament = Tournament(90, self.r_2,  self.r_1, self.r_3)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")


if __name__ == '__main__':
    unittest.main()
