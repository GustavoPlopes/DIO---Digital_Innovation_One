import sqlalchemy
from sqlalchemy import Column, create_engine, func, inspect, select
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    # Atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="User", cascade="all, delete-orphan"
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
        return f"Address (id={self.id}, email_address={self.email_address})"


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

# Declarando dados 
with Session(engine) as session:
    juliana = User(
        name="Juliana",
        fullname="Juliana Mascarenhas",
        address=[Address(email_address="julianam@gmail.com")]
    )
    Sandy = User(
        name="Sandy",
        fullname="Sandy Cardoso",
        address=[Address(email_address="sandy@hotmail.com"),
                 Address(email_address="sandy@gmail.com")]
    )
    Patrick = User(
        name="Patrick",
        fullname="Patrick Cardoso"
    )
    
    # Enviando para o banco de dados
    session.add_all([juliana, Sandy, Patrick])
    session.commit()

# Recuperando usuário a partir de uma filtragem
stmt = select(User).where(User.name.in_(["Juliana", "Sandy"]))
for user in session.scalars(stmt):
    print(user)
print()
    
# Recuperando o address de sandy através do user_id
stmt_address = select(Address).where(Address.user_id.in_([2]))
for address in session.scalars(stmt_address):
    print(address)
print()

# Recuperando todos os usuários de forma ordenada (desc para decrecente, asc para ascendente)
stmt_order = select(User).order_by(User.fullname)
for user in session.scalars(stmt_order):
    print(user)
print()

#Recupera todos os dados e faz a junção de User e Address 
stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
for result in results:
    print(result)
print()

# Recupera e faz a contagem total de User
stmt_count = select(func.count("*")).select_from(User)
for result in session.scalars(stmt_count):
    print(result)
