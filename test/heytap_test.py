import unittest

from pydantic import ValidationError
from capmonstercloudclient.requests import HeyTapCustomTaskRequest, ProxyInfo


class HeyTapCustomTaskRequestTest(unittest.TestCase):
    websiteUrlExample = "https://example.com/"
    websiteKeyExample = "your-website-key"
    metadataExample = {"apiServer": "api.example.com"}

    def testAllFieldsFilling(self):
        request = HeyTapCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
            userAgent="UA",
            metadata=self.metadataExample,
        )
        request_dict = request.getTaskDict()
        self.assertEqual(request_dict["type"], "CustomTask")
        self.assertEqual(request_dict["class"], "heytap")
        self.assertEqual(request_dict["websiteURL"], self.websiteUrlExample)
        self.assertEqual(request_dict["websiteKey"], self.websiteKeyExample)
        self.assertEqual(request_dict["userAgent"], "UA")
        self.assertEqual(request_dict["metadata"], self.metadataExample)

    def testOptionalFieldsNotSentWhenNone(self):
        request_dict = HeyTapCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
        ).getTaskDict()
        self.assertNotIn("metadata", request_dict)
        self.assertNotIn("userAgent", request_dict)

    def testMissingRequiredFields(self):
        self.assertRaises(ValidationError, HeyTapCustomTaskRequest)
        self.assertRaises(
            ValidationError,
            HeyTapCustomTaskRequest,
            websiteUrl=self.websiteUrlExample,
        )
        self.assertRaises(
            ValidationError,
            HeyTapCustomTaskRequest,
            websiteKey=self.websiteKeyExample,
        )

    def testMetadataValidation(self):
        with self.assertRaises(TypeError):
            HeyTapCustomTaskRequest(
                websiteUrl=self.websiteUrlExample,
                websiteKey=self.websiteKeyExample,
                metadata={"unknownKey": "value"},
            )
        with self.assertRaises(TypeError):
            HeyTapCustomTaskRequest(
                websiteUrl=self.websiteUrlExample,
                websiteKey=self.websiteKeyExample,
                metadata={"apiServer": "https://api.example.com"},
            )
        with self.assertRaises(ValidationError):
            HeyTapCustomTaskRequest(
                websiteUrl=self.websiteUrlExample,
                websiteKey=self.websiteKeyExample,
                metadata={"apiServer": ["not", "a", "str"]},
            )

    def testProxyNotSent(self):
        proxy = ProxyInfo(
            proxyType="http",
            proxyAddress="8.8.8.8",
            proxyPort=8080,
            proxyLogin="proxyLoginHere",
            proxyPassword="proxyPasswordHere",
        )
        request_dict = HeyTapCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
            proxy=proxy,
        ).getTaskDict()
        for key in ["proxyType", "proxyAddress", "proxyPort", "proxyLogin", "proxyPassword"]:
            self.assertNotIn(key, request_dict)


if __name__ == "__main__":
    unittest.main()
