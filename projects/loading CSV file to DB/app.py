import os
import json
import pandas as pd
import sys
import glob
import re
from dotenv import  load_dotenv
import multiprocessing

def get_column_names(schema,ds_name,sorting='column_position'):
    columns_details = schema[ds_name]
    columns = sorted(columns_details, key= lambda col: col[sorting])
    return[col['column_name'] for col in columns]

def read_csv(file,schema):
    path= (re.split(r"[/\\]",file))
    df_name = path[-2]
    columns = get_column_names(schema,df_name)
    df = pd.read_csv(file,names=columns,chunksize=10000)
    return df

def to_sql(df,conn_url,df_name):
    df.to_sql(df_name,
              conn_url,
              if_exists='append',
              index=False
            )
    
def db_loader(src_dir,conn_url,df_name):
    schema = json.load(open(f'{src_dir}/schemas.json'))
    files = glob.glob(f'{src_dir}/{df_name}/part-*')
    if len(files)==0:
        raise NameError(f'no such data frame exit with {df_name}')
    
    for file in files:
        df_reader = read_csv(file,schema)
        for idx,df in enumerate(df_reader):
            print(f'Procesing chunk {idx} of {df_name}')
            to_sql(df,conn_url,df_name)


def process_dataset(args):
    src_dir = args[0]
    db_conn_url = args[1]
    df_name = args[2]
    try:
        print(f'Processinf {df_name}')
        db_loader(src_dir,db_conn_url,df_name)
    except NameError as ne:
        print(ne)
        pass
    except Exception as e:
        print(e)
        pass
    finally:
        print(f'Processing {df_name}')



def process_files(df_names=None):
    load_dotenv()
    src_dir = os.getenv('SRC_DIR')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_user = os.environ.get('DB_USER')
    db_password = os.getenv('USER_PASSWORD')
    db_name = os.getenv('DB_NAME')
    db_conn_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    schema = json.load(open(f'{src_dir}/schemas.json'))

    if not df_names:
        df_names = schema.keys()

    pprocess_size = len(df_names) if len(df_names)<4 else 4
    pool=multiprocessing.Pool(pprocess_size)
    pd_args=[]

    for df_name in df_names:
        pd_args.append((src_dir,db_conn_url,df_name))

    pool.map(process_dataset , pd_args)


        


if __name__ == '__main__':
    if len(sys.argv) == 2:
        ds_names = json.loads(sys.argv[1])
        process_files(ds_names)
    else:
        process_files()

