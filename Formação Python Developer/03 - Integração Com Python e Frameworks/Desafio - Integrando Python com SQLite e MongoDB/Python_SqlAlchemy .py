from sqlalchemy import DECIMAL, Column, ForeignKey, Integer, String, create_engine, func, inspect, select
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30))
    CPF = Column(String(15), unique=True)
    endereço = Column(String(50))
    
    conta = relationship("Conta", back_populates="cliente")
    
    def __repr__(self):
        return f"Cliente(id={self.id}, nome={self.nome}, CPF={self.CPF}, endereço={self.endereço})"
    

    
class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String)
    agência = Column(String)
    num = Column(Integer, unique=True)
    saldo = Column(DECIMAL)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    
    cliente = relationship("Cliente", back_populates="conta")
    
    def __repr__(self):
        return f"Conta(id={self.id}, tipo={self.tipo}, agência={self.agência}, num={self.num}, saldo={self.saldo})"
    

    
engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

insp = inspect(engine)

print(insp.get_table_names()) 

with Session(engine) as session:
    Gustavo = Cliente(
        nome = "Gustavo Pereira",
        CPF = "001.001.001-01",
        endereço = "Taguatinga - Brasília/DF",
    conta=  [Conta(tipo="Corrente",
                       agência = "001",
                       num=11111111,
                       saldo=1000.00)]
        
    )
    Matheus = Cliente(
        nome = "Matheus Oliveira",
        CPF = "002.002.002-02",
        endereço = "Ceilândia - Brasília/DF",
        conta=  [Conta(tipo="Corrente",
                       agência = "002",
                       num=2222222222,
                       saldo=10.00)]
        
    )
    Geovana = Cliente(
        nome = "Geovana Albuquerque",
        CPF = "003.003.003-03",
        endereço = "Plano Piloto - Brasília/DF",
        conta=  [Conta(tipo="",
                       agência ="003",
                       num=2222222,
                       saldo=15.00)]
        
    )
    session.add_all([Gustavo, Matheus, Geovana])
    session.commit()

stmt_join = select(Cliente, Conta).join_from(Cliente, Conta)   
connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
for x in results:
    print(x)




