# 🛡️ CyberShield Mini SIEM Threat Detection Portal

## 📌 Project Overview

CyberShield Mini SIEM is a lightweight Security Information and Event Management (SIEM) portal designed to analyze system and web logs, detect suspicious activities using predefined security rules, and generate alerts for potential threats.

The project aims to provide a centralized dashboard for monitoring security events, investigating alerts, and understanding potential threats using sample or synthetic log data.

**Technology Stack:** Python, Flask, SQLite, HTML, CSS, JavaScript, and Git.

---

## 📅 Development Progress

### ✅ Week 1: Project Kick-off and Foundation

**Objective:** Establish the project scope, development environment, and workflow.

**Activities Completed:**
- Defined the scope and objectives of the CyberShield Mini SIEM project.
- Identified the tools and technologies required for development.
- Reviewed ethical guidelines and restrictions for security testing.
- Established a Git/GitHub workflow for version control.
- Refreshed Python fundamentals required for backend development.
- Identified the project requirements and initial development tasks.

**Deliverables:**
- Project scope and objectives.
- Initial development plan.
- Development environment and tool checklist.
- GitHub repository setup.

---

### ✅ Week 2: SIEM and Log Fundamentals

**Objective:** Understand SIEM concepts, security events, and log analysis fundamentals.

**Activities Completed:**
- Studied the fundamentals of Security Information and Event Management (SIEM).
- Learned the differences between events, alerts, and incidents.
- Studied alert severity levels: Low, Medium, High, and Critical.
- Explored false positives and their impact on threat detection.
- Examined sample log formats and identified important security fields.
- Studied common suspicious activities, including repeated failed logins and brute-force attempts.
- Identified the log fields required for security event analysis.

**Deliverables:**
- SIEM terminology and fundamentals.
- Sample log datasets.
- Initial log field mapping.
- Identification of potential security detection scenarios.

---

### ✅ Week 3: Solution Design

**Objective:** Design the architecture, data model, user interface, and initial detection rules.

**Activities Completed:**
- Designed the overall architecture of the CyberShield Mini SIEM portal.
- Planned the workflow for log ingestion, parsing, detection, alert generation, and dashboard visualization.
- Designed the initial event schema for storing normalized security events.
- Planned the SQLite database structure for storing events and alerts.
- Prepared the initial user interface layout for the dashboard.
- Created an initial detection rule catalogue with severity levels and expected evidence.
- Defined the main security scenarios to be detected by the system.

**Initial Detection Rules:**

| Detection Rule         | Example Condition                                                              | Severity |
|------------------------|---------------------------------------------------------------------------------|------------|
| Brute-force Login      | At least 5 failed logins from one IP against one or more users within 2 minutes | High |
| Account Enumeration    | One IP attempts at least 5 distinct usernames within 5 minutes                  | High |
| Blacklisted IP Match   | Source IP matches an entry in a local approved watchlist                        | Critical |
| Excessive Web Requests | More than 100 requests from one IP within 1 minute                              | Medium |
| Repeated Server Errors | At least 10 HTTP 5xx responses from one IP within 5 minutes                     | Medium |
| After-hours Successful Login | Successful login outside configured business hours                        | Low/Medium |


**How system works**

        Sample Log Files
               │
               ▼
      ┌──────────────────┐
      │  Log Ingestion   │
      │  CSV / JSON      │
      └──────────────────┘
               │
               ▼
      ┌──────────────────┐
      │  Input Validation│
      │  & File Checks   │
      └──────────────────┘
               │
               ▼
      ┌──────────────────┐
      │  Log Parsing &   │
      │  Normalization   │
      └──────────────────┘
               │
               ▼
      ┌──────────────────┐
      │ Detection Engine │
      │ Security Rules   │
      └──────────────────┘
               │
               ▼
      ┌──────────────────┐
      │ Risk Scoring &   │
      │ Deduplication    │
      └──────────────────┘
               │
               ▼
      ┌──────────────────┐
      │ SQLite Database  │
      │ Events & Alerts  │
      └──────────────────┘
               │
               ▼
      ┌──────────────────┐
      │ Flask Dashboard  │
      │ Alerts & Charts  │
      └──────────────────┘ 
      
**Deliverables:**
- Initial system architecture.
- Event schema and database design.
- Dashboard wireframe.
- Initial detection rule catalogue.
- Development backlog and demonstration plan.

---

## 📊 Three-Week Progress Summary

| Week | Focus Area | Status |
|---|---|---|
| Week 1 | Project Foundation | ✅ Completed |
| Week 2 | SIEM and Log Fundamentals | ✅ Completed |
| Week 3 | Solution Design | ✅ Completed |

### Current Project Status

The initial planning and design phases have been completed. The project has a defined scope, an initial detection rule catalogue, and a planned architecture for processing security logs and generating alerts.

The next phase focuses on developing the application skeleton using Flask, configuring SQLite, implementing logging and health-check functionality, and creating the initial frontend.

## 📁 Project Structure

```text
CyberShield-Mini-SIEM/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── data/
│   ├── sample_logs/
│   │   ├── auth.log
│   │   ├── web_access.log
│   │   └── web_error.log
│   │
│   └── uploads/
│       └── .gitkeep
│
├── database/
│   ├── db.py
│   ├── schema.sql
│   └── .gitkeep
│
├── ingestion/
│   ├── __init__.py
│   ├── upload_handler.py
│   └── validators.py
│
├── parsers/
│   ├── __init__.py
│   ├── auth_parser.py
│   ├── web_parser.py
│   └── normalizer.py
│
├── detection/
│   ├── __init__.py
│   ├── engine.py
│   ├── rules.py
│   ├── risk_scoring.py
│   └── deduplication.py
│
├── alerts/
│   ├── __init__.py
│   ├── alert_manager.py
│   └── incident_workflow.py
│
├── dashboard/
│   ├── __init__.py
│   └── routes.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   ├── alerts.html
│   ├── alert_details.html
│   ├── investigations.html
│   └── upload.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── dashboard.js
│   │   └── charts.js
│   └── images/
│
├── tests/
│   ├── test_ingestion.py
│   ├── test_parsers.py
│   ├── test_detection.py
│   ├── test_alerts.py
│   └── test_dashboard.py
│
├── docs/
│   ├── architecture.md
│   ├── detection_rules.md
│   ├── database_schema.md
│   └── screenshots/
│
└── scripts/
    ├── generate_sample_logs.py
    └── initialize_db.py
```
---

## 🚀 Upcoming Work: Weeks 4–6

- **Week 4:** Develop the Flask application skeleton, SQLite configuration, logging, and basic frontend.
- **Week 5:** Implement secure CSV/JSON log uploads, input validation, file-size limits, and error handling.
- **Week 6:** Develop log parsers and a common normalized event model, including handling malformed log entries.

---

## 🎯 Project Goal

To develop a lightweight SIEM portal that collects and analyzes log data, detects suspicious activities using configurable rules, generates explainable security alerts, and presents useful information through a centralized dashboard.

**Note:** Detection rules are initial design specifications. Their implementation and validation will be documented as development progresses. Testing will use authorized environments and sample or synthetic log data.
