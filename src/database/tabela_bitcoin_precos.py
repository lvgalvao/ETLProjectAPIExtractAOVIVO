from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Float, String, Integer, DateTime
from datetime import datetime

# Cria a classe Base do SQLAlchemy (na versão 2.x)
Base = declarative_base()

class BitcoinPreco(Base):
    """Define a tabela no banco de dados."""
    __tablename__ = "bitcoin_precos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float, nullable=False)
    criptomoeda = Column(String(50), nullable=False)  # até 50 caracteres
    moeda = Column(String(10), nullable=False)        # até 10 caracteres
    timestamp = Column(DateTime, default=datetime.now)
