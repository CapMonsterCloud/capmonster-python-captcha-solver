import unittest

from pydantic import ValidationError
from capmonstercloudclient.requests import RecaptchaV2EnterpriseRequest


class RecaptchaV2EnterpriseRequestTest(unittest.TestCase):
    websiteUrlExample = "https://example.com"
    websiteKeyExample = "6Le0xVgUAAAAAIt20XEB4rVhYOODgTl00d8juDob"

    def test_min_score_in_task_dict(self):
        request = RecaptchaV2EnterpriseRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
            minScore=0.7,
        )
        self.assertEqual(request.getTaskDict()["minScore"], 0.7)

    def test_min_score_omitted(self):
        request = RecaptchaV2EnterpriseRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
        )
        self.assertNotIn("minScore", request.getTaskDict())

    def test_min_score_out_of_range(self):
        for value in (0.0, 1.0):
            with self.assertRaises(ValidationError):
                RecaptchaV2EnterpriseRequest(
                    websiteUrl=self.websiteUrlExample,
                    websiteKey=self.websiteKeyExample,
                    minScore=value,
                )


if __name__ == "__main__":
    unittest.main()
