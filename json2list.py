#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
#
# __author__ = Su
#


import os
import json


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(ROOT_PATH, "test.json")
OUTPUT_PATH = os.path.join(ROOT_PATH, "test.list")


def read_json(file_path, output_path):
    """ 
    read a json file and change it into a list
    input: json
    output: [ key value ]
    """
    with open(file_path, 'r', encoding='UTF-8') as j:
        
        try:
            know = json.load(j)
            
            # change json to list
            output = json2list(know)
            
            all_know = set()
            for s in output:
                if s:
                    all_know.add(s)

            with open(output_path, "w", encoding='UTF-8') as o:
                for k in all_know:
                    o.write(str(k) + "\n")
                    
        except json.decoder.JSONDecodeError:
            print("INFO: Json parse error.")
            
            return None


def json2list(knowledge):
    know_list = []

    def sub_list(know_json):
        
        if isinstance(know_json, dict):
            for key in know_json:
                know_list.append(key)
                sub_list(know_json[key])
        elif isinstance(know_json, list):
            for j in know_json:
                sub_list(j)
        else:
            know_list.append(know_json)

    sub_list(knowledge)
    return know_list


if __name__ == "__main__":
    read_json(DATA_PATH, OUTPUT_PATH)
