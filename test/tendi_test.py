import unittest

from pydantic import ValidationError
from capmonstercloudclient.requests import TenDiCustomTaskRequest


class TenDiCustomTaskRequestTest(unittest.TestCase):
    websiteUrlExample = "https://example.com"
    websiteKeyExample = "189123456"
    userAgentExample = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

    def testCaptchaInputTypes(self):
        with self.assertRaises(ValidationError):
            request = TenDiCustomTaskRequest(
                websiteUrl=TenDiCustomTaskRequestTest.websiteUrlExample
            )

        with self.assertRaises(ValidationError):
            request = TenDiCustomTaskRequest(
                websiteKey=TenDiCustomTaskRequestTest.websiteKeyExample,
            )

        request = TenDiCustomTaskRequest(
            websiteUrl=TenDiCustomTaskRequestTest.websiteUrlExample,
            websiteKey=TenDiCustomTaskRequestTest.websiteKeyExample,
            userAgent=TenDiCustomTaskRequestTest.userAgentExample,
        )

    def testAllRequiredFieldsFilling(self):
        required_fields = ["class", "type", "websiteURL", "websiteKey"]
        request = TenDiCustomTaskRequest(
            websiteUrl=TenDiCustomTaskRequestTest.websiteUrlExample,
            websiteKey=TenDiCustomTaskRequestTest.websiteKeyExample,
        )
        request_dict = request.getTaskDict()
        for i in required_fields:
            self.assertTrue(
                i in list(request_dict.keys()),
                msg=f"Required field {i} not in {request_dict}",
            )

        self.assertEqual(request_dict["class"], "TenDI")
        self.assertEqual(request_dict["type"], "CustomTask")

    def testMetadataOptional(self):
        request = TenDiCustomTaskRequest(
            websiteUrl=TenDiCustomTaskRequestTest.websiteUrlExample,
            websiteKey=TenDiCustomTaskRequestTest.websiteKeyExample,
        )
        request_dict = request.getTaskDict()
        self.assertNotIn("metadata", request_dict)

    def testMetadataWithCaptchaUrl(self):
        request = TenDiCustomTaskRequest(
            websiteUrl=TenDiCustomTaskRequestTest.websiteUrlExample,
            websiteKey=TenDiCustomTaskRequestTest.websiteKeyExample,
            metadata={"captchaUrl": "https://example.com/TCaptcha.js"},
        )
        request_dict = request.getTaskDict()
        self.assertEqual(request_dict["metadata"]["captchaUrl"], "https://example.com/TCaptcha.js")

    def testMetadataWithAidEncrypted(self):
        request = TenDiCustomTaskRequest(
            websiteUrl=TenDiCustomTaskRequestTest.websiteUrlExample,
            websiteKey=TenDiCustomTaskRequestTest.websiteKeyExample,
            metadata={
                "captchaUrl": "https://example.com/TCaptcha.js",
                "aidEncrypted": "YOUR_AID_ENCRYPTED",
            },
        )
        request_dict = request.getTaskDict()
        self.assertEqual(request_dict["metadata"]["aidEncrypted"], "YOUR_AID_ENCRYPTED")
        self.assertEqual(request_dict["metadata"]["captchaUrl"], "https://example.com/TCaptcha.js")

    def testMetadataAidEncryptedOnly(self):
        request = TenDiCustomTaskRequest(
            websiteUrl=TenDiCustomTaskRequestTest.websiteUrlExample,
            websiteKey=TenDiCustomTaskRequestTest.websiteKeyExample,
            metadata={"aidEncrypted": "YOUR_AID_ENCRYPTED"},
        )
        self.assertEqual(request.getTaskDict()["metadata"], {"aidEncrypted": "YOUR_AID_ENCRYPTED"})

    def testMetadataAidEncryptedWrongType(self):
        for bad_value in (123, True):
            with self.assertRaises((TypeError, ValidationError)):
                TenDiCustomTaskRequest(
                    websiteUrl=TenDiCustomTaskRequestTest.websiteUrlExample,
                    websiteKey=TenDiCustomTaskRequestTest.websiteKeyExample,
                    metadata={"aidEncrypted": bad_value},
                )

    def testMetadataInvalidKey(self):
        self.assertRaises(
            TypeError,
            TenDiCustomTaskRequest,
            websiteUrl=TenDiCustomTaskRequestTest.websiteUrlExample,
            websiteKey=TenDiCustomTaskRequestTest.websiteKeyExample,
            metadata={"invalidKey": "value"},
        )


if __name__ == "__main__":
    unittest.main()
