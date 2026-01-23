import os
import sys
import glob
import json
import pandas as pd
import re
from dotenv import  load_dotenv

def get_column_names (schema , df_name,sort_by='column_position'):
    column_names = schema[df_name]
    columns = sorted(column_names, key= lambda col : col[sort_by])
    return [col['column_name'] for col in columns]

def read_csv(file,schema):
    paths=(re.split(r"[/\\]",file))
    df_name = paths[-2]
    columns = get_column_names(schema,df_name)
    df=pd.read_csv(file,names=columns)
    return df

def to_json(df,tgt_base_dir,df_name,file_name):
    json_file_path = f'{tgt_base_dir}/{df_name}/{file_name}'
    os.makedirs(f'{tgt_base_dir}/{df_name}',exist_ok=True)
    df.to_json(json_file_path,
              orient='records',
              lines=True)
    

def file_converter(df_name,src_file_path,tgt_file_path):
    
    schema = json.load(open(f'{src_file_path}/schemas.json'))
    files=glob.glob(f'{src_file_path}/{df_name}/part-*')
    if len(files) == 0:
        raise NameError(f'no such data frame exit with {df_name}')
    
        
    for file in files:
        df = read_csv(file,schema)
        file_name = re.split(r'[/\\]',file)[-1]
        to_json(df,tgt_file_path,df_name,file_name)



def process_files(df_names=None):
    load_dotenv()
    src_file_path = os.getenv('SRC_FILE_PATH')
    tgt_file_path = os.getenv('TGT_FILE_PATH')

    schema = json.load(open(f'{src_file_path}/schemas.json'))

    if not df_names:
        df_names=schema.keys()
    for df_name in df_names:
        
        try:
            print(f'processing  {df_name}')
            file_converter(df_name,src_file_path,tgt_file_path)
        except NameError as ne:
                print(ne)
                print(f'error at {df_name}')
                pass


if __name__ == '__main__':
    if len(sys.argv) == 2:
        ds_names = json.loads(sys.argv[1])
        process_files(ds_names)
    else:
        process_files()