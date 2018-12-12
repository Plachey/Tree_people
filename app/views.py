from flask import render_template
from app import app
import sqlite3


@app.route('/')
@app.route('/index')
def index():
    conn = sqlite3.connect('employees.db')
    conn.row_factory = sqlite3.Row
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM employees WHERE Chief = 0")

        empl = []

        rows = c.fetchall()
        for row in rows:
            tmpdict = {}
            tmpdict['name'] = row['Name']
            tmpdict['position'] = row['Position']
            tmpdict['salary'] = row['Salary']
            tmpdict['date'] = row['Date']
            tmpdict['subordinates'] = []
            conn1 = sqlite3.connect('employees.db')
            conn1.row_factory = sqlite3.Row
            with conn1:
                c1 = conn.cursor()
                c1.execute("SELECT * FROM employees WHERE Chief = ?", (row['Id'],))
                subordinates = c1.fetchall()
                if len(subordinates) != 0:
                    for s in subordinates:
                        tmps = {}
                        tmps['name'] = s['Name']
                        tmps['position'] = s['Position']
                        tmps['salary'] = s['Salary']
                        tmps['date'] = s['Date']
                        tmps['subordinates'] = []
                        tmpdict['subordinates'].append(tmps)

                        conn2 = sqlite3.connect('employees.db')
                        conn2.row_factory = sqlite3.Row
                        with conn2:
                            c2 = conn.cursor()
                            c2.execute("SELECT * FROM employees WHERE Chief = ?", (s['Id'],))
                            subordinates2 = c2.fetchall()
                            if len(subordinates2) != 0:
                                for s2 in subordinates2:
                                    tmps2 = {}
                                    tmps2['name'] = s2['Name']
                                    tmps2['position'] = s2['Position']
                                    tmps2['salary'] = s2['Salary']
                                    tmps2['date'] = s2['Date']
                                    tmps2['subordinates'] = []
                                    tmps['subordinates'].append(tmps2)

                                    conn3 = sqlite3.connect('employees.db')
                                    conn3.row_factory = sqlite3.Row
                                    with conn3:
                                        c3 = conn.cursor()
                                        c3.execute("SELECT * FROM employees WHERE Chief = ?", (s2['Id'],))
                                        subordinates3 = c3.fetchall()
                                        if len(subordinates3) != 0:
                                            for s3 in subordinates3:
                                                tmps3 = {}
                                                tmps3['name'] = s3['Name']
                                                tmps3['position'] = s3['Position']
                                                tmps3['salary'] = s3['Salary']
                                                tmps3['date'] = s3['Date']
                                                tmps3['subordinates'] = []
                                                tmps2['subordinates'].append(tmps3)

                                                conn4 = sqlite3.connect('employees.db')
                                                conn4.row_factory = sqlite3.Row
                                                with conn4:
                                                    c4 = conn.cursor()
                                                    c4.execute("SELECT * FROM employees WHERE Chief = ?", (s3['Id'],))
                                                    subordinates4 = c4.fetchall()
                                                    if len(subordinates4) != 0:
                                                        for s4 in subordinates4:
                                                            tmps4 = {}
                                                            tmps4['name'] = s4['Name']
                                                            tmps4['position'] = s4['Position']
                                                            tmps4['salary'] = s4['Salary']
                                                            tmps4['date'] = s4['Date']
                                                            tmps3['subordinates'].append(tmps4)

            empl.append(tmpdict)
    return render_template("index.html",
                           title='Abz',
                           empl=empl)
