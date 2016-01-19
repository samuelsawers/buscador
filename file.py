import MySQLdb
DB_HOST = 'localhost'
DB_DB = 'mq1'
DB_USER = 'root'
DB_PASS = ''

def run_query(query=''):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_DB]
    conn = MySQLdb.connect(*datos)
	cursor = conn.cursor()
	cursor.execute(query)
	if query.upper().startswith('SELECT'):
	    data = cursor.fetchall()
	else:
	    conn.commit()
	    data = None
	cursor.close
	conn.close()print result
	return data
result = run_query('SELECT * FROM usuario')
