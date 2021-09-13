from os import name


class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,category,country,url,description):
        self.id = id
        self.name = name
        self.category = category
        self.country = country
        self.url = url
        self.description = description


class NewsArticle:

    def __init__(self,id,name,title,author,description,url,urlToImage,publishedAt,content):
        self.id = id
        self.name = name
        self.title = title
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
    
    # def save_review(self):
    #     Review.all_reviews.appe