from typing import Dict, Union
from pydantic import Field, field_validator, model_validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class ProtonCustomTaskRequest(CustomTaskRequestBase):
    """
    Represents a payload structure for solving Proton Captcha challenges
    via a custom module.

    Attributes:
        captchaClass: The class (subtype) identifier of the custom
            module, constant "proton" for this task.
        metadata: A dictionary with the required HumanVerificationToken
            and pageAction ("login" or "signup").
        proxy: Proxy settings to route the request through. Required for
            this task type.
    """

    captchaClass: str = Field(default='proton', description='Class (subtype) identifier of the custom module, constant "proton".')
    metadata: Dict[str, str] = Field(..., description='A dictionary with the required HumanVerificationToken and pageAction ("login" or "signup").')

    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        allowed = {'HumanVerificationToken', 'pageAction'}
        if not set(value.keys()).issubset(allowed):
            raise TypeError(f'Allowed keys for metadata are {sorted(allowed)}.')
        for key in sorted(allowed):
            if value.get(key) is None:
                raise TypeError(f'{key} must be defined inside metadata.')
        if value['pageAction'] not in ('login', 'signup'):
            raise TypeError(f'pageAction must be "login" or "signup".')
        return value

    @model_validator(mode='before')
    def validate_proton_proxy(cls, values):
        proxy = values.get('proxy')
        if proxy is None:
            raise RuntimeError(f'You are required to use your own proxies.')
        return values

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['class'] = self.captchaClass
        task['websiteURL'] = self.websiteUrl
        task['metadata'] = self.metadata
        task['proxyType'] = self.proxy.proxyType
        task['proxyAddress'] = self.proxy.proxyAddress
        task['proxyPort'] = self.proxy.proxyPort
        task['proxyLogin'] = self.proxy.proxyLogin
        task['proxyPassword'] = self.proxy.proxyPassword
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        return task
