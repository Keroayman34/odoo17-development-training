# Odoo 17 HMS Training

A beginner-friendly Hospital Management System (HMS) built using Odoo 17 during backend and ERP development training.

This project was developed step by step while learning core Odoo backend development concepts including models, views, relations, constraints, computed fields, CRM integration, and Odoo 17 compatibility fixes.

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
* Form and Tree Views
* XML View Inheritance
* Security Access Rules
* Odoo 17 Compatible UI Logic

The project is intentionally kept beginner-friendly while still following clean and professional Odoo development practices.

---

# Technologies Used

* Odoo 17
* Python
* PostgreSQL
* XML

---

# Current Branch

```bash
day3-constraints-and-crm
```

This branch contains:

* Day 1 HMS basics
* Day 2 relations and views
* Day 3 constraints, CRM integration, computed fields, logs, and Odoo 17 fixes

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
│   └── ir.model.access.csv
│
└── static/
    └── description/
```

---

# Features

## Patients

* Create and manage patients
* Auto calculate age from birth date
* PCR auto-check for patients below 30 years old
* Email validation and uniqueness
* Patient states management
* Department assignment
* Doctors assignment
* Upload patient image
* Patient log history tracking

---

## Departments

* Create hospital departments
* Define department capacity
* Open/close departments
* Link departments with patients

---

## Doctors

* Create doctors records
* Store doctors information
* Assign doctors to patients

---

## Patient Logs

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
* Security Access
* Menus & Actions
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
git clone <repo-url>
```

Go to the project:

```bash
cd hms
```

Run Odoo:

```bash
python3 odoo-bin --addons-path=addons,custom_addons
```

Upgrade HMS module:

```bash
python3 odoo-bin --addons-path=addons,custom_addons -u hms
```

---

# Future Improvements

Future training branches may include:

* Smart Buttons
* Search Views
* Record Rules
* Wizards
* ORM Advanced Methods
* Scheduled Actions
* Reports
* Dashboards
* API Integrations

---

# Learning Purpose

This project is built for educational and training purposes while learning Odoo 17 backend development step by step.
