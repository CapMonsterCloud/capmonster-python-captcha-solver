# CapMonster Cloud Python SDK: AI Captcha Solver & Captcha Bypass

> **🔄 Migrating from 2Captcha or Capsolver?** CapMonster Cloud is a fast, cost-effective **2captcha alternative** and **capsolver alternative**: reCAPTCHA v3 from **$0.90 per 1,000 solves**, which is **up to 38% cheaper than 2Captcha** and **10% cheaper than Capsolver**, with an API response time of **≤ 2 s**. Already have software built for 2Captcha? CapMonster Cloud [supports the 2Captcha API format](https://docs.capmonster.cloud/docs/external-services/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme). Moving your Python code takes just a few lines: see the **Migration examples** below. Full comparison and disclaimer are in the comparison section below.

<p align="center">
  <a href="https://capmonster.cloud/en/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme">
    <img src="https://img.shields.io/badge/CapMonster%20Cloud-Python%20Captcha%20Solver-00B2FF?style=for-the-badge&logo=python&logoColor=white" alt="CapMonster Cloud Python SDK" height="40">
  </a>
</p>

<p align="center">
  <strong>Fast, AI-driven CAPTCHA solving client for Python. Seamlessly bypass Cloudflare Turnstile, reCAPTCHA v2/v3/Enterprise, DataDome, GeeTest, and Amazon WAF in web scraping and browser automation.</strong>
</p>

<p align="center">
  <a href="https://pypi.org/project/capmonstercloudclient/"><img src="https://img.shields.io/pypi/v/capmonstercloudclient.svg?style=flat-square&color=blue" alt="PyPI version"></a>
  <a href="https://pepy.tech/project/capmonstercloudclient"><img src="https://static.pepy.tech/badge/capmonstercloudclient/month" alt="PyPI downloads"></a>
  <a href="https://pypi.org/project/capmonstercloudclient/"><img src="https://img.shields.io/pypi/pyversions/capmonstercloudclient.svg?style=flat-square" alt="Python Versions"></a>
  <a href="https://github.com/CapMonsterCloud/capmonster-python-captcha-solver/stargazers"><img src="https://img.shields.io/github/stars/CapMonsterCloud/capmonster-python-captcha-solver?style=flat-square&color=yellow" alt="GitHub Stars"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-orange.svg?style=flat-square" alt="License: MIT"></a>
</p>

---

Official asynchronous Python SDK for [CapMonster Cloud](https://capmonster.cloud/en/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme). Easily plug ultra-fast AI captcha recognition into **Playwright, Selenium, Puppeteer, Scrapy, BeautifulSoup, and Requests** automation workflows without human-in-the-loop delays.

The CapMonster Cloud Python SDK (`capmonstercloudclient`, also known as the CapMonster SDK for Python) is a captcha solver and captcha bypass client for Python 3.6+. Use it to bypass reCAPTCHA v2, v3 and Enterprise, solve Cloudflare Turnstile, DataDome, GeeTest and Amazon WAF, and recognize image-to-text captchas in web scraping and automation, as a cost-effective 2captcha alternative and capsolver alternative.

**[👉 Get your Free API Key & Free Trial Balance on CapMonster Cloud](https://dash.capmonster.cloud/Account/SignUp?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme)**

---

## ⚡ Highlights & Benchmarks

- ⚡ **Fast Solving:** Automated AI models solve captchas in 300 ms to 6 seconds depending on the system load.
- 🤖 **Zero Human Workers:** 100% automated machine learning pipeline with no manual latencies.
- 🌐 **Browser Automation Ready:** Works out-of-the-box with **Playwright, Selenium, and Puppeteer**.
- 🛡️ **Modern Anti-Bot Bypass:** Full support for Cloudflare Turnstile, reCAPTCHA Enterprise, GeeTest, and Amazon WAF.
- 💰 **Cost-Effective:** Low-cost pricing structure based on pay-as-you-go balance.
- 📉 **Cheaper Than Alternatives:** reCAPTCHA v3 from $0.90 per 1,000 solves, versus $1.45 at 2Captcha and $1.00 at Capsolver.
- 🔄 **Easy Migration:** replace your 2Captcha or Capsolver solver call and keep the rest of your scraper or bot unchanged.

---

## 📊 CapMonster Cloud vs 2Captcha vs Capsolver

Looking for a 2captcha alternative or a capsolver alternative for web scraping and automation? Compare price, speed and success rate.

### reCAPTCHA v3

| Parameter | CapMonster Cloud | 2Captcha | CapSolver | DeathByCaptcha |
| :--- | :---: | :---: | :---: | :---: |
| Price per 1,000 solves (from) | **$0.90** | $1.45 | $1.00 | $2.89 |
| API response time | **≤ 2 s** | ≤ 2 s | < 3 s | ≤ 3 s |
| Solving success rate | **up to 99%** | ~77–92% | ~95–98% | ~64–90% |

*Disclaimer: 2Captcha, CapSolver, and DeathByCaptcha are trademarks of their respective owners. CapMonster Cloud is not affiliated with these entities. Performance metrics and pricing comparisons are based on publicly available data and internal benchmarking conducted on 27.09.2026.*

### Cloudflare Turnstile

| Parameter | CapMonster Cloud | 2Captcha | Anti-Captcha | DeathByCaptcha |
| :--- | :---: | :---: | :---: | :---: |
| Price per 1,000 solves (from) | **$1.30** | $1.45 | $2.00 | $2.89 |
| Time to solve | **6.24 s\*** | 16.9 s | 20.33 s | ~13 s |
| Solving success rate | **99%\*** | 96% | 96% | 96% |

*Disclaimer: 2Captcha, Anti-Captcha, and DeathByCaptcha are trademarks of their respective owners. CapMonster Cloud is not affiliated with these entities. Performance metrics and pricing comparisons are based on publicly available data and internal benchmarking as of 12.10.2026.*

**What this means in practice:**

- **reCAPTCHA v3:** $0.90 versus $1.45 at 2Captcha is up to 38% cheaper, and $0.90 versus $1.00 at Capsolver is 10% cheaper.
- **Cloudflare Turnstile:** $1.30 versus $1.45 at 2Captcha is 10% cheaper, and a solving time of 6.24 s versus 16.9 s is more than 60% faster.

---

## 📦 Installation

```bash
pip install capmonstercloudclient
```

---

## 🚀 Quick Start & Usage Examples

### 1. Asynchronous reCAPTCHA v2 Solving

```python
import asyncio
from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import RecaptchaV2Request

# Initialize client with your API key from dashboard
options = ClientOptions(api_key="YOUR_CAPMONSTER_API_KEY")
client = CapMonsterClient(options=options)

async def main():
    # Build the task payload
    request = RecaptchaV2Request(
        websiteUrl="[https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=high](https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=high)",
        websiteKey="6Lcg7CMUAAAAANphynKgn9YAgA4tQ2KI_iqRyTwd"
    )
    
    # Send task and receive token
    result = await client.solve_captcha(request)
    print("reCAPTCHA Token:", result.get("gRecaptchaResponse"))

if __name__ == "__main__":
    asyncio.run(main())
```

### 2. Browser Automation (Playwright + Cloudflare Turnstile)

```python
import asyncio
from playwright.async_api import async_playwright
from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import TurnstileRequest

options = ClientOptions(api_key="YOUR_CAPMONSTER_API_KEY")
client = CapMonsterClient(options=options)

async def run_scraper():
    # Solve Turnstile challenge via CapMonster Cloud
    turnstile_req = TurnstileRequest(
        websiteURL="[https://target-website.com/login](https://target-website.com/login)",
        websiteKey="0x4AAAAAAABnPIDnK2k_e-2"
    )
    solution = await client.solve_captcha(turnstile_req)
    token = solution.get("token")

    # Inject token into Playwright browser session
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("[https://target-website.com/login](https://target-website.com/login)")
        
        await page.evaluate(f'document.querySelector("[name=cf-turnstile-response]").value = "{token}";')
        await page.click("#submit-button")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_scraper())
```

---

## 🔄 Migrating from 2Captcha or Capsolver

Already use 2Captcha or Capsolver in your scraper or bot? Replace only the solver call and keep the rest of your parser unchanged. CapMonster Cloud follows the same flow: send the website URL and sitekey, receive the token.

### Migration from 2Captcha (2captcha-python)

```python
# Before: 2Captcha
from twocaptcha import TwoCaptcha

solver = TwoCaptcha("YOUR_2CAPTCHA_API_KEY")
result = solver.recaptcha(
    sitekey="YOUR_SITE_KEY",
    url="[https://target-website.com/page-with-recaptcha](https://target-website.com/page-with-recaptcha)",
)
token = result["code"]
```

```python
# After: CapMonster Cloud
import asyncio
from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import RecaptchaV2Request

client = CapMonsterClient(options=ClientOptions(api_key="YOUR_CAPMONSTER_API_KEY"))

async def solve():
    result = await client.solve_captcha(RecaptchaV2Request(
        websiteUrl="[https://target-website.com/page-with-recaptcha](https://target-website.com/page-with-recaptcha)",
        websiteKey="YOUR_SITE_KEY",
    ))
    return result.get("gRecaptchaResponse")

token = asyncio.run(solve())
```

### Migration from Capsolver (capsolver-python)

```python
# Before: Capsolver
import capsolver

capsolver.api_key = "YOUR_CAPSOLVER_API_KEY"
solution = capsolver.solve({
    "type": "ReCaptchaV2TaskProxyLess",
    "websiteURL": "[https://target-website.com/page-with-recaptcha](https://target-website.com/page-with-recaptcha)",
    "websiteKey": "YOUR_SITE_KEY",
})
token = solution["gRecaptchaResponse"]
```

The "After" code is the same CapMonster Cloud snippet as above: only the client, the API key and the request class change, the rest of your scraper stays the same. If you use an async framework, call `await client.solve_captcha(...)` directly instead of `asyncio.run`.

### Keep existing 2Captcha-based software

Software that already speaks the 2Captcha API can work with CapMonster Cloud without code changes. See the [guide for connecting other services' APIs](https://docs.capmonster.cloud/docs/external-services/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme).

---

## 🛡️ Supported CAPTCHA Types: reCAPTCHA, Cloudflare Turnstile, DataDome, GeeTest & More

Use this Python captcha solver for captcha bypass in web scraping and automation: reCAPTCHA bypass (v2, v3, Enterprise), Cloudflare Turnstile solver, DataDome solver, GeeTest solver, Amazon WAF bypass and image-to-text recognition.

All task types conform to the official [CapMonster Cloud API Documentation](https://docs.capmonster.cloud/docs/captchas/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme):

| Protection Type | Task Request Class | Proxyless Mode |
| :--- | :--- | :---: |
| **Cloudflare Turnstile** | `TurnstileRequest` | ✅ Supported |
| **reCAPTCHA v2** | `RecaptchaV2Request` | ✅ Supported |
| **reCAPTCHA v3** | `RecaptchaV3ProxylessRequest` | ✅ Supported |
| **reCAPTCHA Enterprise** | `RecaptchaV2EnterpriseProxylessRequest` / `RecaptchaV2EnterpriseRequest` | ✅ Supported |
| **GeeTest (v3, v4)** | `GeeTestProxylessRequest` / `GeeTestRequest` | ✅ Supported |
| **Amazon WAF** | `AmazonWafRequest` | ✅ Supported |
| **DataDome** | `DataDomeCustomTaskRequest` | 🌐 Proxy Required |
| **Imperva / Incapsula** | `ImpervaCustomTaskRequest` / `ImpervaCustomTaskProxylessRequest` | ✅ Supported |
| **Binance CAPTCHA** | `BinanceTaskRequest` / `BinanceTaskProxylessRequest` | ✅ Supported |
| **Standard Text CAPTCHA** | `ImageToTextRequest` | ✅ Supported |
| **Complex Image Tasks** | `RecaptchaComplexImageTaskRequest` | ✅ Supported |

---

## 🛠️ How It Works

```text
[ Script / Scraper ]
         │
         ▼
[ Extract sitekey & website URL ]
         │
         ▼
[ CapMonsterClient API ] ──► POST createTask to [https://api.capmonster.cloud](https://api.capmonster.cloud)
         │
         ▼
[ Neural Network Processing ] ──► Poll getTaskResult (300ms - 6s)
         │
         ▼
[ Receive Token & Autosubmit ] ──► Complete bypass
```

---

## ⚙️ Best Practices

- **Token Expiration:** Most tokens (reCAPTCHA, Turnstile) remain valid for 120 seconds. Inject and submit the solution immediately after receiving the response.
- **Proxy Usage:** For custom tasks and strict protections, use the same proxy in your scraping session and the CapMonster task payload.
- **Balance Monitoring:** Ensure your account balance remains positive in the [Dashboard](https://dash.capmonster.cloud/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme).

---

## ❓ FAQ

**Is CapMonster Cloud a 2Captcha alternative?**
Yes. It is a captcha solving service with an official Python SDK. For reCAPTCHA v3 it starts at $0.90 per 1,000 solves versus $1.45 at 2Captcha, which is up to 38% cheaper. For Cloudflare Turnstile it starts at $1.30 versus $1.45, which is 10% cheaper.

**Is CapMonster Cloud a Capsolver alternative?**
Yes. For reCAPTCHA v3 it is 10% cheaper than Capsolver ($0.90 versus $1.00 per 1,000 solves) and shows an API response time of ≤ 2 s versus < 3 s. See the comparison table above and its disclaimer.

**How do I migrate from 2Captcha or Capsolver to CapMonster Cloud in Python?**
Install `capmonstercloudclient`, create a `CapMonsterClient` with your API key and replace your solver call with `client.solve_captcha(...)`. See the migration examples above. Software that already supports the 2Captcha API can also be connected through the [CapMonster Cloud guide](https://docs.capmonster.cloud/docs/external-services/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme).

**Which captchas can the Python SDK bypass?**
reCAPTCHA v2, v3 and Enterprise, Cloudflare Turnstile, GeeTest, Amazon WAF, DataDome, Imperva / Incapsula, Binance CAPTCHA, standard text (image-to-text) captchas and reCAPTCHA image tasks. See the supported types table.

**Which Python versions are supported?**
The package on PyPI requires Python 3.6 or newer.

**How do I get an API key?**
Register on CapMonster Cloud, top up your balance and copy your API key. The [Getting Started Guide](https://docs.capmonster.cloud/docs/getting-start/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme) describes each step.

---

## 📚 Official Documentation & Links

- 📖 [Getting Started Guide](https://docs.capmonster.cloud/docs/getting-start/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme)
- 🎯 [Supported Captchas Overview](https://docs.capmonster.cloud/docs/captchas/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme)
- ⚙️ [API Methods Reference](https://docs.capmonster.cloud/docs/methods/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme)
- 💬 [Support & Community](https://capmonster.cloud/en/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme#support)

## Other official SDKs

- [.NET](https://github.com/CapMonsterCloud/capmonster-dotnet-captcha-solver)
- [Node.js](https://github.com/CapMonsterCloud/capmonster-nodejs-captcha-solver)
- [n8n](https://github.com/CapMonsterCloud/capmonster-n8n-captcha-solver)
- [API Docs](https://github.com/CapMonsterCloud/capmonster-captcha-solver-docs)

---

## 📄 License

[MIT](./LICENSE) © [CapMonster Cloud](https://capmonster.cloud/en/?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme)
