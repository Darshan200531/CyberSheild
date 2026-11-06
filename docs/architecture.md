# Architecture – initial design

```text
Linux auth logs ─┐
Windows events ──┼─> Upload / collection -> Validation -> Parsing
Apache logs ─────┘                              |
                                                v
                                      Common event normalization
                                                |
                                                v
                                          SQLite events
                                                |
                                                v
                                      Rule detection / scoring
                                                |
                                                v
                                         SQLite alerts
                                                |
                                                v
                                          Flask dashboard
```

Week 4 implements the Flask application foundation, database initialization, health endpoint and static dashboard. Ingestion, parsing and detection are planned for later weeks.
