import sqlite3

conn = sqlite3.connect("research_history.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT,
    report TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()


def save_report(topic, report):
    cursor.execute(
        """
        INSERT INTO history(topic, report)
        VALUES (?, ?)
        """,
        (topic, report)
    )
    conn.commit()


def get_reports():
    cursor.execute("""
    SELECT id, topic, created_at
    FROM history
    ORDER BY id DESC
    """)
    return cursor.fetchall()


def get_report(report_id):
    cursor.execute(
        """
        SELECT report
        FROM history
        WHERE id=?
        """,
        (report_id,)
    )
def total_reports():
    cursor.execute("SELECT COUNT(*) FROM history")
    return cursor.fetchone()[0]


def latest_report():
    cursor.execute("""
        SELECT created_at
        FROM history
        ORDER BY id DESC
        LIMIT 1
    """)

    row = cursor.fetchone()

    return row[0] if row else "No reports yet"

    row = cursor.fetchone()

    return row[0] if row else ""