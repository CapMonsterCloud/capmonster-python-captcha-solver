import asyncio
import unittest
from unittest.mock import AsyncMock, patch

from capmonstercloudclient.requests import TurnstileRequest
from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.captchaResult import CaptchaResult


class CostTest(unittest.TestCase):
    def _solve(self, result_response):
        client = CapMonsterClient(options=ClientOptions(api_key="YOUR_API_KEY"))
        request = TurnstileRequest(
            websiteURL="https://example.com/", websiteKey="key123"
        )
        with patch.object(
            CapMonsterClient, "_createTask",
            new=AsyncMock(return_value={"errorId": 0, "taskId": 1}),
        ), patch.object(
            CapMonsterClient, "_getTaskResult",
            new=AsyncMock(return_value=result_response),
        ):
            return asyncio.run(client.solve_captcha(request))

    def test_captcha_result_cost(self):
        self.assertEqual(CaptchaResult(solution={"token": "t"}, cost=0.0003).cost, 0.0003)
        self.assertIsNone(CaptchaResult(solution={"token": "t"}).cost)

    def test_cost_returned_with_solution(self):
        response = self._solve(
            {"errorId": 0, "status": "ready", "cost": 0.0003, "solution": {"token": "t"}}
        )
        self.assertEqual(response, {"token": "t", "cost": 0.0003})

    def test_no_cost_in_response(self):
        response = self._solve(
            {"errorId": 0, "status": "ready", "solution": {"token": "t"}}
        )
        self.assertEqual(response, {"token": "t"})


if __name__ == "__main__":
    unittest.main()
