import unittest

from pydantic import ValidationError
from capmonstercloudclient.requests import HuntCustomTaskRequest, ProxyInfo


class HuntCustomTaskRequestTest(unittest.TestCase):
    websiteUrlExample = "https://example.com"
    userAgentExample = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    apiGetLibExample = "https://example.com/hd-api/external/apps/a2157wab1045d68672a63557e0n2a77edbfd15ea/api.js"
    dataExample = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
    widgetUrlExample = "https://captcha.example.com/widget?hash=abc123"

    def setUp(self):
        self.proxy = ProxyInfo(
            proxyType="http",
            proxyAddress="8.8.8.8",
            proxyPort=8080,
            proxyLogin="proxyLoginHere",
            proxyPassword="proxyPasswordHere"
        )

    def test_hunt_request_required_fields(self):
        required_fields = ["type", "class", "websiteURL", "metadata",
                           "proxyType", "proxyAddress", "proxyPort", "proxyLogin", "proxyPassword"]
        metadata_required_fields = ["apiGetLib"]
        metadata_example = {
            "apiGetLib": self.apiGetLibExample,
        }
        request = HuntCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            metadata=metadata_example,
            proxy=self.proxy,
        )
        task_dictionary = request.getTaskDict()
        for f in required_fields:
            self.assertTrue(
                f in list(task_dictionary.keys()),
                msg=f'Required captcha input key "{f}" does not include to request.',
            )
        for f in metadata_required_fields:
            self.assertTrue(
                f in list(task_dictionary["metadata"].keys()),
                msg=f'Required captcha input key "{f}" does not include to request.',
            )
        self.assertEqual(task_dictionary["class"], "HUNT")
        self.assertEqual(task_dictionary["type"], "CustomTask")

    def test_hunt_metadata_validation(self):
        base_kwargs = {
            "websiteUrl": self.websiteUrlExample,
            "metadata": {},
            "proxy": self.proxy,
        }
        self.assertRaises(TypeError, HuntCustomTaskRequest, **base_kwargs)
        base_kwargs["metadata"]["apiGetLib"] = self.apiGetLibExample
        HuntCustomTaskRequest(**base_kwargs)

    def test_hunt_metadata_with_data(self):
        metadata_example = {
            "apiGetLib": self.apiGetLibExample,
            "data": self.dataExample,
        }
        request = HuntCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            metadata=metadata_example,
            proxy=self.proxy,
        )
        task_dictionary = request.getTaskDict()
        self.assertEqual(task_dictionary["metadata"]["data"], self.dataExample)

    def test_hunt_missing_fields(self):
        metadata_example = {
            "apiGetLib": self.apiGetLibExample,
        }
        # No proxy -> RuntimeError
        base_kwargs = {}
        self.assertRaises(RuntimeError, HuntCustomTaskRequest, **base_kwargs)
        # With proxy but missing other required fields
        base_kwargs.update({"proxy": self.proxy})
        self.assertRaises(ValidationError, HuntCustomTaskRequest, **base_kwargs)
        base_kwargs.update({"websiteUrl": self.websiteUrlExample})
        self.assertRaises(ValidationError, HuntCustomTaskRequest, **base_kwargs)
        base_kwargs.update({"metadata": metadata_example})
        HuntCustomTaskRequest(**base_kwargs)

    def test_hunt_metadata_with_widget_url(self):
        metadata_example = {
            "apiGetLib": self.apiGetLibExample,
            "widgetUrl": self.widgetUrlExample,
        }
        request = HuntCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            metadata=metadata_example,
            proxy=self.proxy,
        )
        task_dictionary = request.getTaskDict()
        self.assertEqual(task_dictionary["metadata"]["widgetUrl"], self.widgetUrlExample)

    def test_hunt_data_and_widget_url_mutually_exclusive(self):
        metadata_example = {
            "apiGetLib": self.apiGetLibExample,
            "data": self.dataExample,
            "widgetUrl": self.widgetUrlExample,
        }
        self.assertRaises(
            TypeError,
            HuntCustomTaskRequest,
            websiteUrl=self.websiteUrlExample,
            metadata=metadata_example,
            proxy=self.proxy,
        )

    def test_hunt_requires_proxy(self):
        metadata_example = {
            "apiGetLib": self.apiGetLibExample,
        }
        self.assertRaises(
            RuntimeError,
            HuntCustomTaskRequest,
            websiteUrl=self.websiteUrlExample,
            metadata=metadata_example,
        )

    def test_hunt_optional_useragent(self):
        metadata_example = {
            "apiGetLib": self.apiGetLibExample,
        }
        request = HuntCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            metadata=metadata_example,
            proxy=self.proxy,
            userAgent=self.userAgentExample,
        )
        task_dictionary = request.getTaskDict()
        self.assertEqual(task_dictionary["userAgent"], self.userAgentExample)


if __name__ == "__main__":
    unittest.main()
