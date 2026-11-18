import unittest

from pydantic import ValidationError
from capmonstercloudclient.requests import FengkongCloudCustomTaskRequest, ProxyInfo


class FengkongCloudCustomTaskRequestTest(unittest.TestCase):
    websiteUrlExample = "https://www.example.com/"
    websiteKeyExample = "your-website-key"
    metadataExample = {"apiJsUrl": "https://example.com/path/to/script.js"}

    def testAllFieldsFilling(self):
        request = FengkongCloudCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
            userAgent="UA",
            metadata=self.metadataExample,
        )
        request_dict = request.getTaskDict()
        self.assertEqual(request_dict["type"], "CustomTask")
        self.assertEqual(request_dict["class"], "fengkongcloud")
        self.assertEqual(request_dict["websiteURL"], self.websiteUrlExample)
        self.assertEqual(request_dict["websiteKey"], self.websiteKeyExample)
        self.assertEqual(request_dict["userAgent"], "UA")
        self.assertEqual(request_dict["metadata"], self.metadataExample)

    def testOptionalFieldsNotSentWhenNone(self):
        request_dict = FengkongCloudCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
        ).getTaskDict()
        self.assertNotIn("metadata", request_dict)
        self.assertNotIn("userAgent", request_dict)

    def testMissingRequiredFields(self):
        self.assertRaises(ValidationError, FengkongCloudCustomTaskRequest)
        self.assertRaises(
            ValidationError,
            FengkongCloudCustomTaskRequest,
            websiteUrl=self.websiteUrlExample,
        )
        self.assertRaises(
            ValidationError,
            FengkongCloudCustomTaskRequest,
            websiteKey=self.websiteKeyExample,
        )

    def testMetadataValidation(self):
        with self.assertRaises(TypeError):
            FengkongCloudCustomTaskRequest(
                websiteUrl=self.websiteUrlExample,
                websiteKey=self.websiteKeyExample,
                metadata={"unknownKey": "value"},
            )
        with self.assertRaises(ValidationError):
            FengkongCloudCustomTaskRequest(
                websiteUrl=self.websiteUrlExample,
                websiteKey=self.websiteKeyExample,
                metadata={"apiJsUrl": ["not", "a", "str"]},
            )

    def testProxyNotSent(self):
        proxy = ProxyInfo(
            proxyType="http",
            proxyAddress="8.8.8.8",
            proxyPort=8080,
            proxyLogin="proxyLoginHere",
            proxyPassword="proxyPasswordHere",
        )
        request_dict = FengkongCloudCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
            proxy=proxy,
        ).getTaskDict()
        for key in ["proxyType", "proxyAddress", "proxyPort", "proxyLogin", "proxyPassword"]:
            self.assertNotIn(key, request_dict)


if __name__ == "__main__":
    unittest.main()
