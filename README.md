# Smart Sales Forecasting & Business Analytics System

Starter full-stack project based on the resume description: Python for forecasting, Java Spring Boot for an API layer, and MySQL for data management.

## Folders
- `ml-service/` - Python + scikit-learn sales forecasting
- `springboot-service/` - Spring Boot REST API starter
- `database/` - MySQL database schema and sample data

## Run Python forecasting
```bash
cd ml-service
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python forecast.py
```

## Run Spring Boot
Install Java 17 and Maven, then:
```bash
cd springboot-service
mvn spring-boot:run
```
Open `http://localhost:8080/api/forecast`.

## Database
Run `database/schema.sql` in MySQL. Before using JDBC operations, set your own username/password in `application.properties`.

## Note
This repository is a clean starter implementation derived from the project description on the resume. Replace sample data and connect your final ML model/API flow when you have your original project files.
