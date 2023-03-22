from flask import Blueprint,render_template

main = Blueprint('main', __name__)

@main.route('/')
def home_page():
    return '<h1>This is Hoge page</h1>'

