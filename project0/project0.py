def fetchincidents(url):
    '''This function fetches the pdf file from the url'''
    import urllib.request
    import requests
    data = urllib.request.urlopen(url).read()
   #data = data.encode('utf-8')
    with open('/tmp/arrests.pdf','wb') as p:
         p.write(data)
    return[]
def extractincidents():
    '''This function extracts the text and converts pdf to a dataframe'''
    import tempfile
    import PyPDF2
    import pandas as pd
    with open('/tmp/arrests.pdf','rb') as p:
        pdfReader = PyPDF2.PdfFileReader(p)
        pdfReader.getNumPages()
        page1 = pdfReader.getPage(0).extractText()
        page1 = page1.replace(' \n',' ').replace('-\n','-')
        rows=page1.split(';')

    cells=[]
    for i in range(len(rows)):
        cells.append(rows[i].split('\n'))
    for i in cells[1:]:
        del i[0]
    del cells[0][0:13]
    del cells[-1]
    for i in range(len(cells)):
        cells[i][6:-2] = [' '.join(cells[i][6:-2])]
    return(cells)

def createdb():
    '''This function creates a database connection to the SQLite database and create a database and a table'''
    import sqlite3
    conn=sqlite3.connect('normanpd.db',timeout=15)
    print("Database created")
    sql = conn.cursor()
    sql.execute( '''DROP TABLE IF EXISTS arrests''')
    sql.execute( '''CREATE TABLE arrests(arrest_time TEXT,
    case_number TEXT,
    arrest_location TEXT,
    offense TEXT,
    arrestee_name TEXT,
    arrestee_birthday TEXT,
    arrestee_address TEXT,
    status TEXT,
    officer TEXT);''')
    conn.commit()
    conn.close()
    return ('normanpd.db')
    
def populatedb(db,incidents):
    '''This function inserts the data extracted from the PDF into the database'''
    import sqlite3
    conn = sqlite3.connect(db,timeout=60)
    print('Connected to the DB')
    sql=conn.cursor()

    for i in incidents:
        sql.execute('INSERT INTO arrests(arrest_time,case_number,arrest_location,offense,arrestee_name,arrestee_birthday,arrestee_address,status,officer) VALUES (?,?,?,?,?,?,?,?,?)',(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))

    print("Database Populated")
    conn.commit()
    conn.close()

def status(db):
    import sqlite3
    conn=sqlite3.connect(db,timeout=30)
    print('Connected to the DB')
    sql=conn.cursor()

    sql.execute("SELECT * FROM arrests ORDER BY RANDOM() LIMIT 1;")
    for row in sql.fetchall():
        for i in range(len(row)):
            print(row[i],'þ',end=" ")

    conn.commit()
    conn.close()
