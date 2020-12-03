import os, sys
import unittest

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


from hospital.Hospital import Hospital
from hospital.Hospital import Patients
from hospital.Hospital import (
    Employees,
    Doctors,
    CoronaSpecialist,
    FluSpecialist,
    Surgeon,
    Ophtalmologist,
    Administration,
    Janitor,
    Administrator,
)


class HospitalWhiteBoxTests(unittest.TestCase):
    def test_00_init(self):
        doc = CoronaSpecialist("Matthias Imhof", 24, "Dr. Dr. PHD")
        h = Hospital("Weid", doc)
        actual = h.list_all_doctors()
        self.assertEqual(actual, ["CoronaSpecialist"], "doctor was not successfully added")

    def test_01_assertError(self):
        self.assertRaises(Warning, Hospital, "", "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
