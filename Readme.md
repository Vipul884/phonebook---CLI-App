# Phonebook CLI

A lightweight command-line contact management tool written in Python, backed by a local SQLite database.

## Key Features

- **Full CRUD Operations:** Add, view, edit, and delete contact records.
- **Multi-Field Search:** Query records by Name (supports partial string matching), Phone Number, Address, City, or Pincode.
- **Parameterized Queries:** All SQL executions use placeholders (`?`) to prevent syntax errors and SQL injection.
- **Zero Dependencies:** Built entirely with Python standard libraries (`sqlite3`, `os`).
- **Auto-Initialization:** Automatically creates the storage directory and database schema on first run.

## Project Structure

```text
Phonebook/
├── Database/
│   └── Phonebook.db   # Created automatically on first run
├── Database.py        # SQLite schema setup and CRUD queries
├── Phonebook.py       # CLI interface and user interaction logic
└── README.md
```

## Database Schema

Table: `Phonebook_data`

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique record ID |
| `Name` | TEXT | NOT NULL | Contact full name |
| `Phone_no` | TEXT | NOT NULL | Contact phone number |
| `Address` | TEXT | | Street/Locality |
| `City` | TEXT | | City name |
| `Pincode` | TEXT | | Postal/ZIP code |

*(Note: Storing phone numbers and postal codes as text preserves leading zeros and international formatting).*

## Quickstart

### Prerequisites
- Python 3.8+ installed on your system.

### Running the Application

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/phonebook-cli.git
   cd phonebook-cli
   ```

2. Launch the CLI:
   ```bash
   python Phonebook.py
   ```

## Example Usage

```text
==============================
       PHONEBOOK CLI
==============================
[1] Add Contact
[2] View All Contacts
[3] Search Contact
[4] Edit Contact
[5] Delete Contact
[6] Exit
Select an option (1-6): 2

ID   Name            Phone        Address       City      Pincode
-------------------------------------------------------------------
1    Vipul         000000000    Civil Lines     XYZ       200001
-------------------------------------------------------------------
```

## Planned Roadmap

- Input sanitization (regex-based phone and postal code validation).
- CSV/JSON export and import capabilities.
- Refactor core logic into an Object-Oriented structure.
- Optional desktop GUI via Tkinter.

