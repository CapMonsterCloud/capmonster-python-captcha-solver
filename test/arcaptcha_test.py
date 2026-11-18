import unittest

from pydantic import ValidationError
from capmonstercloudclient.requests import ArCaptchaRequest


class ArCaptchaRequestTest(unittest.TestCase):
    websiteUrlExample = "https://example.com/"
    websiteKeyExample = "your-website-key"

    def testAllFieldsFilling(self):
        request = ArCaptchaRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
            isInvisible=False,
            userAgent="UA",
        )
        request_dict = request.getTaskDict()
        self.assertEqual(request_dict["type"], "ArCaptchaTask")
        self.assertEqual(request_dict["websiteURL"], self.websiteUrlExample)
        self.assertEqual(request_dict["websiteKey"], self.websiteKeyExample)
        self.assertEqual(request_dict["isInvisible"], False)
        self.assertEqual(request_dict["userAgent"], "UA")

    def testOptionalFieldsNotSentWhenNone(self):
        request_dict = ArCaptchaRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
        ).getTaskDict()
        self.assertNotIn("isInvisible", request_dict)
        self.assertNotIn("userAgent", request_dict)

    def testMissingRequiredFields(self):
        self.assertRaises(ValidationError, ArCaptchaRequest)
        self.assertRaises(
            ValidationError,
            ArCaptchaRequest,
            websiteUrl=self.websiteUrlExample,
        )
        self.assertRaises(
            ValidationError,
            ArCaptchaRequest,
            websiteKey=self.websiteKeyExample,
        )

    def testNoProxyKeys(self):
        request_dict = ArCaptchaRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
        ).getTaskDict()
        for key in ["proxyType", "proxyAddress", "proxyPort", "proxyLogin", "proxyPassword"]:
            self.assertNotIn(key, request_dict)


if __name__ == "__main__":
    unittest.main()
