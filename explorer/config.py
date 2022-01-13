import os
import json

# SERVER_HOST = '0.0.0.0'
SERVER_PORT = 7070
# cache config

CACHE_TYPE = 'RedisCache'
CACHE_REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
CACHE_REDIS_PORT = os.getenv('REDIS_PORT', "6379")
CACHE_REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', "")
CACHE_REDIS_DB = 1

# Mongodb
MONGODB_NAME = os.getenv("MONGODB_NAME_EXPLORER") #  "explorer_stat_v2"
MONGODB_HOST = json.loads(os.getenv("MONGODB_HOST"))
MONGODB_USER = os.getenv("MONGODB_USER")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")

# 冰河
BINGHE_HOST = os.getenv("BINGHE_HOST")
BINGHE_SECRET= os.getenv("BINGHE_SECRET")