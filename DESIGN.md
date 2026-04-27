# Notification Module — Design

# Directory Structure
```bash
NotificationModule/
  --providers/
    --email.py
    --sms.py
    --push.py
  --dispatcher.py
  --models.py
  --templates/
  --utils.py
  --PLAN.md
  --DESIGN.md
  --README.md
```

## Flow
```bash
Your App
   ↓
notify(channel, user, template, data)
   ↓
Dispatcher → picks Email / SMS / Push
   ↓
Provider sends it
   ↓ (fail?)
Retry → Retry → Retry
   ↓ (still fail?)
log.error("failed after 3 attempts")
   ↓ (success?)
log.info("notification sent")
```

## Decisions
- Logging: Python logging module (success + failure)
- On failure: retry 3 times, then log.error and move on

## Providers
- Email → Resend
- SMS → Twilio  
- Push → Firebase

## DB Schema
`notifications` — notification_id, user_id, recipient, channel, template, status, created_at   
`delivery_log` — delivery_id, notification_id, status, error_msg, sent_at

## Skipped (intentionally)
- Celery / Redis queue
- Webhooks
- Delivery status tracking beyond logs