# Employee Database Manager

## Description
Application for managing simple Employee database.

## Installation
Clone this repository to your local machine.
```bash
git clone git@github.com:illata1998/ptmk_test.git
cd ptmk_test
```
Install dependencies using [Poetry](https://python-poetry.org/docs/).
```bash
make install
```
Create the new .env file and define your database connection parameters (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT) there. For example,
```bash
echo "DB_NAME=ptmk_test_db" >> .env
echo "DB_USER=postgres" >> .env
echo "DB_PASSWORD=5456" >> .env
echo "DB_HOST=localhost" >> .env
echo "DB_PORT=5432" >> .env
```
Use the build command builds the source and wheels archives.
```bash
make build
```
Install the app.
```bash
make package-install
```

## Usage
```bash
# create the 'employees' database
ptmk_test 1
# insert an employee into the 'employees' database
ptmk_test "Ivanov Petr Sergeevich" 2009-07-12 Male
# fetch employees with unique combination of 
# 'full_name' and 'date_of_birth' fields
ptmk_test 3
# fill the 'employees' database with 1,000,000 fake employees
# and 100 fake male employees whose names start with the letter 'F'
ptmk_test 4
# fetch all the fake male employees whose names start with the letter 'F'
# and measure the execution time
ptmk_test 5
```