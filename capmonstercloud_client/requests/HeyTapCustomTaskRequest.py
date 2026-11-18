from typing import Dict, Optional, Union
from pydantic import Field, field_validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class HeyTapCustomTaskRequest(CustomTaskRequestBase):
    """
    Represents a payload structure for solving HeyTap captcha challenges
    via a custom module.

    Attributes:
        captchaClass: The class (subtype) identifier of the custom
            module, constant "heytap" for this task.
        websiteKey: The siteKey value found on the page (the ak
            parameter of the HeyTap captcha API request).
        metadata: Optional dictionary; the only allowed key is apiServer,
            the HeyTap API server domain without the https:// prefix
            (needed only if it differs from the default server).
    """

    captchaClass: str = Field(default='heytap', description='Class (subtype) identifier of the custom module, constant "heytap".')
    websiteKey: str = Field(..., description='The siteKey value found on the page.')
    metadata: Optional[Dict[str, str]] = Field(default=None, description='Optional dictionary; the only allowed key is apiServer, the HeyTap API server domain without the https:// prefix.')

    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        if value is None:
            return value
        allowed = {'apiServer'}
        if not set(value.keys()).issubset(allowed):
            raise TypeError(f'Allowed keys for metadata are {sorted(allowed)}.')
        api_server = value.get('apiServer')
        if api_server is not None and api_server.startswith(('https://', 'http://')):
            raise TypeError(f'apiServer must be a domain without the https:// prefix.')
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
