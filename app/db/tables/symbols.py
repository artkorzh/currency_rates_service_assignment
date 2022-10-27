from sqlalchemy import Column, Integer, String, Sequence

from app.db.base_class import Base


class Symbol(Base):
    __tablename__ = "symbols"

    id: int = Column(Integer, Sequence("symbols_id_seq", start=1), primary_key=True)
    symbol = Column(String, nullable=False, unique=True)
