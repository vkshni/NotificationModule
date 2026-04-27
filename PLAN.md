# Week 12 — Notification Module
> **Channels:** Email · SMS · Push  
> **Time:** 1 hour/day · 4 tasks/day

---

## Day 1 — System Design, Architecture & Git Setup

| # | Task | Type |
|---|------|------|
| 1 | Draw notification system architecture — providers, queue, dispatcher, retry flow | `design` |
| 2 | Define DB schema: `notifications`, `delivery_log`, `user_preferences`, `templates` | `design` |
| 3 | Init Git repo, create folder structure: `/email` `/sms` `/push` `/core` `/config` `/tests` | `infra` |
| 4 | Write ADR (Architecture Decision Record) doc — why queue-based, chosen providers | `doc` |

---

## Day 2 — Core Abstractions & Provider Interfaces

| # | Task | Type |
|---|------|------|
| 1 | Create base `NotificationProvider` interface / abstract class with `send()`, `validate()`, `status()` | `code` |
| 2 | Build `NotificationPayload` model — channel, recipient, template_id, variables, priority | `code` |
| 3 | Write `DeliveryResult` model — status, provider_response, timestamp, error_code | `code` |
| 4 | Add config loader for provider credentials (env-based), write unit tests for models | `test` |

---

## Day 3 — Email Provider Integration

| # | Task | Type |
|---|------|------|
| 1 | Integrate email provider (Resend / SendGrid / SES) — implement `EmailProvider` class | `code` |
| 2 | Build HTML email template engine with variable interpolation and layout support | `code` |
| 3 | Handle bounces, spam complaints via webhooks — update `delivery_log` on events | `code` |
| 4 | Write email tests: send success, failed delivery, missing template variable | `test` |

---

## Day 4 — SMS Provider Integration

| # | Task | Type |
|---|------|------|
| 1 | Integrate SMS provider (Twilio / AWS SNS) — implement `SmsProvider` class | `code` |
| 2 | Add phone number validation, E.164 formatting, opt-out / STOP keyword handling | `code` |
| 3 | Handle delivery receipts via webhook — map provider status codes to internal enums | `code` |
| 4 | Write SMS tests: valid send, invalid number, opt-out block, rate limit mock | `test` |

---

## Day 5 — Push Notification Integration

| # | Task | Type |
|---|------|------|
| 1 | Integrate FCM (Firebase) for Android/web push — implement `PushProvider` class | `code` |
| 2 | Add APNs support for iOS — handle token registration and device token storage | `code` |
| 3 | Build topic/segment targeting — send to `user_id`, segment, or broadcast topic | `code` |
| 4 | Write push tests: single device, topic send, expired token cleanup, silent push | `test` |

---

## Day 6 — Dispatcher, Queue & Retry Logic

| # | Task | Type |
|---|------|------|
| 1 | Build `NotificationDispatcher` — routes payload to correct provider by channel | `code` |
| 2 | Add queue integration (Bull / BullMQ / SQS) — async dispatch with priority levels | `code` |
| 3 | Implement retry logic — exponential backoff, max attempts, dead-letter queue | `code` |
| 4 | Write integration test: end-to-end dispatch → queue → provider → `delivery_log` | `test` |

---

## Day 7 — User Preferences, API & Week Review

| # | Task | Type |
|---|------|------|
| 1 | Build user preferences module — per-channel opt-in/out, quiet hours, frequency caps | `code` |
| 2 | Expose REST endpoints: `POST /notify`, `GET /status/:id`, `PATCH /preferences` | `code` |
| 3 | Write README for the module — setup, env vars, provider config, API usage | `doc` |
| 4 | Week review: run full test suite, fix gaps, tag release `v0.12.0` | `infra` |

---

## Task Type Legend

| Tag | Meaning |
|-----|---------|
| `design` | Architecture, schema, diagrams |
| `code` | Implementation |
| `test` | Unit / integration tests |
| `infra` | Git, config, CI, releases |
| `doc` | README, ADR, comments |

---

> **Next up → Week 13:** _(your next module here)_