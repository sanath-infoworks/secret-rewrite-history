import psycopg2

DB_PASSWORD = "SuperSecretP@ssw0rd123"

def connect():
    return psycopg2.connect(host="db.example.com", user="admin", password=DB_PASSWORD)
