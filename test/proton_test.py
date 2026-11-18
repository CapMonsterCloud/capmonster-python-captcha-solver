import unittest

from pydantic import ValidationError
from capmonstercloudclient.requests import ProtonCustomTaskRequest, ProxyInfo


class ProtonCustomTaskRequestTest(unittest.TestCase):
    websiteUrlExample = "https://example.com/"
    metadataExample = {
        "HumanVerificationToken": "your-verification-token",
        "pageAction": "login",
    }

    def setUp(self):
        self.proxy = ProxyInfo(
            proxyType="http",
            proxyAddress="8.8.8.8",
            proxyPort=8080,
            proxyLogin="proxyLoginHere",
            proxyPassword="proxyPasswordHere",
        )

    def testRequiresProxy(self):
        self.assertRaises(
            RuntimeError,
            ProtonCustomTaskRequest,
            websiteUrl=self.websiteUrlExample,
            metadata=self.metadataExample,
        )

    def testAllRequiredFieldsFilling(self):
        request = ProtonCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            metadata=self.metadataExample,
            proxy=self.proxy,
            userAgent="UA",
        )
        request_dict = request.getTaskDict()
        for key in ["type", "class", "websiteURL", "metadata", "userAgent",
                    "proxyType", "proxyAddress", "proxyPort", "proxyLogin", "proxyPassword"]:
            self.assertIn(key, request_dict)
        self.assertEqual(request_dict["type"], "CustomTask")
        self.assertEqual(request_dict["class"], "proton")
        self.assertEqual(request_dict["metadata"], self.metadataExample)
        self.assertNotIn("websiteKey", request_dict)

    def testUserAgentNotSentWhenNone(self):
        request_dict = ProtonCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            metadata=self.metadataExample,
            proxy=self.proxy,
        ).getTaskDict()
        self.assertNotIn("userAgent", request_dict)

    def testPageActionValues(self):
        for action in ["login", "signup"]:
            ProtonCustomTaskRequest(
                websiteUrl=self.websiteUrlExample,
                metadata={**self.metadataExample, "pageAction": action},
                proxy=self.proxy,
            )
        with self.assertRaises(TypeError):
            ProtonCustomTaskRequest(
                websiteUrl=self.websiteUrlExample,
                metadata={**self.metadataExample, "pageAction": "logout"},
                proxy=self.proxy,
            )

    def testMetadataValidation(self):
        for missing in ["HumanVerificationToken", "pageAction"]:
            metadata = self.metadataExample.copy()
            metadata.pop(missing)
            with self.assertRaises(TypeError):
                ProtonCustomTaskRequest(
                    websiteUrl=self.websiteUrlExample,
                    metadata=metadata,
                    proxy=self.proxy,
                )
        with self.assertRaises(TypeError):
            ProtonCustomTaskRequest(
                websiteUrl=self.websiteUrlExample,
                metadata={**self.metadataExample, "unknownKey": "value"},
                proxy=self.proxy,
            )
        with self.assertRaises(ValidationError):
            ProtonCustomTaskRequest(
                websiteUrl=self.websiteUrlExample,
                metadata={**self.metadataExample, "HumanVerificationToken": ["a"]},
                proxy=self.proxy,
            )

    def testMissingWebsiteUrl(self):
        self.assertRaises(
            ValidationError,
            ProtonCustomTaskRequest,
            metadata=self.metadataExample,
            proxy=self.proxy,
        )


if __name__ == "__main__":
    unittest.main()
