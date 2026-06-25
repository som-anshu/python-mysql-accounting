# Python-SQL Connectivity Accounting Software

A CLI-based accounting application developed as an investigatory project for Class 12 Computer Science. The system interfaces a Python backend with a MySQL database to record, update, view, and manage client invoicing records.

---

## Features

- **Add Data**: Append new invoice records containing client name, billing amount, and date.
- **Delete Record**: Remove entries permanently from the database via an invoice number.
- **Modify/Update**: Edit existing client names, billing amounts (override or incremental modifications), and invoice dates.
- **Targeted Search**: Query complete records filtered by a specific client name or transaction date.
- **View Entire Dataset**: Fetch and display all active table records instantly.

---

## Database Architecture

The system utilizes a single table named `record` within an `account` database:

```sql
CREATE DATABASE account;
USE account;

CREATE TABLE record (
    invoice_no VARCHAR(4) PRIMARY KEY,
    client VARCHAR(20) NOT NULL,
    billing_amount INTEGER NOT NULL,
    Date DATE NOT NULL
);
