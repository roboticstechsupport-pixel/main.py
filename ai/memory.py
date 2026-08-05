"""
==========================================================
Project ULTRON
AI Memory System
memory.py
==========================================================
"""

import sqlite3
from pathlib import Path
from datetime import datetime


class Memory:

    def __init__(self, config):

        self.config = config

        self.database = Path(config.DATABASE_PATH)

        self.connection = sqlite3.connect(
            self.database,
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self._create_tables()

        print("[Memory] Database Ready")

    ############################################################

    def _create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            role TEXT NOT NULL,

            message TEXT NOT NULL,

            timestamp TEXT NOT NULL

        )
        """)

        self.connection.commit()

    ############################################################

    def save(self, role, message):

        self.cursor.execute(
            """
            INSERT INTO conversations
            (role, message, timestamp)
            VALUES (?, ?, ?)
            """,
            (
                role,
                message,
                datetime.now().isoformat()
            )
        )

        self.connection.commit()

    ############################################################

    def get_recent(self, limit=20):

        self.cursor.execute(
            """
            SELECT role, message, timestamp
            FROM conversations
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )

        rows = self.cursor.fetchall()

        rows.reverse()

        return rows

    ############################################################

    def search(self, keyword):

        self.cursor.execute(
            """
            SELECT role, message, timestamp
            FROM conversations
            WHERE message LIKE ?
            ORDER BY id DESC
            """,
            (f"%{keyword}%",)
        )

        return self.cursor.fetchall()

    ############################################################

    def count(self):

        self.cursor.execute(
            "SELECT COUNT(*) FROM conversations"
        )

        return self.cursor.fetchone()[0]

    ############################################################

    def clear(self):

        self.cursor.execute(
            "DELETE FROM conversations"
        )

        self.connection.commit()

    ############################################################

    def export(self, filename="conversation_log.txt"):

        rows = self.get_recent(100000)

        with open(filename, "w", encoding="utf-8") as file:

            file.write("PROJECT ULTRON Conversation Log\n")
            file.write("=" * 60 + "\n\n")

            for role, message, timestamp in rows:

                file.write(f"[{timestamp}] {role.upper()}\n")
                file.write(message + "\n\n")

        print(f"[Memory] Exported to {filename}")

    ############################################################

    def close(self):

        self.connection.close()

        print("[Memory] Database Closed")
