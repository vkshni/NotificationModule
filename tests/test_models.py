import pytest
from pydantic import ValidationError
from models import Channel, NotificationPayload, DeliveryResult


# ── Channel ──────────────────────────────────────────────


def test_channel_values():
    assert Channel.EMAIL.value == "email"
    assert Channel.SMS.value == "sms"
    assert Channel.PUSH.value == "push"


# ── NotificationPayload ──────────────────────────────────


def test_payload_valid():
    payload = NotificationPayload(
        channel=Channel.EMAIL,
        recipient="test@example.com",
        template="Welcome to the app, enjoy your stay!",
        data={"name": "Raj"},
    )
    assert payload.channel == Channel.EMAIL
    assert payload.recipient == "test@example.com"
    assert payload.data == {"name": "Raj"}


def test_payload_data_defaults_to_empty_dict():
    payload = NotificationPayload(
        channel=Channel.SMS,
        recipient="+919876543210",
        template="Your OTP is ready to use now",
    )
    assert payload.data == {}


def test_payload_created_at_auto_set():
    payload = NotificationPayload(
        channel=Channel.PUSH,
        recipient="device-token-abc123",
        template="You have a new message waiting for you",
    )
    assert payload.created_at is not None


def test_payload_empty_recipient_fails():
    with pytest.raises(ValidationError):
        NotificationPayload(
            channel=Channel.EMAIL,
            recipient="",
            template="Welcome to the app, enjoy your stay!",
        )


def test_payload_invalid_channel_fails():
    with pytest.raises(ValidationError):
        NotificationPayload(
            channel="WHATSAPP",
            recipient="test@example.com",
            template="Welcome to the app, enjoy your stay!",
        )


def test_payload_template_too_short_fails():
    with pytest.raises(ValidationError):
        NotificationPayload(
            channel=Channel.EMAIL,
            recipient="test@example.com",
            template="Hi",
        )


# ── DeliveryResult ───────────────────────────────────────


def test_delivery_result_success():
    result = DeliveryResult(success=True, status="delivered")
    assert result.success is True
    assert result.error_msg is None


def test_delivery_result_failure():
    result = DeliveryResult(
        success=False, status="failed", error_msg="Recipient address not found"
    )
    assert result.success is False
    assert result.error_msg == "Recipient address not found"


def test_delivery_result_sent_at_auto_set():
    result = DeliveryResult(success=True, status="delivered")
    assert result.sent_at is not None


def test_delivery_result_missing_success_fails():
    with pytest.raises(ValidationError):
        DeliveryResult(status="delivered")
