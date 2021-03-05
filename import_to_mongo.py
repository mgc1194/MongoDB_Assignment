#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import time
import glob
from pymongo import MongoClient


def main():
    # Ruta destino
    #client = MongoClient()
    client = MongoClient('localhost', 27017)

    # Collection name
    db = client.Publications
    # The collection is
    db.Publications.drop()

    file_list = glob.glob('data/dblp.*.json')

    # Loading json files.
    for json_file in file_list:
        print('Reading file %s' % json_file)
        start = time.time()
        with open(json_file) as file:
            Json = json.load(file)
        file.close()
        end = time.time()

        # Se seleccionan las publicaciones y no otra información
        articles = Json['dblp']

        # Se crea la colección.
        articles_colletion = db.Publications

        start2 = time.time()

        # Se van recorriendo los documentos e insertanto en la colección. Se
        # transforma el campo year a tipo entero.
        try:
            for journal in articles['article']:
                if 'year' in journal:
                    journal['year'] = int(float(journal['year']))
                journal['type'] = 'article'
                article_id = articles_colletion.insert_one(journal)
        except:
            print('No journal publications in this file.')
        try:
            for book in articles['incollection']:
                if 'year' in book:
                    book['year'] = int(float(book['year']))
                book['type'] = 'incollection'
                article_id = articles_colletion.insert_one(book)
        except:
            print('No book publications in this file.')
        try:
            for conference in articles['inproceedings']:
                if 'year' in conference:
                    conference['year'] = int(float(conference['year']))
                conference['type'] = 'inproceedings'
                article_id = articles_colletion.insert_one(conference)
        except:
            print('No conference publications in this file.')




if __name__ == '__main__':
    main()
