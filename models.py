from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Channel(Enum):

    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"


class NotificationPayload(BaseModel):

    channel: Channel
    recipient: str = Field(min_length=1)
    data: dict = Field(default_factory=dict)
    template: str = Field(min_length=10)
    created_at: datetime = Field(default_factory=datetime.now)


class DeliveryResult(BaseModel):

    success: bool
    status: str
    error_msg: Optional[str] = None
    sent_at: datetime = Field(default_factory=datetime.now)


if __name__ == "__main__":

    print(Channel.EMAIL.value)
    notification = NotificationPayload(
        channel="email",
        recipient="user@example.com",
        template="Welcome to our service!",  # Must be >= 10 chars
    )

    print(notification.model_dump())  # Converts to a dictionary
