from .models import News, NewsArticle
import urllib.request,json

api_key = None
base_url = None

def configure_request(app):
    global api_key,base_url,news_article_url
    api_key = app.config['NEWS_API_KEY']
    news_article_url = app.config['NEWS_ARTICLE_URL']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news():
    '''
    Function to get json response to url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_source = None

        if get_news_response['sources']:
            news_source_list = get_news_response['sources']
            news_source = process_source(news_source_list)
    
    return news_source

def process_source(news_list):
    """
    Function  that processes the news source and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_source: A list of news objects
    """
    news_source = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        category = news_item.get('category')
        country = news_item.get('country')
        url = news_item.get('url')
        description = news_item.get('description')

        news_object = News(
            id,name,category,country,url,description
        )
        news_source.append(news_object)

    return news_source


        







        

    

