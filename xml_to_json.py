import gzip
import json
import xmltodict


def main():
    # se descomprime y se parsea para posteriormente copiarlo en json
    xml_file = gzip.open('dblp.xml.gz')
    xml_object = xml_file.read()
    OB = xmltodict.parse(xml_object)
    JsonOB_encoded = json.dumps(OB)
    JsonOB_decoded = json.loads(JsonOB_encoded)
    with open('dblp.json', 'w') as file:
        json.dump(JsonOB_decoded, file, indent=4)


if __name__ == '__main__':
    main()
