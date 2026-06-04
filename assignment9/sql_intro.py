import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "magazines.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)


def add_publisher(conn, name):
    try:
        row = conn.execute(
            "SELECT publisher_id FROM publishers WHERE name = ?", (name,)
        ).fetchone()
        if row:
            return row[0]
        cursor = conn.execute(
            "INSERT INTO publishers (name) VALUES (?)", (name,)
        )
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")
        return None


def add_magazine(conn, name, publisher_id):
    try:
        row = conn.execute(
            "SELECT magazine_id FROM magazines WHERE name = ?", (name,)
        ).fetchone()
        if row:
            return row[0]
        cursor = conn.execute(
            "INSERT INTO magazines (name, publisher_id) VALUES (?, ?)",
            (name, publisher_id),
        )
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")
        return None


def add_subscriber(conn, name, address):
    try:
        row = conn.execute(
            "SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?",
            (name, address),
        ).fetchone()
        if row:
            return row[0]
        cursor = conn.execute(
            "INSERT INTO subscribers (name, address) VALUES (?, ?)",
            (name, address),
        )
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")
        return None


def add_subscription(conn, subscriber_id, magazine_id, expiration_date):
    try:
        row = conn.execute(
            """SELECT subscription_id FROM subscriptions
               WHERE subscriber_id = ? AND magazine_id = ? AND expiration_date = ?""",
            (subscriber_id, magazine_id, expiration_date),
        ).fetchone()
        if row:
            return row[0]
        cursor = conn.execute(
            """INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date)
               VALUES (?, ?, ?)""",
            (subscriber_id, magazine_id, expiration_date),
        )
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")
        return None


# Connect to a new SQLite database
with sqlite3.connect(DB_PATH) as conn:  # Create the file here, so that it is not pushed to GitHub!
    conn.execute("PRAGMA foreign_keys = 1")
    print("Database created and connected successfully.")

    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
                publisher_id INTEGER PRIMARY KEY,
                name TEXT UNIQUE NOT NULL
            )
        """)
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")

    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                magazine_id INTEGER PRIMARY KEY,
                name TEXT UNIQUE NOT NULL,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
            )
        """)
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")

    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                subscriber_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                address TEXT NOT NULL
            )
        """)
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")

    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                subscription_id INTEGER PRIMARY KEY,
                subscriber_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                expiration_date TEXT NOT NULL,
                FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
                FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
            )
        """)
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")

    conde = add_publisher(conn, "Conde Nast")
    hearst = add_publisher(conn, "Hearst Communications")
    meredith = add_publisher(conn, "Meredith Corporation")

    vogue = add_magazine(conn, "Vogue", conde)
    cosmopolitan = add_magazine(conn, "Cosmopolitan", hearst)
    better_homes = add_magazine(conn, "Better Homes & Gardens", meredith)
    gq = add_magazine(conn, "GQ", conde)

    jane_main = add_subscriber(conn, "Jane Doe", "123 Main St, Durham, NC")
    john_oak = add_subscriber(conn, "John Smith", "456 Oak Ave, Raleigh, NC")
    jane_pine = add_subscriber(conn, "Jane Doe", "789 Pine Rd, Chapel Hill, NC")
    bob_main = add_subscriber(conn, "Bob Wilson", "321 Elm St, Durham, NC")

    add_subscription(conn, jane_main, vogue, "2026-12-31")
    add_subscription(conn, john_oak, cosmopolitan, "2026-06-30")
    add_subscription(conn, jane_pine, better_homes, "2027-01-15")
    add_subscription(conn, bob_main, gq, "2026-09-01")
    add_subscription(conn, jane_main, gq, "2026-03-31")

    conn.commit()

    # Task 4: Write SQL Queries
    print("\nAll subscribers:")
    for row in conn.execute("SELECT * FROM subscribers"):
        print(row)

    print("\nAll magazines (sorted by name):")
    for row in conn.execute("SELECT * FROM magazines ORDER BY name"):
        print(row)

    print("\nMagazines for Conde Nast:")
    for row in conn.execute(
        """
        SELECT magazines.magazine_id, magazines.name, magazines.publisher_id
        FROM magazines
        JOIN publishers ON magazines.publisher_id = publishers.publisher_id
        WHERE publishers.name = ?
        """,
        ("Conde Nast",),
    ):
        print(row)
