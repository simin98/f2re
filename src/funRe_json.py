from src.asvs_csv_to_json import convert_to_utf8
import pandas as pd
import json
import os
import chardet

def deal_xlsx()


if __name__=="__main__":
    print("--"*40)
    print("csv转json")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    xlsx_path = os.path.join(script_dir, '..', 'data', 'funcRE', 'annotationRQ1.xlsx')
    json_path = os.path.join(script_dir, '..', 'results', 'json_output', 'funRe_json_output.json')

    convert_to_utf8(xlsx_path)

