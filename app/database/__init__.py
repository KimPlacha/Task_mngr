from flask import g
import sqlite3

DATABASE_URL = "main.db"


def get_db():  # sourcery skip: inline-immediately-returned-variable
    db = g._database or sqlite3.connect(DATABASE_URL)
    return db
