
PRAGMA foreign_keys = ON;

-- 1. Normalized security events
CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    source_type TEXT NOT NULL,
    source_ip TEXT,
    username TEXT,
    event_type TEXT NOT NULL,
    action TEXT,
    status TEXT,
    endpoint TEXT,
    http_method TEXT,
    http_status INTEGER,
    message TEXT,
    raw_log TEXT,
    created_at TEXT NOT NULL DEFAULT
        (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);

-- 2. Detection rules
CREATE TABLE IF NOT EXISTS detection_rules (
    rule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    rule_name TEXT NOT NULL UNIQUE,
    description TEXT,
    rule_type TEXT NOT NULL,
    threshold INTEGER,
    time_window_sec INTEGER,
    severity TEXT NOT NULL
        CHECK (severity IN ('Low', 'Medium', 'High', 'Critical')),
    enabled INTEGER NOT NULL DEFAULT 1
        CHECK (enabled IN (0, 1)),
    created_at TEXT NOT NULL DEFAULT
        (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);

-- 3. Security alerts
CREATE TABLE IF NOT EXISTS alerts (
    alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
    rule_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    severity TEXT NOT NULL
        CHECK (severity IN ('Low', 'Medium', 'High', 'Critical')),
    source_ip TEXT,
    username TEXT,
    event_count INTEGER NOT NULL DEFAULT 1,
    evidence TEXT,
    status TEXT NOT NULL DEFAULT 'New'
        CHECK (status IN (
            'New', 'Investigating', 'Resolved', 'False Positive'
        )),
    fingerprint TEXT UNIQUE,
    first_seen TEXT NOT NULL,
    last_seen TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT
        (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    FOREIGN KEY (rule_id)
        REFERENCES detection_rules(rule_id)
);

-- 4. Link alerts to their supporting events
CREATE TABLE IF NOT EXISTS alert_events (
    alert_event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    alert_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    FOREIGN KEY (alert_id)
        REFERENCES alerts(alert_id) ON DELETE CASCADE,
    FOREIGN KEY (event_id)
        REFERENCES events(event_id) ON DELETE CASCADE,
    UNIQUE (alert_id, event_id)
);

-- 5. Audit trail for alert investigations
CREATE TABLE IF NOT EXISTS audit_logs (
    audit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    alert_id INTEGER NOT NULL,
    action TEXT NOT NULL,
    details TEXT,
    actor TEXT DEFAULT 'system',
    created_at TEXT NOT NULL DEFAULT
        (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    FOREIGN KEY (alert_id)
        REFERENCES alerts(alert_id) ON DELETE CASCADE
);

-- Indexes for efficient searching and detection
CREATE INDEX IF NOT EXISTS idx_events_timestamp
    ON events(timestamp);

CREATE INDEX IF NOT EXISTS idx_events_source_ip
    ON events(source_ip);

CREATE INDEX IF NOT EXISTS idx_events_type_timestamp
    ON events(event_type, timestamp);

CREATE INDEX IF NOT EXISTS idx_events_username
    ON events(username);

CREATE INDEX IF NOT EXISTS idx_alerts_severity
    ON alerts(severity);

CREATE INDEX IF NOT EXISTS idx_alerts_status
    ON alerts(status);

CREATE INDEX IF NOT EXISTS idx_alerts_created_at
    ON alerts(created_at);

CREATE INDEX IF NOT EXISTS idx_alert_events_event
    ON alert_events(event_id);

CREATE INDEX IF NOT EXISTS idx_audit_logs_alert
    ON audit_logs(alert_id);
