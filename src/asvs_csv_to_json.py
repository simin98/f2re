import csv
import json
import os
import chardet


def convert_to_utf8(input_file,output_file=None):
    with open(input_file,'rb') as f:
        raw_data=f.read()
        result = chardet.detect(raw_data)
        original_encoding = result['encoding']

    try:
        with open(input_file,'r',encoding=original_encoding) as f:
            content =f.read()

        with open(input_file,'w',encoding='utf-8') as f:
            f.write(content)

    except Exception as e:
        print(f"转换失败: {e}")

def csv_to_json(csv_file_input,json_file_output=None):
    '''
        将CSV文件转换为JSON格式
        输出格式: vr_full_text = f"{chapter_title} - {section_title} - {description}"

        参数:
        csv_file_path: CSV文件路径
        output_file_path: 可选，输出的JSON文件路径

    '''

    data_list=[]

    try:
        with open(csv_file_input, 'r', encoding='utf-8') as csv_file:
            csv_reader=csv.DictReader(csv_file)

            for row in csv_reader:
                chapter_title=row.get('chapter_name','')
                section_title = row.get('section_name', '')
                description=row.get('req_description','')

                data_item={
                    'chapter_title':chapter_title,
                    'section_title':section_title,
                    'description':description

                }

                data_list.append(data_item)

        if json_file_output:
                with open(json_file_output,'w',encoding='utf-8') as json_file:
                    json.dump(data_list,json_file,ensure_ascii=False, indent=4)
                print(f"文件已保存到：{json_file_output}")

        return data_list

    except FileNotFoundError:
        print(f"找不到文件")
        return None

    except Exception as e:
        print(f"error:{str(e)}")
        return None

if __name__=="__main__":
    print("--"*40)
    print("csv转json")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, '..', 'data', 'asvs', 'OWASP.csv')
    json_path = os.path.join(script_dir, '..', 'results', 'json_output', 'json_file_output.json')

    convert_to_utf8(csv_path)

    result=csv_to_json(csv_path,json_path)



