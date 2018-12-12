from faker import Factory
from faker.providers import person, job, date_time
from random import randint
import sqlite3

conn = sqlite3.connect('employees.db')
c = conn.cursor()

fake = Factory.create()
fake.add_provider(person)
fake.add_provider(job)
fake.add_provider(date_time)


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS employees(Id INTEGER PRIMARY KEY, '
              'Name TEXT, '
              'Position TEXT, '
              'Date INT, '
              'Salary REAL, '
              'Chief TEXT)')


def data_entry():
    for z in range(50000):
        name = fake.name()
        position = fake.job()
        date_work = fake.date_this_year(before_today=True, after_today=False)
        salary = randint(3700, 10000)

        chief = randint(1, 4)

        c.execute("INSERT INTO employees (Name, Position, Date, Salary, Chief) VALUES (?, ?, ?, ?, ?)",
                (name, position, date_work, salary, chief))

    conn.commit()
    c.close()
    conn.close()


create_table()
data_entry()
