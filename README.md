# Employee Database Manager

## Description
Application for managing simple Employee database.

## Installation
Clone this repository to your local machine.
```bash
git clone https://github.com/illata1998/ptmk_test.git

cd ptmk_test
```
Install dependencies using [Poetry](https://python-poetry.org/docs/).
```bash
make install
```
Create the new config.py file in the 'ptmk_test' directory (not in the root directory) and define your database connection parameters (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT) there. For example,
```bash
cd ptmk_test

echo "DB_NAME = 'your_db_name'" >> config.py
echo "DB_USER = 'your_user_name'" >> config.py
echo "DB_PASSWORD = 'your_password'" >> config.py
echo "DB_HOST = 'your_host'" >> config.py
echo "DB_PORT = 5432" >> config.py
```
Go back to the root directory and use the build command to build the source and wheels archives.
```bash
cd ..

make build
```
Install the app.
```bash
make package-install
```

## Usage
```bash
# create the 'employees' table
ptmk-app 1

# insert an employee into the 'employees' table
ptmk-app "Ivanov Petr Sergeevich" 2009-07-12 Male

# fetch employees with unique combination of 
# 'full_name' and 'date_of_birth' fields
ptmk-app 3

# fill the 'employees' tabke with 1,000,000 fake employees
# and 100 fake male employees whose names start with the letter 'F'
ptmk-app 4

# fetch all the fake male employees whose names start with the letter 'F'
# and measure the execution time
ptmk-app 5
```
## Screenshots

<img width="759" alt="Modes 1-4 running successfully" src="https://github.com/user-attachments/assets/348d3c94-9aff-4506-89d8-efd2f43b1b40">

<img width="759" alt="Mode 5 execution time" src="https://github.com/user-attachments/assets/44fb5650-4bd7-4660-a06a-4dcc6fd791a4">
