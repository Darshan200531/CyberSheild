# Initial detection rule catalogue (design only)

| Rule ID | Rule | Initial condition | Suggested severity |
|---|---|---|---|
| CS-001 | SSH repeated failures | 5 failed attempts from one IP within 120 seconds | High |
| CS-002 | Successful login after failures | Successful login follows repeated failures from same IP/account | Medium |
| CS-003 | HTTP forbidden responses | Repeated HTTP 403 responses from one IP | Medium |
| CS-004 | HTTP not found probing | Repeated HTTP 404 responses from one IP | Low |
| CS-005 | Server errors | Unusual increase in HTTP 5xx responses | Medium |

These are proposed starter rules, not active detections in the Week 4 application. Thresholds should be tested and tuned against sample data.
