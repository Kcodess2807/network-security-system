import os
import sys
import numpy as np
import pandas as pd

'''
data ingestion related constant start with variable name: DATA_INGESTION
'''

DATA_INGESTION_COLLECTION_NAME:str="NetworkData"
DATA_INGESTION_DATABASE_NAME:str='AKacademy'
DATA_INGESTION_DIR_NAME:str='data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR:str='feature_store'
DATA_INGESTION_INGESTED_DIR:str='ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float=0.2