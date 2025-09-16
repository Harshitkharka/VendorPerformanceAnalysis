import psycopg2
import pandas as pd
import numpy as np
import time
import sqlite3
import logging
import os

logging.basicConfig(
    format='%(asctime)s %(levelname)s : %(message)s',
    level=logging.DEBUG
)

logging.info('----Fetching tables from postgresql database---\n')
#------------------------------------------------------------------------------
# Establishing connecting with Postgres Database
#------------------------------------------------------------------------------
try:
    conn = psycopg2.connect(
    host="localhost",
    database="inventory",
    port ="5432",
    user="postgres",
    password="1999"
)
except Exception as e:
    logging.error(f'Error establishing connection: {e}')
else:
    logging.info('---Established connection Successfully---')

#------------------------------------------------------------------------------
# Importing tables from Postgres Database
#------------------------------------------------------------------------------
def loading_raw_data():
    try:
        tables ={'begin_inventory': 'select * from begin_inventory;',
          'end_inventory':'select * from end_inventory;',
          'purchase_prices':'select * from purchase_prices;',
          'purchases':'select * from purchases;',
          'sales':'select * from sales',
          'vendor_invoice':'select * from vendor_invoice'
        }
    except Exception as e:
        logging.error(f'error : {e}')

    #------------------------------------------------------------------------------
    # Creating inventory data directory
    #------------------------------------------------------------------------------
    try:
      os.makedirs("InventoryData",exist_ok=True)
    except Exception as e:
        logging.error(f'Error Creating directory{e}')
    else:
        logging.info("-- Directory created successfully-- ")

    #------------------------------------------------------------------------------
    # displaying tables from database
    #------------------------------------------------------------------------------
    for table,query in tables.items():
        try:
            df=pd.read_sql_query(query,conn)
            # Creating file path with .csv
            file_path=os.path.join("InventoryData",f'{table}.csv')
            print(file_path)
            # saving as csv
            df.to_csv(file_path,index=False)
        except Exception as e:
          logging.error(f'Error {e}')
        else:
          logging.info(f"--Successfully loaded {table} to inventory data -- ")
            
loading_raw_data()

conn = sqlite3.connect("Inventory.db")

def ingest_db():
        for file in os.listdir("InventoryData"):
            try:
                if file.endswith('.csv'):
                        file_path=os.path.join("InventoryData",file)

                        table_names = os.path.splitext(file)[0]

                        df=pd.read_csv(file_path)
                        df.to_sql(table_names,conn,if_exists='replace',index=False)
            except Exception as e:
                  logging.error(f'Error {e}')
            else:
                  logging.info(f"--Successfully loaded {table_names} to inventory.db -- ")

ingest_db()