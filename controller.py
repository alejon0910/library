from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from email_models import Email

class Controller:
    def __init__(self):
        self.engine = create_engine('sqlite:///emails.sqlite', echo=True)

    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:

            with Session(self.engine) as sess:
                sess.add(Email(address=email))
                sess.commit()

        except ValueError as error:
            # show an error message
            raise ValueError