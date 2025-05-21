from flask import Flask
from data.data_productos import productos, categorias

app = Flask(__name__)

@app.route("/")
def home():
    nombre = "Axel"
    apellido = "Alan"
    descripcion = "Soy estudiante de Desarrollo Web, apasionado por la tecnologia y la programación"
    return f"Hola, soy {nombre} {apellido}. {descripcion}"

@app.route("/productos")
def listar_productos():
    resultado = "<h2>Listado de Productos</h2>"
    for producto in productos:
        resultado += f"ID: {producto['id']} - Descripción: {producto['descripcion']} - Categoria ID: {producto['categoria_id']}<br>"
    return resultado

@app.route("/categorias")
def listar_categorias():
    resultado = "<h2>Listado de Categorías</h2>"
    for categoria in categorias:
        resultado += f"ID: {categoria['id']} - Descripción: {categoria['descripcion']}<br>"
    return resultado

if __name__ == "__main__":
    app.run(debug=True)


