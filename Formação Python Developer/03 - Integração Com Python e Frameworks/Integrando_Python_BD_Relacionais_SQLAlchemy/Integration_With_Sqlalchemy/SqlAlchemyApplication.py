import sqlalchemy
from sqlalchemy import Column, create_engine, inspect
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    # Atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address (id={self.id}, email={self.email_address})"


print(User.__tablename__)
print(Address.__tablename__)

# Conexão com o banco de dados
engine = create_engine("sqlite://")

# Criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

insp = inspect(engine)

# Verifica se a tabela existe e retorna um booleano
print(insp.has_table("user_account"))

# Retorna nomes das tabelas
print(insp.get_table_names())

# Retorna o nome do banco de dados
print(insp.default_schema_name)

