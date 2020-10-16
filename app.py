from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_api import status
import json
from Pelicula import Pelicula

app = Flask(__name__)
CORS(app)

peliculas = []

@app.route('/', methods = ['GET'])
def inicio():
    return "Api Iniciada"

@app.route('/agregarPelicula', methods = ['POST'])
def agregarPelicula():
    datos = request.get_json()
    titulo = datos['titulo']
    url_imagen = datos['url_imagen']
    puntuacion = datos['puntuacion']
    duracion = datos['duracion']
    sinopsis = datos['sinopsis']
    nueva_pelicula = Pelicula(titulo, url_imagen, puntuacion, duracion, sinopsis)
    global peliculas
    for pelicula in peliculas:
        if pelicula.titulo == titulo:
            return jsonify({'mensaje': 'Error, la pelicula ya existe'}), status.HTTP_400_BAD_REQUEST
    peliculas.append(nueva_pelicula)
    return jsonify({'mensaje': 'Satisfactorio, la pelicula se agrego correctamente'})

@app.route('/obtenerPeliculas', methods = ['GET'])
def ontenerFunciones():
    json_peliculas = []
    global peliculas
    for pelicula in peliculas:
        json_peliculas.append({
            'titulos': pelicula.titulo, 
            'url_imagen' : pelicula.url_imagen, 
            'puntuacion': pelicula.puntuacion,
            'duracion' : pelicula.duracion,
            'sinopsis' : pelicula.sinopsis
            })
    return jsonify(json_peliculas)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port = '3000')