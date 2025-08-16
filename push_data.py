import os
import sys
import json
from dotenv import load_dotenv
load_dotenv()

MONGODB_URL=os.getenv('MONGODB_URL')
print(MONGODB_URL)

import certifi  
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networkSecurity.exception.exception import NetworkSecurityException
from networkSecurity.logging.logger import logging

class networkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv2json(self, file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            #for every record wwe will have a json
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def insert_to_mongodb(self, records, database, collection):
        try:
            self.mongo_client = pymongo.MongoClient(MONGODB_URL, tlsCAFile=ca)
            db = self.mongo_client[database]         
            col = db[collection]                     
            col.insert_many(records)                
            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

        
if __name__=='__main__':
    FILE_PATH='network_data/phisingData.csv'
    DATABASE='arushK'
    Collection='NetworkData'
    networkobj=networkDataExtract()
    records=networkobj.csv2json(file_path=FILE_PATH)
    print(records)
    num_records=networkobj.insert_to_mongodb(records=records, database=DATABASE, collection=Collection)
    print(num_records)
        
