from typing import Dict, Optional, Union
from pydantic import Field

from .baseRequest import BaseRequest

class ArCaptchaRequest(BaseRequest):
    """
    Represents a payload structure for solving ARCaptcha challenges.

    Attributes:
        websiteUrl: The URL of the webpage containing the ARCaptcha challenge.
        websiteKey: The site key associated with the ARCaptcha on the webpage.
        type: The constant string value identifying the task type as
            "ArCaptchaTask".
        isInvisible: True if the captcha is invisible (has a hidden
            verification field).
        userAgent: Browser User-Agent to emulate.
    """
    websiteUrl: str = Field(..., description='Address of a webpage with ARCaptcha.')
    websiteKey: str = Field(..., description='The site key associated with the ARCaptcha on the webpage.')
    type: str = Field(default='ArCaptchaTask', description='The constant string value identifying the task type as "ArCaptchaTask".')
    isInvisible: Optional[bool] = Field(default=None, description='True if the captcha is invisible (has a hidden verification field).')
    userAgent: Optional[str] = Field(default=None, description='Browser User-Agent to emulate.')

    def getTaskDict(self) -> Dict[str, Union[str, bool]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        if self.isInvisible is not None:
            task['isInvisible'] = self.isInvisible
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        return task
