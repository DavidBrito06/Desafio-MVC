from sqlalchemy import Column, BIGINT, String
from src.models.sqlite.settings.base import Base

class PersonPj(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(BIGINT, primary_key=True)
    faturamento = Column(BIGINT, nullable=False)
    idade = Column(BIGINT, nullable=False)
    nome_fantasia = Column(String, nullable=False)
    celular = Column(String, nullable=False)
    email_corporativo = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    saldo = Column(BIGINT, nullable=False)

    def __repr__(self):
        return f"<PersonPj(id={self.id}, nome_fantasia='{self.nome_fantasia}', faturamento={self.faturamento})>"
