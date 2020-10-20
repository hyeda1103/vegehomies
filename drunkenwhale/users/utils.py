import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from drunkenwhale import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('비밀번호 재설정 요청', 
                sender='drunkenwhale00@gmail.com', 
                recipients=[user.email])
    msg.body = f'''비밀번호 재설정을 원하신다면, 다음의 링크를 클릭하시기 바랍니다:
{url_for('users.reset_token', token=token, _external=True)}

비밀번호 재설정을 요청하지 않았다면 본 메일을 무시하셔도 좋습니다. 귀하의 계정에 어떤 변화도 일어나지 않을 것입니다.
'''
    mail.send(msg)