from __future__ import print_function
import sys
if sys.version_info < (3,):
    print("Python 2 not supported by CapMonsterCloudClient.")
    sys.exit(-1)

from pathlib import Path
#from pkg_resources import parse_requirements
from setuptools import setup


NAME = 'capmonstercloudclient'
DESCRIPTION = 'Official CapMonster Cloud Python SDK: captcha solver & captcha bypass for reCAPTCHA, Cloudflare Turnstile, DataDome and GeeTest. A 2captcha and capsolver alternative.'
EMAIL = 'support@capmonster.cloud'
AUTHOR = 'CapMonster Cloud'
with open('capmonstercloud_client/version.txt', 'r') as f:
    VERSION = f.read()
with open("requirements.txt") as f:
    REQUIRED = [line.strip() for line in f if line.strip() and not line.startswith("#")]
URL='https://github.com/CapMonsterCloud/capmonster-python-captcha-solver'

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author_email=EMAIL,
    author=AUTHOR,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['capmonstercloudclient', 'capmonstercloudclient.requests'],
    package_dir={"capmonstercloudclient": 'capmonstercloud_client'},
    package_data={'': ['version.txt']},
    include_package_data=True,
    py_modules=["capmonstercloudclient"],
    url=URL,
    project_urls={
        "Homepage": "https://capmonster.cloud/en/",
        "Source": "https://github.com/CapMonsterCloud/capmonster-python-captcha-solver",
        "Issues": "https://github.com/CapMonsterCloud/capmonster-python-captcha-solver/issues",
        "Documentation": "https://docs.capmonster.cloud/",
    },
    python_requires='>=3.6',
    install_requires=REQUIRED,
    keywords="""
                capmonster
                capmonster-cloud
                capmonstercloudclient
                captcha
                captcha-solver
                captcha-bypass
                recaptcha
                cloudflare-turnstile
                geetest
                datadome
                web-scraping
                python3
                2captcha-alternative
                capsolver-alternative
               """,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Development Status :: 5 - Production/Stable",
        "Framework :: AsyncIO",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
    ]
)
