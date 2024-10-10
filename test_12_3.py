import unittest
import runner
import runner_and_tournament


class RunnerTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        r1 = runner.Runner('Гоша')
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50, f'{r1.name} пробежал {r1.distance}, а должен был 50')

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        r2 = runner.Runner('Сёма')
        for _ in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100, f'{r2.name} пробежал {r2.distance}, а должен был 100')

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r3 = runner.Runner('Гога')
        r4 = runner.Runner('Гера')
        for _ in range(10):
            r3.walk()
            r4.run()
        self.assertNotEqual(r3.distance, r4.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = None

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            formatted_result = '{' + ', '.join(f'{place}: {runner}' for place, runner in result.items()) + '}'
            print(formatted_result)

    def setUp(self):
        self.r_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.r_2 = runner_and_tournament.Runner('Андрей', 9)
        self.r_3 = runner_and_tournament.Runner('Ник', 3)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run_first(self):
        tournament = runner_and_tournament.Tournament(90, self.r_1, self.r_3)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run_second(self):
        tournament = runner_and_tournament.Tournament(90, self.r_2, self.r_3)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run_third(self):
        tournament = runner_and_tournament.Tournament(90, self.r_2, self.r_1, self.r_3)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")


if __name__ == '__main__':
    unittest.main()