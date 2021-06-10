import psycopg2
import psycopg2 as ext 

def run_sql(sql, vales= None):
    conn = None
    reults = []
    
    try:
        conn=psycopg2.connect("dbname='shop_inventory'")
        cur =conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql,values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except(Exception, psycopg2.CheckDatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        return results