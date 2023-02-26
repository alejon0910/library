from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Book, Author, Publisher

publishers = [Publisher(name="Puffin"),
              Publisher(name="Scholastic"),
              Publisher(name="Penguin")]

authors = [Author(name="George Orwell"),
           Author(name="William Golding"),
           Author(name="Jane Austen"),
           Author(name="Neil Gaiman"),
           Author(name="Terry Pratchett")]

books = [Book(title="1984", isbn=9783161484100, num_pages=328, publication_date=1949, publisher_id=1),
         Book(title="Lord of The Flies", isbn=9783153485291, num_pages=284, publication_date=1954, publisher_id=2),
         Book(title="Pride and Prejudice", isbn=9783153725481, num_pages=412, publication_date=1813, publisher_id=3),
         Book(title="Animal Farm", isbn=97831275491243, num_pages=109, publication_date=1945, publisher_id=1),
         Book(title="Good Omens", isbn=97831215231243, num_pages=245, publication_date=1990, publisher_id=3)
         ]

authors[0].books.append(books[0])
authors[0].books.append(books[3])
authors[1].books.append(books[1])
authors[2].books.append(books[2])
authors[3].books.append(books[4])
authors[4].books.append(books[4])

# Connect to the activities database
engine = create_engine('sqlite:///library.sqlite', echo=True)

# Create a session and add the people to the database
with Session(engine) as sess:
    sess.add_all(books)
    sess.commit()
