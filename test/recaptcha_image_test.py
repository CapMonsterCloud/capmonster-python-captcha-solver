import unittest

from pydantic import ValidationError
from capmonstercloudclient.requests import RecaptchaComplexImageTaskRequest
from capmonstercloudclient.exceptions import (
    NumbersImagesErrors,
    TaskNotDefinedError,
    ZeroImagesErrors,
    UserAgentNotDefinedError,
)


class RecaptchaImageRequestTest(unittest.TestCase):
    websiteUrlExample = (
        "https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=middle"
    )
    imageUrlsExamples = ["https://i.postimg.cc/yYjg75Kv/payloadtraffic.jpg"]
    metadataExample = {
        "Task": "Click on traffic lights",
        "Grid": "3x3",
        "TaskDefinition": "/m/015qff",
    }

    def testImagesTypes(self):
        with self.assertRaises(ValidationError):
            request = RecaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata=RecaptchaImageRequestTest.metadataExample,
                imagesBase64="[]",
            )

        with self.assertRaises(ValidationError):
            request = RecaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata=RecaptchaImageRequestTest.metadataExample,
                imagesUrls="[]",
            )

    def testImagesFilling(self):
        with self.assertRaises(
            ZeroImagesErrors,
            msg="Empty array imagesUrls must be cause ZeroImagesErrors",
        ):
            request = RecaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata=RecaptchaImageRequestTest.metadataExample,
                imagesUrls=[],
                userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36.",
            )

        with self.assertRaises(
            ZeroImagesErrors,
            msg="Empty array imagesBase64 must be cause ZeroImagesErrors",
        ):
            request = RecaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata=RecaptchaImageRequestTest.metadataExample,
                imagesBase64=[],
            )

        with self.assertRaises(
            ZeroImagesErrors,
            msg="Both empty arrays imagesBase64 and imagesUrls must be cause ZeroImagesErrors",
        ):
            request = RecaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata=RecaptchaImageRequestTest.metadataExample,
            )
            request.getTaskDict()

    def testNumbersImages(self):
        with self.assertRaises(
            NumbersImagesErrors, msg="Empty array must be cause ZeroImagesErrors"
        ):
            request = RecaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata=RecaptchaImageRequestTest.metadataExample,
                imagesUrls=RecaptchaImageRequestTest.imageUrlsExamples * 2,
                userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36.",
            )

        with self.assertRaises(
            NumbersImagesErrors, msg="Empty array must be cause ZeroImagesErrors"
        ):
            request = RecaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata=RecaptchaImageRequestTest.metadataExample,
                imagesBase64=["base64image"] * 2,
                userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36.",
            )

    def testAllRequiredFieldsFilling(self):
        required_fields = ["class", "type", "websiteUrl", "metadata", "userAgent"]
        metadata_fields = ["Task", "TaskDefinition", "Grid"]
        request = RecaptchaComplexImageTaskRequest(
            websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
            metadata=RecaptchaImageRequestTest.metadataExample,
            imagesUrls=RecaptchaImageRequestTest.imageUrlsExamples,
            userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36.",
        )
        request_dict = request.getTaskDict()
        for i in required_fields:
            self.assertTrue(
                i in list(request_dict.keys()),
                msg=f"Required field {i} not in {request_dict}",
            )

        metadata_dict = request_dict["metadata"]
        for i in metadata_fields:
            self.assertTrue(
                i in list(metadata_dict.keys()),
                msg=f"Required field {i} not in {request_dict}",
            )

        self.assertEqual(request_dict["class"], "recaptcha")
        self.assertEqual(request_dict["type"], "ComplexImageTask")

    def testTaskDefined(self):
        with self.assertRaises(
            TaskNotDefinedError,
            msg='Expect that empty "Task" field will be cause TaskNotDefinedError',
        ):
            request = RecaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata={},
                imagesUrls=RecaptchaImageRequestTest.imageUrlsExamples,
            )

        with self.assertRaises(TaskNotDefinedError):
            request = RecaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata={"dsfsdf": "sdfsdf"},
                imagesUrls=RecaptchaImageRequestTest.imageUrlsExamples,
                userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36.",
            )

    def testTaskOrTaskDefinitionAlone(self):
        # "Task" alone (no "TaskDefinition") must be accepted.
        request = RecaptchaComplexImageTaskRequest(
            websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
            metadata={"Task": "Click on traffic lights", "Grid": "3x3"},
            imagesUrls=RecaptchaImageRequestTest.imageUrlsExamples,
        )
        task_dictionary = request.getTaskDict()
        self.assertIn("Task", task_dictionary["metadata"])
        self.assertNotIn("TaskDefinition", task_dictionary["metadata"])

        # "TaskDefinition" alone (no "Task") must be accepted.
        request = RecaptchaComplexImageTaskRequest(
            websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
            metadata={"TaskDefinition": "/m/015qff", "Grid": "3x3"},
            imagesUrls=RecaptchaImageRequestTest.imageUrlsExamples,
        )
        task_dictionary = request.getTaskDict()
        self.assertIn("TaskDefinition", task_dictionary["metadata"])
        self.assertNotIn("Task", task_dictionary["metadata"])

        # Neither "Task" nor "TaskDefinition" must still fail.
        with self.assertRaises(TaskNotDefinedError):
            RecaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata={"Grid": "3x3"},
                imagesUrls=RecaptchaImageRequestTest.imageUrlsExamples,
            )

    @unittest.skip("Doesnt work right now")
    def testUserAgentWithUrl(self):
        with self.assertRaises(UserAgentNotDefinedError):
            request = RecaptchaComplexImageTaskRequest(
                metadata=RecaptchaImageRequestTest.metadataExample,
                imagesUrls=RecaptchaImageRequestTest.imageUrlsExamples,
            )
            request.getTaskDict()


if __name__ == "__main__":
    unittest.main()
