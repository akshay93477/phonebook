import sqlite3

# Function to create the contacts table
def create_contacts_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Cell TEXT,
            Email TEXT
        )
    ''')

# Function to insert data into the contacts table
def insert_contact(cursor, name, cell, email):
    cursor.execute('''
        INSERT INTO contacts (Name, Cell, Email)
        VALUES (?, ?, ?)
    ''', (name, cell, email))

# Function to fetch all data from the contacts table
def fetch_all_contacts(cursor):
    cursor.execute('SELECT * FROM contacts')
    return cursor.fetchall()

# Connect to SQLite database
conn = sqlite3.connect('phone_book.db')
cursor = conn.cursor()

# Create contacts table if not exists
create_contacts_table(cursor)

# Insert 5 rows of data
contacts_data = [
    ('John Doe', '1234567890', 'john@example.com'),
    ('Jane Smith', '9876543210', 'jane@example.com'),
    ('Bob Johnson', '5551234567', 'bob@example.com'),
    ('Alice Williams', '9998887777', 'alice@example.com'),
    ('Charlie Brown', '7773331111', 'charlie@example.com')
]

for contact in contacts_data:
    insert_contact(cursor, *contact)

# Commit the changes to the database
conn.commit()

# Fetch all data and display on screen
all_contacts = fetch_all_contacts(cursor)
print("ID\tName\t\tCell#\t\tE-mail")
print("-------------------------------------")
for contact in all_contacts:
    print(f"{contact[0]}\t{contact[1]}\t{contact[2]}\t{contact[3]}")

# Close the connection
conn.close()