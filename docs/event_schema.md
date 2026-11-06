# Common event schema (draft)

| Field | Type | Suggested size | Required | Description |
|---|---|---:|---|---|
| timestamp | ISO-8601 text | 35 chars | Yes | Event time including timezone where available |
| source | string | 30 chars | Yes | linux, windows or apache |
| event_type | string | 50 chars | Yes | authentication, web_request, etc. |
| username | string | 128 chars | No | Account name |
| source_ip | string | 45 chars | No | IPv4 or IPv6 address |
| status | string | 20 chars | No | success, failed, blocked, etc. |
| severity | string | 10 chars | No | low, medium, high, critical |
| raw_event | text | variable | No | Original source record |

SQLite uses TEXT for flexible source values. Validate lengths and formats in the ingestion layer before inserting records.
