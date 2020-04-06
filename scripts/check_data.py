import json
import unittest
from pathlib import Path

class CheckJSONData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data_path = Path(__file__).parent.parent / "dati-json" / "dpc-covid19-ita-andamento-nazionale.json"
        with data_path.open(mode="r") as f:
            cls.json_data = json.load(f)

    def setUp(self):
        self.json_data = self.__class__.json_data

    def test_deaths_growing_or_equal_of_prev_day(self):
        n = 0
        for e in self.json_data:
            self.assertGreaterEqual(e["deceduti"], n)
            n = e["deceduti"]

    def test_number_of_test_growing_or_equal_of_prev_day(self):
        n = 0
        for e in self.json_data:
            self.assertGreaterEqual(e["tamponi"], n)
            n = e["tamponi"]

    def test_total_cases_growing_or_equal_of_prev_day(self):
        n = 0
        for e in self.json_data:
            self.assertGreaterEqual(e["totale_casi"], n)
            n = e["totale_casi"]

    def test_healed_growing_or_equal_of_prev_day(self):
        n = 0
        for e in self.json_data:
            self.assertGreaterEqual(e["dimessi_guariti"], n)
            n = e["dimessi_guariti"]

    def test_total_hospitalized_as_sum_of_icu_and_others_in_hospital(self):
        for e in self.json_data:
            tot_hosp_json = e["totale_ospedalizzati"]
            tot_hosp_calc = (e["terapia_intensiva"] + e["ricoverati_con_sintomi"])
            self.assertEqual(tot_hosp_json, tot_hosp_calc)

    def test_total_positives_as_sum_of_total_hospitalized_and_home_confinement(self):
        for e in self.json_data:
            tot_positives_json = e["totale_positivi"]
            tot_positives_calc = e["isolamento_domiciliare"] + e["totale_ospedalizzati"]
            self.assertEqual(tot_positives_json, tot_positives_calc)

    def test_total_positives_summing_new_positives_minus_deaths_and_healed(self):
        for i in range(1, len(self.json_data)):
            e = self.json_data[i]
            prev = self.json_data[i-1]
            tot_positives_json = e["totale_positivi"]
            tot_positives_calc = prev["totale_positivi"] + e["nuovi_positivi"] - (e["deceduti"] - prev["deceduti"]) - (e["dimessi_guariti"] - prev["dimessi_guariti"])
            self.assertEqual(tot_positives_json, tot_positives_calc)

    def test_total_cases_as_sum_of_total_positives_healed_and_deaths(self):
        for e in self.json_data:
            tot_cases_json = e["totale_casi"]
            tot_cases_calc = e["totale_positivi"] + e["dimessi_guariti"] + e["deceduti"]
            self.assertEqual(tot_cases_json, tot_cases_calc)

    def test_total_positives_variation_as_total_positives_diff(self):
        for i in range(1, len(self.json_data)):
            e = self.json_data[i]
            prev = self.json_data[i-1]
            total_positives_diff_json = e["variazione_totale_positivi"]
            total_positives_diff_calc = e["totale_positivi"] - prev["totale_positivi"]
            self.assertEqual(total_positives_diff_json, total_positives_diff_calc)

if __name__ == '__main__':
    unittest.main(verbosity=2)
