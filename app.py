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
            'titulo': pelicula.titulo, 
            'url_imagen' : pelicula.url_imagen, 
            'puntuacion': pelicula.puntuacion,
            'duracion' : pelicula.duracion,
            'sinopsis' : pelicula.sinopsis
            })
    return jsonify(json_peliculas)

@app.route('/modificarPelicula', methods = ['POST'])
def modificarPelicula():
    datos = request.get_json()
    titulo_actual = datos['titulo_actual']
    titulo = datos['titulo']
    url_imagen = datos['url_imagen']
    puntuacion = datos['puntuacion']
    duracion = datos['duracion']
    sinopsis = datos['sinopsis']
    global peliculas
    for pelicula in peliculas:
        if pelicula.titulo == titulo_actual:
            for pelicula2 in peliculas:
                if pelicula2.titulo == titulo:
                    return jsonify({'mensaje': 'Error, ya existe en la lista de peliculas el nuevo nombre, prueba otro'}), status.HTTP_400_BAD_REQUEST
            pelicula.titulo = titulo
            pelicula.url_imagen = url_imagen
            pelicula.puntuacion = puntuacion
            pelicula.duracion = duracion
            pelicula.sinopsis = sinopsis
            return jsonify({'mensaje': 'Satisfactorio, la pelicula se modificó correctamente'})
    return jsonify({'mensaje': 'Error, la pelicula no existe en la lista de peliculas'}), status.HTTP_400_BAD_REQUEST

@app.route('/eliminarPelicula', methods = ['POST'])
def eliminarPelicula():
    datos = request.get_json()
    titulo = datos['titulo']
    global peliculas
    i = 0
    for pelicula in peliculas:
        if pelicula.titulo == titulo:
            peliculas.pop(i)
            return jsonify({'mensaje': 'Satisfactorio, la pelicula se eliminó correctamente'})
        i += 1
    return jsonify({'mensaje': 'Error, la pelicula no existe en la lista de peliculas'}), status.HTTP_400_BAD_REQUEST

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port = '3000')