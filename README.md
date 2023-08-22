# DataValidity

# Student Similarity Analysis Project

This Python project aims to analyze past student information and identify similarities based on specified criteria. It processes a CSV file containing student data and identifies students who share more than three similar criteria, such as name, age, date of birth, address, phone number, email, and school information.

## Features

- Loads student data from a CSV file.
- Compares student records based on specified criteria.
- Identifies students with more than three similar criteria.
- Provides a clear list of similar students.

## Prerequisites

- Python 3.x
- pandas library (`pip install pandas`)

## Installation

1. Clone this repository to your local machine using:

git clone https://github.com/rohankumar009/DataValidity.git

2. Navigate to the project directory:

cd student-similarity-analysis

## Usage

1. Prepare your CSV file containing student data. The CSV should have columns for Name, Age, Date of Birth, Address, Phone Number, Email, and School Information.
2. Modify the `csv_file` with the variable/criteria that is being tested
3. Run the script using: python "FILE_NAME".py
4. The script will print the names of students with more than three similar criteria.

## Contributing

Contributions are welcome! If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

