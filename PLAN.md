# Week 12 — Notification Module
> **Stack:** Python · Resend · Twilio · Firebase  
> **Time:** 1 hour/day · 4 tasks/day

---

## Day 1 — Design, Architecture & Git ✅

| # | Task | Type | Status |
|---|------|------|--------|
| 1 | Architecture flow diagram + key decisions noted | `design` | ✅ |
| 2 | DB schema — `notifications` + `delivery_log` tables | `design` | ✅ |
| 3 | Git repo + folder scaffold committed | `infra` | ✅ |
| 4 | `DESIGN.md` with flow, providers, schema, skipped items | `doc` | ✅ |

---

## Day 2 — models.py (Pydantic)  ✅ 

| # | Task | Type | Status |
|---|------|------|--------|
| 1 | `NotificationPayload` model — channel, recipient, template, variables | `code` | ✅ |   
| 2 | `DeliveryResult` model — status, error_msg, sent_at | `code` | ✅ | 
| 3 | `Channel` enum — EMAIL, SMS, PUSH | `code` | ✅ | 
| 4 | Unit tests for model validation in `tests/` | `test` | ✅ | 

---

## Day 3 — Email Provider (Resend)

| # | Task | Type |
|---|------|------|
| 1 | `EmailProvider` class wrapping Resend SDK — `send()` | `code` |
| 2 | Jinja2 template rendering for email body | `code` |
| 3 | 3-attempt retry loop with logging on each fail | `code` |
| 4 | Test: successful send, failed send, bad template variable | `test` |

---

## Day 4 — SMS Provider (Twilio)

| # | Task | Type |
|---|------|------|
| 1 | `SmsProvider` class wrapping Twilio SDK — `send()` | `code` |
| 2 | Phone number validation + E.164 format using `phonenumbers` lib | `code` |
| 3 | 3-attempt retry loop with logging | `code` |
| 4 | Test: valid send, invalid number, retry on fail | `test` |

---

## Day 5 — Push Provider (Firebase)

| # | Task | Type |
|---|------|------|
| 1 | `PushProvider` class wrapping `firebase-admin` SDK — `send()` | `code` |
| 2 | Accept device token + title + body as payload | `code` |
| 3 | 3-attempt retry loop with logging | `code` |
| 4 | Test: valid token send, expired token, retry on fail | `test` |

---

## Day 6 — Dispatcher + Utils

| # | Task | Type |
|---|------|------|
| 1 | `dispatcher.py` — routes payload to correct provider by channel | `code` |
| 2 | `utils.py` — shared logging setup, retry decorator | `code` |
| 3 | Wire all 3 providers through dispatcher end-to-end | `code` |
| 4 | Integration test: one call hits all 3 channels correctly | `test` |

---

## Day 7 — Cleanup, README & Final Test

| # | Task | Type |
|---|------|------|
| 1 | Write `README.md` — what it does, providers, setup, env vars | `doc` |
| 2 | Clean up `DESIGN.md` — finalize decisions and skipped items | `doc` |
| 3 | Run full test suite, fix any gaps | `test` |
| 4 | Final commit + tag `v0.12.0` | `infra` |

---

## Task Type Legend

| Tag | Meaning |
|-----|---------|
| `design` | Architecture, schema, diagrams |
| `code` | Implementation |
| `test` | Unit / integration tests |
| `infra` | Git, config, releases |
| `doc` | README, DESIGN.md, comments |
