import json
import time
from pymongo import MongoClient


def main():
    # Ruta destino
    client = MongoClient()
    client = MongoClient('localhost', 27017)

    # Nombre de la colección destino
    db = client.Publications

    # Ruta y nombre del archivo origen
    json_dir = "./data/"
    json_name = "dblp.json"

    # Se lee el archivo origen.
    # 1554543526.0884762
    start = time.time()
    with open(json_dir + json_name) as file:
        Json = json.load(file)
    file.close()
    end = time.time()
    # 1554544637.8074813

    # Se seleccionan las publicaciones y no otra información
    articles = Json['dblp']

    # Como se da por hecho que la colección es nueva y no una actualización ni
    # una insercción adicional de la misma, se elimina previamente por si hubiera
    # alguna antigua.

    db.publications.drop()

    # Se crea la colección.
    articles_colletion = db.publications

    start2 = time.time()
    # 1554545651.7335484

    # Se van recorriendo los documentos e insertanto en la colección. Se
    # transforma el campo year a tipo entero.
    for revista in articles['article']:
        if 'year' in revista:
            revista['year'] = int(float(revista['year']))
        revista['type'] = 'article'
        article_id = articles_colletion.insert_one(revista)

    for libro in articles['incollection']:
        if 'year' in libro:
            libro['year'] = int(float(libro['year']))
        libro['type'] = 'incollection'
        article_id = articles_colletion.insert_one(libro)
    for congreso in articles['inproceedings']:
        if 'year' in congreso:
            congreso['year'] = int(float(congreso['year']))
        congreso['type'] = 'inproceedings'
        article_id = articles_colletion.insert_one(congreso)

    end2 = time.time()
    # 1554550267.6431792


if __name__ == '__main__':
    main()
