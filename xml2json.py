#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import xmltodict
import glob
import os


def main():
    file_list = glob.glob('data/dblp.*.xml')
    for file in file_list:
        file_name = os.path.splitext(file)
        xml_file = open(file, 'r')
        xml_object = xml_file.read()
        xml_file.close()
        OB = xmltodict.parse(xml_object)
        JsonFile = open(file_name[0]+'.json', 'w')
        JsonFile.write(json.dumps(OB, sort_keys=True, indent=4))
        JsonFile.close()
        print("File %s done" % file_name[0])

if __name__ == '__main__':
    main()

