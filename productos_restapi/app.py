#importamos las librerias
from flask import Flask, json, jsonify, request


#inicialisanmos la variable app
app = Flask(__name__)

#importamos los datos de la dase de datos 
from products import products


#prueba del servidor
@app.route('/ping')
def ping():
    return jsonify({"message": "pong!"})


#prueba de los productos 
@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "lista de productos"})

#Buscar productos
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if(len(productFound) > 0):
        return jsonify({"product": productFound[0]})
    return jsonify({"message": "product not found"})



#Agregar productos 
@app.route('/products', methods=['POST'])
def addProduct():
    #print(request.json)
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "product added succesfully", "products": products})



#Actualizamos los productos 
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if(len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({"message": "product updated", "product": productFound[0]})
    return jsonify({"message": "product not found"})




#eliminamos los productos
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if(len(productFound)>0):
        products.remove(productFound[0])
        return jsonify({
            "message": "Product Deleted",
            "products": products
        })
    return jsonify({"message": "product not found"})
    

#INICIAMOS EL SERVIDOR EN EL PUERTO 4000    
if __name__ == '__main__':
    app.run(debug=True, port=4000)