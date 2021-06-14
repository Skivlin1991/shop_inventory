from models.manufacturer import Manufacturer
from flask import Flask,render_template,request,redirect 
from flask import Blueprint
from models.stock import Stock 
from templates import *
import repositories.stock_repository as stock_repository
import repositories.manufacturer_repository as manufacturer_repository
from models import *

stock_blueprint = Blueprint("stock",__name__)

@stock_blueprint.route("/stock")
def stock():
    stock = stock_repository.select_all() # NEW
    print(stock)
    return render_template("index.html", all_stock = stock)

# NEW
# GET'/stock/new'
@stock_blueprint.route('/stock/new', methods =['GET'])
def new_stock():
    manufacturers = manufacturer_repository.select_all()
    return render_template("new.html", all_manufacturers = manufacturers)

# CREATE
# POST '/stocks'
@stock_blueprint.route('/stock', methods = ['POST'])
def create_stock():
    name = request.form['name']
    description = request.form['description']
    manufacturer = manufacturer_repository.select(request.form['manufacturer_id'])
    cost = int (request.form['cost'])
    price = int (request.form['price'])
    stock = Stock(name, description,manufacturer,cost , price)
    stock_repository.save(stock)
    return redirect('/stock')
# SHOW
# GET'/stock/<id>'
@stock_blueprint.route('/stock/<id>', methods=['GET'])
def show_stock(id):
    stock = stock_repository.select(id)
    return render_template('show.html', stock=stock)

# EDIT
# GET '/stock/<id>/edit'
@stock_blueprint.route('/stock/<id>/edit', methods=['GET'])
def edit_stock(id):
    stock = stock_repository.select(id)
    manufacturer = manufacturer_repository.select_all()
    return render_template('edit.html',stock= stock, all_manufacturers= manufacturer)
    
# UPDATE
# PUT '/stock/<id>'
@stock_blueprint.route('/stock/<id>', methods= ["POST"])
def update_stock(id):
    name =request.form['name']
    description= request.form['description']
    price = int(request.form['price'])
    cost = int(request.form['cost'])
    in_stock = request.form['in_stock']
    manufacturer = manufacturer_repository.select(request.form['manufacturer_id'])
    stock = Stock(name, description, manufacturer, cost, price,in_stock, id)
    stock_repository.update(stock)
    return redirect('/stock')

@stock_blueprint.route("/stock/<id>/sell",methods=["POST"])
def sell_stock(id):
    stock_item = stock_repository.select(id)
    name = stock_item.name 
    description = stock_item.description
    price = stock_item.price
    cost = stock_item.cost
    in_stock = False
    manufacturer = manufacturer_repository.select(stock_item.manufacturer.id)
    stock = Stock(name,description,manufacturer, cost, price,in_stock,id)
    stock_repository.update(stock)
    return redirect('/stock')

# DELETE
# DELETE '/stock/<id>'
@stock_blueprint.route("/stock/<id>/delete", methods=['POST'])
def delete_stock(id):
    stock_repository.delete(id)
    return redirect('/stock')