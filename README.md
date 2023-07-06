
# Export All Database Tables to separate CSV Files
This Python script automates the process of exporting all database tables into separate CSV files. It supports PostreSQL & SQLite databases, but you can try it with other database systems as well. 

## Prerequisites
- Python 3.x
-  PostreSQL or SQLite database (example provided for PostreSQL , modify the code for other databases)

## Installation 
1. Clone the repository or download the repo directly.
2. Install the required dependencies by running the following command:
`pip install -r requirements.txt`

## Usage 
1. Place the script (`sqlalchemy-exports.py`) in your project directory or the desired location.
2. Replace the placeholders `<DATABASE_USERNAME>`, `<DATABASE_PASSWORD>`, `<DATABASE_HOST>`, `<DATABASE_PORT>`, `<DATABASE_NAME>` with the details of your PostgreSQL database or SQLite database file.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the following command to execute the script:
`python sqlalchemy-exports.py`
5. When prompted enter the project/folder name and press enter. This will connect to the database, retrieve all the table names, and export each table as a separate CSV file.
6. After running the script, you will find individual CSV files for each table in a new directory with the Project/folder name as the prefix.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details