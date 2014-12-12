from connection import Base
from crawler import Cralwer
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def main():
    engine = create_engine("sqlite:///hacksearch.db")
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    pesho = Cralwer('www.mattcutts.com', session)
    pesho.start()

if __name__ == '__main__':
    main()
