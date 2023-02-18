from sqlalchemy import Column, Integer, String, Table, UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

book_author = Table('book_author',
                    Base.metadata,
                    Column('id', Integer, primary_key=True),
                    Column('book_id', ForeignKey('book.id')),
                    Column('author_id', ForeignKey('author.id')),
                    UniqueConstraint('author_id', 'book_id')
                    )


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    isbn = Column(Integer, unique=True, nullable=False)
    num_pages = Column(Integer, unique=False, nullable=False)
    publication_date = Column(Integer, unique=False, nullable=False)
    publisher_id = Column(Integer, ForeignKey("publisher.id"), default=None)
    authors = relationship("Author",
                           secondary=book_author,
                           order_by='Author.name',
                           back_populates="books")

    def __repr__(self):
        return f"<Book({self.name})>"


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    books = relationship("Book",
                           secondary=book_author,
                           order_by='Book.title',
                           back_populates="authors")

    def __repr__(self):
        return f"<Author({self.name})>"


class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Publisher({self.name})>"
