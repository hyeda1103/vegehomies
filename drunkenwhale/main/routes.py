from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from drunkenwhale import db
from drunkenwhale.models import Post
from drunkenwhale.posts.forms import PostForm


main = Blueprint('main', __name__)


@main.route('/')
def home():
   return render_template('home.html')


@main.route('/dashboard')
@login_required
def dashboard():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)

    return render_template('dashboard.html', name=current_user.username)
