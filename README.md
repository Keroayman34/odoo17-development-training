# Odoo 17 HMS Training

A beginner-friendly Hospital Management System (HMS) built using Odoo 17 during backend and ERP development training.

This project was developed step by step while learning core Odoo backend development concepts including models, views, relations, constraints, computed fields, CRM integration, security, reporting, and Odoo 17 compatibility fixes.

---

# Project Overview

The project is a custom HMS (Hospital Management System) module for Odoo 17.

The module currently supports:

* Patient Management
* Department Management
* Doctors Management
* Patient State Management
* Patient Log History
* CRM Customer Integration
* Computed Fields
* API & SQL Constraints
* Security Groups & Record Rules
* QWeb PDF Reporting
* Form and Tree Views
* XML View Inheritance
* Odoo 17 Compatible UI Logic

The project is intentionally kept beginner-friendly while still following clean and professional Odoo development practices.

---

# Technologies Used

* Odoo 17
* Python
* PostgreSQL
* XML
* QWeb Reports

---

# Current Branch

```bash
day4-security-and-reports
````

This branch contains:

* Day 1 HMS basics
* Day 2 relations and views
* Day 3 constraints and CRM integration
* Day 4 security system and reporting

---

# Project Structure

```text
hms/
│
├── __init__.py
├── __manifest__.py
│
├── models/
│   ├── __init__.py
│   ├── patient.py
│   ├── department.py
│   ├── doctors.py
│   ├── patient_log.py
│   └── res_partner.py
│
├── views/
│   ├── patient_view.xml
│   ├── department_view.xml
│   ├── doctors_view.xml
│   ├── patient_log_view.xml
│   └── res_partner_view.xml
│
├── security/
│   ├── ir.model.access.csv
│   ├── res_groups.xml
│   └── record_rules.xml
│
├── reports/
│   ├── patient_report.xml
│   └── patient_report_template.xml
│
└── static/
    └── description/
```

---

# Features

# Patients

* Create and manage patients
* Auto calculate age from birth date
* PCR auto-check for patients below 30 years old
* Email validation and uniqueness
* Patient states management
* Department assignment
* Doctors assignment
* Upload patient image
* Patient log history tracking
* Patient PDF report generation

---

# Departments

* Create hospital departments
* Define department capacity
* Open/close departments
* Link departments with patients

---

# Doctors

* Create doctors records
* Store doctors information
* Assign doctors to patients

---

# Patient Logs

Automatically creates logs when:

* Patient state changes

Each log contains:

* Created By
* Date
* Description

Example:

```text
State changed to serious
```

---

# CRM / Contacts Integration

Extended Odoo Contacts model (`res.partner`) with:

* Related Patient field
* Customer validation rules
* Delete protection for linked customers
* Website field inside list view
* Mandatory Tax ID validation

---

# Relations Implemented

| Relation              | Type      |
| --------------------- | --------- |
| Patient → Department  | Many2one  |
| Department → Patients | One2many  |
| Patient ↔ Doctors     | Many2many |
| Customer → Patient    | Many2one  |

---

# Security System (Day 4)

Implemented professional role-based access control using Odoo security groups and record rules.

## HMS User Group

HMS Users can:

* Create their own patients
* Read their own patients
* Update their own patients
* Read departments
* Read doctors

Restrictions:

* Cannot delete patients
* Cannot manage departments
* Cannot manage doctors
* Cannot see doctors menu
* Cannot see doctors field inside patient form
* Can only access their own patient records

---

## HMS Manager Group

HMS Managers can:

* Full CRUD on patients
* Full CRUD on departments
* Full CRUD on doctors
* View all patients
* Access all menus and fields

---

# Patient PDF Report

Implemented a professional QWeb PDF report for patients.

The report includes:

* Patient Image
* Name
* Age
* Birth Date
* Blood Type
* PCR Status
* Email
* Department
* Assigned Doctors
* Patient Logs History

The report uses:

* QWeb PDF
* web.external_layout
* Odoo Report Actions

---

# Odoo Concepts Practiced

* Models
* Fields
* Relations
* Tree Views
* Form Views
* XML Inheritance
* Model Inheritance
* Computed Fields
* Related Fields
* API Constraints
* SQL Constraints
* Onchange Methods
* Security Groups
* Record Rules
* Access Rights
* Menus & Actions
* QWeb Reports
* Odoo 17 Modern Syntax

---

# Business Logic

Implemented business rules including:

* Closed departments cannot be selected
* Doctors field becomes readonly until department selected
* PCR auto-check for young patients
* CR Ratio becomes required when PCR is checked
* History field hidden for patients under 50
* Email uniqueness validation
* CRM customer protection
* Automatic patient state logs
* Ownership-based patient access

---

# Odoo 17 Compatibility

This project follows Odoo 17 compatible syntax.

Deprecated syntax removed:

* attrs
* states

Modern Odoo 17 expressions are used instead.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Keroayman34/odoo17-development-training.git
```

Go to the project:

```bash
cd odoo17-development-training
```

Create virtual environment:

```bash
python3 -m venv .venv
```

Activate virtual environment:

```bash
source .venv/bin/activate
```

Install Python requirements:

```bash
pip install -r requirements.txt
```

Run PostgreSQL service:

```bash
sudo service postgresql start
```

Run Odoo:

```bash
python3 odoo-bin --addons-path=addons,custom_addons
```

Upgrade HMS module:

```bash
python3 odoo-bin --addons-path=addons,custom_addons -u hms
```

Open browser:

```text
http://localhost:8069
```

---

# Git Workflow

Main development branches:

```bash
day1-day2
day3-constraints-and-crm
day4-security-and-reports
```

Each branch represents training progress and feature evolution during the course.

---

# Future Improvements

Future training branches may include:

* Smart Buttons
* Search Views
* Wizards
* ORM Advanced Methods
* Scheduled Actions
* Dashboards
* REST APIs
* Website Integration
* Barcode Integration
* Accounting Integration

---

# Learning Purpose

This project is built for educational and training purposes while learning Odoo 17 backend and ERP development step by step.

The project focuses on understanding real Odoo architecture and backend development fundamentals using practical labs and incremental feature implementation.

```
```
