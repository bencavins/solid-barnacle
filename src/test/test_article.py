from models import Article, Author, Magazine


def test_article_init():
    """
    Should be able to initialize an article
    with an author, magazine, and title
    """
    author = Author('Stephen King')
    magazine = Magazine('Spooky Zine', 'horror')
    article = Article(author, magazine, 'Top 10 Horror Movies')
    assert article.author == author
    assert article.magazine == magazine
    assert article.title == 'Top 10 Horror Movies'

def test_article_get_title():
    """
    get_title() should return the title of
    the article
    """
    author = Author('Stephen King')
    magazine = Magazine('Spooky Zine', 'horror')
    article = Article(author, magazine, 'Top 10 Horror Movies')
    assert article.get_title() == 'Top 10 Horror Movies'

def test_article_get_author():
    """
    get_author() should return the author
    of the aricle
    """
    author = Author('Stephen King')
    magazine = Magazine('Spooky Zine', 'horror')
    article = Article(author, magazine, 'Top 10 Horror Movies')
    assert article.get_author() == author

def test_article_get_magazine():
    """
    get_magazine() should return the magazine
    the article is written for
    """
    author = Author('Stephen King')
    magazine = Magazine('Spooky Zine', 'horror')
    article = Article(author, magazine, 'Top 10 Horror Movies')
    assert article.get_magazine() == magazine
