from models import Magazine, Author, Article


def test_magazine_init():
    """
    Should be able to initialize a magazine with
    a name and category
    """
    magazine = Magazine('Spooky Zine', 'horror')
    assert magazine.name == 'Spooky Zine'
    assert magazine.category == 'horror'

def test_magazine_get_name():
    """
    get_name() should return the name of the
    magazine
    """
    magazine = Magazine('Spooky Zine', 'horror')
    assert magazine.get_name() == 'Spooky Zine'

def test_magazine_get_category():
    """
    get_category() should return the category
    of the magazine
    """
    magazine = Magazine('Spooky Zine', 'horror')
    assert magazine.get_category() == 'horror'

def test_magazine_get_contributors():
    """
    get_contributors() should return a list of
    authors who have written for the magazine
    """
    author = Author('Stephen King')
    magazine = Magazine('Spooky Zine', 'horror')
    article = Article(author, magazine, 'Top 10 Horror Movies')
    magazine.articles = [article]
    assert magazine.get_contributors() == [author]

def test_magazine_article_titles():
    """
    article_titles() should return a list of 
    titles of all articles for the magazine
    """
    author = Author('Stephen King')
    magazine = Magazine('Spooky Zine', 'horror')
    article = Article(author, magazine, 'Top 10 Horror Movies')
    magazine.articles = [article]
    assert magazine.article_titles() == ['Top 10 Horror Movies']
