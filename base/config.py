from datetime import timedelta

# ---------------------------------------------------
# 环境
# ---------------------------------------------------
ENV = 'testing'
DEBUG = True
DEBUG_LEVEL = 'DEBUG'

# ---------------------------------------------------
# Sentry Error Track Config
# ---------------------------------------------------
SENTRY_ENABLE = False
SENTRY_DSN = ''
GIT_DIRECTORY = ''

# ---------------------------------------------------
# Zipkin APM Config
# ---------------------------------------------------
ZIPKIN_ENABLE = False
ZIPKIN_DSN = ''
ZIPKIN_SAMPLE = 0.5

# ---------------------------------------------------
# 允许跨域访问
# ---------------------------------------------------
CORS_ENABLE = False

# ---------------------------------------------------
# Consul配置
# ---------------------------------------------------
CONSUL_HOST = ''
CONSUL_PORT = 8500
CONSUL_TOKEN = None

# ---------------------------------------------------
# SESSION
# ---------------------------------------------------
# SECRET_KEY = b'>\xb4\x06\xa7BTm\xe5\x12d6\x17[\xba\xf4v\xb4q\xb0d\x1f\x85A}'
# SESSION_TYPE = 'redis'
# SESSION_COOKIE_HTTPONLY = False
# SESSION_COOKIE_NAME = 'n_session_id'
# SESSION_REDIS_HOST = 'localhost'
# SESSION_REDIS_PORT = 6379
# SESSION_REDIS_DB = 0
# SESSION_REDIS_PASSWORD = ''
#
# # session time
# PERMANENT_SESSION_LIFETIME = timedelta(days=1)

