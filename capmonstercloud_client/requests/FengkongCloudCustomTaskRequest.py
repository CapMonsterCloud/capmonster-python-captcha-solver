from typing import Dict, Optional, Union
from pydantic import Field, field_validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class FengkongCloudCustomTaskRequest(CustomTaskRequestBase):
    """
    Represents a payload structure for solving FengkongCloud captcha
    challenges via a custom module.

    Attributes:
        captchaClass: The class (subtype) identifier of the custom
            module, constant "fengkongcloud" for this task.
        websiteKey: The siteKey value found on the page (the appid
            parameter of the /conf request).
        metadata: Optional dictionary; the only allowed key is apiJsUrl,
            the link to smcp.min.js.
    """

    captchaClass: str = Field(default='fengkongcloud', description='Class (subtype) identifier of the custom module, constant "fengkongcloud".')
    websiteKey: str = Field(..., description='The siteKey value found on the page.')
    metadata: Optional[Dict[str, str]] = Field(default=None, description='Optional dictionary; the only allowed key is apiJsUrl, the link to smcp.min.js.')

    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        if value is None:
            return value
        allowed = {'apiJsUrl'}
        if not set(value.keys()).issubset(allowed):
            raise TypeError(f'Allowed keys for metadata are {sorted(allowed)}.')
        return value

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['class'] = self.captchaClass
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        if self.metadata is not None:
            task['metadata'] = self.metadata
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        return task
