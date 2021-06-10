from db.run_sql import run_sql
from models.manufacturer import Manufacturer
from models.stock import Stock

def save(manufacturer):
    sql = "INSERT INTO manufacturers(first_name, last_name) VALUES(%s,%s) RETURNING *"
    values = [manufacturer.first_name, manufacturer.last_name]
    results = run_sql(sql,values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer

def select_all():
    manufacturer = []
    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)
    
    for row in results:
        new_manufacturer = Manufacturer(row['first_name'],
        row['last_name'], row['id'])
        manufacturer.append(new_manufacturer)
    return manufacturer

def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    
    if result is not None:
        manufacturer = Manufacturer(result['first_name'],result['last_name'],result['id'])
        return manufacturer

def delete_all():
    sql = 'DELETE FROM manufacturer WhERE id = %s'
    values = [id]
    run_sql(sql, values)
    
def delete(id):
    sql = "DELETE FROM manufacturer WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
def update(manufacturer):
    stock = []
    sql='SELECT * FROM stock WHERE manufacturer_id = %s'
    values = [manufacturer.id]
    results = run_sql(sql,values)
    for row in results:
        stock = Stock(row['name'],row['description'],row['manufacturer'],row['cost'],row['price'],row['id'])
        stock.append(stock)
    return stock
