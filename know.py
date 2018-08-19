#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# __author__ = Su
#


import os
import re
import json


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(ROOT_PATH, "知识库.json")
OUTPUT_PATH = os.path.join(ROOT_PATH, "知识库.list")


def is_number(s):
    try:
        complex(s) # for int, long, float and complex
    except ValueError:
        return False
    return True


def read_json(file_path, output_path):
    with open(file_path, 'r', encoding='UTF-8') as knowledge:
        try:
            know = json.load(knowledge)
            output = set(json2list(know))
            all_know = []
            for s in output:
                if s:
                    if isinstance(s, str) and not isinstance(s, int):
                        for sub_s in re.split("、|;|；|，", s):
                            if "占位病变" in s:
                                print(sub_s)
                            if not is_number(sub_s):
                                all_know.append(sub_s)
                    else:
                        if not is_number(str(s)):
                            all_know.append(s)
            all_know = set(all_know)

            with open(output_path, "w", encoding='UTF-8') as o:
                for k in all_know:
                    o.write(str(k) + "\n")

        except json.decoder.JSONDecodeError:
            print("json parse error.")
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
