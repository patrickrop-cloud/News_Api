from flask import render_template,request,redirect,url_for
# from app import app
from . import main
from ..requests import get_article, get_news, process_article

#Views
@main.route('/', methods=['GET'])
def index():

    '''
    View news page function that returns news details with its data
    '''
    news = get_news()
    title = 'News'
    return render_template('index.html', news = news, title = title)


@main.route('/source/<id>')
def article(id):
    '''
    view news page fucntion that returns articles details and its data.
    '''

    articles = get_article(id)
    title = 'News'

    return render_template('article.html', articles = articles, title=title)
