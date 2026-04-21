# 🧪 Urban.Grocers API - Test Automation Framework

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pytest](https://img.shields.io/badge/Tested%20With-Pytest-green)
![API](https://img.shields.io/badge/Testing-API-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![QA](https://img.shields.io/badge/Focus-QA%20Automation-blueviolet)

This project implements an automated API testing framework for the Urban.Grocers application.

The goal is to validate API reliability, data integrity, and correct behavior across different scenarios, simulating real-world backend testing conditions.

---

## 📌 Overview

The test suite focuses on validating the creation of kits through API endpoints, ensuring proper request handling and response validation.

Key scenarios covered:

* Valid kit creation
* Invalid input handling
* Boundary value validation
* Data integrity verification
* Negative testing scenarios

---

## 💼 Professional Context

This project demonstrates practical QA Automation skills aligned with real-world backend testing:

* API testing using automated scripts
* Validation of request/response cycles
* Detection of defects through negative testing
* Structured and maintainable test code
* Simulation of backend validation logic

---

## 🛠️ Technologies & Tools

* Python 🐍
* Pytest ⚡
* Requests 🌐
* Git & GitHub

---

## 📂 Project Structure

```bash id="3z1v9k"
urban-grocers-api-testing/
│
├── configuration.py              # Environment configuration
├── data.py                       # Test data and utilities
├── sender_stand_request.py       # API request handling
├── create_kit_name_kit_test.py   # Test cases
```

---

## 🔄 Example API Test Scenario

### 🔹 Request

```json id="n8o9k2"
POST /kits
{
  "name": "Weekly Groceries"
}
```

### 🔹 Expected Response

```json id="5k2n9q"
{
  "status": "success",
  "message": "Kit created successfully"
}
```

---

### 🔹 Negative Test Example

```json id="v7x1pl"
POST /kits
{
  "name": ""
}
```

### 🔹 Expected Response

```json id="d9k3lw"
{
  "status": "error",
  "message": "Name cannot be empty"
}
```

---

## ▶️ Running Tests

1. Clone the repository:

```bash id="k2m9pz"
git clone https://github.com/Fitzonder/qa-project-Urban-Grocers-app-es.git
cd urban-grocers-api-testing
```

2. Install dependencies:

```bash id="q9l2xv"
pip install -r requirements.txt
```

3. Run tests:

```bash id="b2n8xk"
pytest
```

---

## 🧪 Key Testing Validations

* API response status code validation
* Data integrity verification
* Input validation and error handling
* Negative and boundary testing
* Request/response consistency

---

## 📈 Skills Demonstrated

* API Test Automation
* Test Case Design
* Backend Validation Testing
* Debugging and issue identification
* Data-driven testing

---

## 🚧 Future Improvements

* Add more endpoint coverage
* Implement parameterized tests with pytest
* Integrate Allure Reports
* Add CI/CD pipeline (GitHub Actions)
* Environment-based configuration

---

## 👨‍💻 Author

Carlos Lenis
QA Automation Engineer (Junior) 🚀

---

## 📬 Contact

* LinkedIn: *https://www.linkedin.com/in/carlos-lenis-812a5918/*
* GitHub: https://github.com/Fitzonder



