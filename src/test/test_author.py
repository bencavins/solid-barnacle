from models import Author, Article, Magazine


def test_author_init():
    """
    Should be able to initialize an author
    with a name
    """
    author = Author('Stephen King')
    assert author.name == 'Stephen King'

def test_author_get_name():
    """
    get_name() should return the name of the
    author
    """
    author = Author('Stephen King')
    assert author.get_name() == 'Stephen King'

def test_author_get_articles():
    """
    get_articles() should return a list of 
    articles written by the author
    """
    author = Author('Stephen King')
    magazine = Magazine('Spooky Zine', 'horror')
    article = Article(author, magazine, 'Top 10 Horror Movies')
    author.articles = [article]
    assert author.get_articles() == [article]

def test_author_get_magazines():
    """
    get_magazines() should return a list of
    magazines the author has written articles
    for
    """
    author = Author('Stephen King')
    magazine = Magazine('Spooky Zine', 'horror')
    article = Article(author, magazine, 'Top 10 Horror Movies')
    author.articles = [article]
    assert author.get_magazines() == [magazine]

def test_author_add_article():
    """
    add_article(magazine, title) should add a new
    article with the given title for the given 
    magazine and associate it with the author
    """
    author = Author('Stephen King')
    magazine = Magazine('Spooky Zine', 'horror')
    author.add_article(magazine, 'Top 10 Horror Movies')
    assert len(author.get_articles()) == 1
    assert author.get_articles()[0].title == 'Top 10 Horror Movies'

def test_author_topic_areas():
    """
    topic_areas() should return a list of 
    magazine categories the author has 
    contributed to
    """
    author = Author('Stephen King')
    magazine = Magazine('Spooky Zine', 'horror')
    article = Article(author, magazine, 'Top 10 Horror Movies')
    author.articles = [article]
    assert author.topic_areas() == ['horror']
