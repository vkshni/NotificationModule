# Email provider

import resend

# Set your API key
resend.api_key = "re_123456789"


class EmailProvider:

    def __init__(self):
        pass

    def send(self, notification):

        params = notification.model_dump()

        # Resend email
        email = resend.Emails.send()


params = {
    "from": "onboarding@resend.dev",
    "to": ["delivered@resend.dev"],
    "subject": "Hello World",
    "html": "<strong>It works!</strong>",
}

email = resend.Emails.send(params)
print(email)
