# 🏥 Patient Data Management System – Hasan Sadikin Hospital (Dummy Project)

This project is a **Capstone Project** that simulates a patient data management system for a hospital.
All data used in this project is **not real patient data**, but **dummy data** created for learning purposes only.

## 📌 Main Features

This CLI (Command Line Interface) application provides the following features:

1. **User Login & Logout**
2. **Show Patient Database**

   * Display all patient data
   * Search patient data
   * Show user dashboard
3. **Add Patient Database**

   * Add a new patient
   * Bulk insert (add multiple patients at once)
   * Add patient diagnosis
   * Add a new user
4. **Delete Patient Database**

   * Delete patient data by ID
5. **Update Patient Database**

   * Update specific patient information (name, room, diagnosis, family phone number, etc.)

## 🗂️ Data Structure

Initial dataset (dummy data):

```python
data_pasien = [
    {'ID':1,'nama pasien':'Ahmad Fadhil','kamar pasien':305,'diagnosa':'Dengue Fever','no telp keluarga':'081234567890','nama keluarga':'Siti Aminah'},
    {'ID':2,'nama pasien':'Liana Putri','kamar pasien':208,'diagnosa':'Throat Infection','no telp keluarga':'082233445566','nama keluarga':'Andi Pratama'},
    {'ID':3,'nama pasien':'Budi Santoso','kamar pasien':405,'diagnosa':'Asthma','no telp keluarga':'083344556677','nama keluarga':'Dewi Sartika'},
    {'ID':4,'nama pasien':'Rina Mariani','kamar pasien':101,'diagnosa':'Severe Asthma','no telp keluarga':'085123456789','nama keluarga':'Yudi Prakoso'}
]

data_user = [{'ID':1,'user':'Admin','password':'Admin123'}]
```

## 🚀 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```
2. Run the program with Python:

   ```bash
   python main.py
   ```
3. Log in using the default account:

   ```
   USER     : Admin
   PASSWORD : Admin123
   ```

## 🛠️ Tech Stack

* **Python 3** (no external libraries)
* Data stored in **list of dictionaries**
* CLI built using `input()` and `print()`

## 📖 Program Flow

* **Login** → Access the main dashboard
* **Main Menu**:

  1. Show hospital database
  2. Add hospital database
  3. Delete hospital database
  4. Update hospital database
  5. Log out
  6. Exit program

## ⚠️ Disclaimer

* All patient data is **fictional (dummy data)** and does not represent real individuals.
* This project is for **learning purposes only** as part of a capstone project in Python.

---
