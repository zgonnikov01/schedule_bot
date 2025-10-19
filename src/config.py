from environs import Env

env = Env()
env.read_env("../.env")

BOT_TOKEN = env.str("BOT_TOKEN")

REDIS_PASSWORD = env.str("REDIS_PASSWORD")

MONGO_INITDB_ROOT_USERNAME = env.str("MONGO_INITDB_ROOT_USERNAME")
MONGO_INITDB_ROOT_PASSWORD = env.str("MONGO_INITDB_ROOT_PASSWORD")

ADMIN_IDS = env.list("ADMIN_IDS", subcast=int)
