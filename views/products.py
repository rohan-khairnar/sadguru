from flask import Flask, render_template, request,redirect, Response, url_for 
import json
import sqlalchemy as sa
from sqlalchemy.sql import select
from models.meta import dbconnect
from models.databases import products
from app import app

eng = dbconnect()

@app.route('/', methods=['GET'])
def home():
    con = eng.connect()
    result = con.execute(select([products.c.prodname,products.c.prodrate,products.c.prodcode]))
    result = result.fetchall()
    return render_template('homepage.html',data = result)

@app.route('/product-details/<prod_code>', methods=['GET'])
def productDetails(prod_code):
    con = eng.connect()
    result = con.execute(select([products]).where(products.c.prodcode == prod_code))
    result = result.fetchone()
    return render_template('productdetails.html',data = result)

@app.route('/new-product')
def addProductPage():
    return render_template('addproduct.html')

@app.route('/save-product', methods=['POST'])
def saveProduct():
    data = request.form
    con = eng.connect()
    result = con.execute(products.insert(),[data])
    return redirect(url_for("addProductPage"))

@app.route('/delete-product/<prod_code>')
def deleteProduct(prod_code):
    con = eng.connect()
    result = con.execute("delete from products where prodcode="+prod_code)
    return redirect(url_for("home"))

@app.route('/update-product', methods=['POST'])
def updateProduct():
    raw_data = str(request.get_data())[2:-1].split('&',3)
    data = dict(s.split('=', 1) for s in raw_data)
    con = eng.connect()
    result = con.execute("update products set prodname='%s' , prodrate=%d , proddesc='%s' where prodcode=%d"%(data['name'],int(data['rate']),data['desc'],int(data['code'])))
    return redirect(url_for("productDetails",prod_code=int(data['code'])))

@app.route('/print', methods=['GET'])
def viewPrintFormat():
    con = eng.connect()
    result = con.execute(select([products.c.prodname,products.c.prodrate,products.c.prodcode]))
    result = result.fetchall()
    return render_template('print.html',data=result)