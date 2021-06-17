from flask_wtf import CSRFProtect
from redis import StrictRedis
from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
# 可以用来指定session 保存的 位置
from flask_session import Session
from flask_script import Manager


class Config(object):
    """项目的配置"""
    DEBUG = True
    SECRET_KEY = "tLBFjUQ2TOV/iNv55ijeQbjC4QA7Qc6BzgIBBB9PjQSlUn72Yhd/1qUaw58SYg=="

    # 为mysql添加篇配置
    SQLALCHEMY_DATABASE_URI ="mysql://root:mysql@127.0.0.1:3306/information06"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis的配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # Session保存配置
    SESSION_TYPE = "redis"
    # 开启session签名
    SESSION_USE_SIGNER = True
    # 指定Session保存的redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    # 设置需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 *2




app = Flask(__name__)

# 加载配置
app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)

# 初始化redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
# 开启当前项目CSRF保护 只做服务器验证功能
CSRFProtect(app)
# 设置session保存指定位置
Session(app)

manager = Manager(app)

@app.route("/")
def index():
    session["name"]="hk"
    return "index3333333"

if __name__ == '__main__':
    manager.run()