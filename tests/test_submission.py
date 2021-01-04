import unittest
import application.submission as sumbission

class TestSubmission(unittest.TestCase):

    def test_submission_validation(self):
        self.assertTrue(True)
        subm = sumbission.Submission()
        self.assertIsNotNone(subm)
        self.assertFalse(subm.is_validated)
        self.assertIsNone(subm.dtg_submit)

        subm.validate()
        self.assertTrue(subm.is_validated)
        self.assertIsNone(subm.dtg_submit)
