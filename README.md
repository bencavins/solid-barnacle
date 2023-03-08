# Object Relations Code Challenge - Articles

For this assignment, you will be working with a Magazine domain.

We have three models: `Author`, `Article`, and `Magazine`.

For our purposes, an `Author` has many `Article`s, a `Magazine` has many `Article`s, and `Article`s belong to both `Author` and `Magazine`.

`Author` - `Magazine` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed in a suggested order, but you can feel free to tackle the ones you think are easiest. Be careful: some of the later methods rely on earlier ones.

Writing error-free code is more important than completing all of the deliverables listed - prioritize writing methods that work over writing more methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First, prioritize getting things working. Then, if there is time at the end, refactor your code to adhere to best practices. When you encounter duplicated logic, extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you expect. If you have any methods that are not working yet, feel free to leave comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to build out any helper methods if needed.

### Initializers, Readers, and Writers

#### Author

- `Author __init__(self, name)`
  - An author is initialized with a name, as a string.
- `Author get_name()`
  - Returns the name of the author

#### Magazine

- `Magazine __init__(self, name, category)`
  - A magazine is initialized with a name as a string and a category as a string
- `Magazine get_name()`
  - Returns the name of this magazine
- `Magazine get_category()`
  - Returns the category of this magazine

#### Article

- `Article __init__(self, author, magazine, title)`
  - An article is initialized with an author as an `Author` object, a magazine as a `Magazine` object, and title as a string.
- `Article get_title()`
  - Returns the title for that given article

### Object Relationship Methods

#### Article

- `Article get_author()`
  - Returns the author for that given article
- `Article get_magazine()`
  - Returns the magazine for that given article

#### Author

- `Author get_articles()`
  - Returns an list of `Article` instances the author has written
- `Author get_magazines()`
  - Returns a list of `Magazine` instances for which the author has contributed to

#### Magazine

- `Magazine get_contributors()`
  - Returns an list of `Author` instances who have written for this magazine

### Associations and Aggregate Methods

#### Author

- `Author add_article(magazine, title)`
  - Given a magazine (as `Magazine` instance) and a title (as a string), creates a new `Article` instance and associates it with that author and that magazine.
- `Author topic_areas()`
  - Returns a list of strings with the categories of the magazines the author has contributed to

#### Magazine

- `Magazine article_titles()`
  - Returns an list strings of the titles of all articles written for that magazine
- `Magazine contributing_authors()`
  - Returns an list of authors who have written for the magazine
