from flask import render_template, url_for, jsonify, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from drunkenwhale import db, bcrypt
from drunkenwhale.models import User, Post
from pymongo import MongoClient   


bar = Blueprint('bar', __name__)


client = MongoClient('localhost', 27017)  #mongoDB는 27017 포트로 돌아갑니다.
dbMongo = client.dbsparta   #dbMongo라는 이름으로 'dbsparta'라는 이름의 DB를 불러옵니다 


## MongoDB에 있는 drunkenVege 이름의 DB를 불러옵니다
@bar.route('/vegeInfo', methods=['GET'])
def listing():
    # 모든 document 찾기 & _id 값은 출력에서 제외하기
    result = list(dbMongo.drunkenVege.find({},{'_id':0}))
    # drunkenVege라는 키 값으로 비건술집정보 내려주기
    return jsonify({'result':'success', 'drunkenVege':result})