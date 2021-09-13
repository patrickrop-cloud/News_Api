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
    """
  Function that gets the json response to our url request
  """
    get_news_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=3a404420748f44a4b0e8dcabe5b7b563'

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_source = None

        if get_news_response["sources"]:
            news_source_list = get_news_response["sources"]
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
        id = news_item.get("id")
        name = news_item.get("name")
        description = news_item.get("description")
        url = news_item.get("url")
        category = news_item.get("category")
        country = news_item.get("country")

        news_object = News(
            id, name, description,url,category,country
        )
        news_source.append(news_object)

    return news_source

def process_article(news_list):
    """
    Function  that processes the news article and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_source: A list of news objects
    """
    news_article = []
    for news_item in news_list:
        id = news_item.get("id")
        name = news_item.get("name")
        author = news_item.get("author")
        title = news_item.get("title")
        description = news_item.get("description")
        url = news_item.get("url")
        urlToImage = news_item.get("urlToImage")
        publishedAt = news_item.get("publishedAt")
        content = news_item.get("content")

        if urlToImage:
            news_object = NewsArticle(
                id,name,author,title,description,url,urlToImage,publishedAt,content
            )
            news_article.append(news_object)

    return news_article


#Getting news articles:
def get_article(id):
    """
  Function that gets the json response to our url request
  """
    get_news_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=3a404420748f44a4b0e8dcabe5b7b563'.format(id)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_article = None

        if get_news_response["articles"]:
            news_article_list = get_news_response["articles"]
            news_article = process_article(news_article_list)

    return news_article




