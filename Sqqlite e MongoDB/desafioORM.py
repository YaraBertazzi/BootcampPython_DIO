from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey



Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    # atributos

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(String)
    endereco = Column(String)

    conta = relationship(
        "Conta", back_populates="user", cascate="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, cpf={self.cpf}, endereco={self.endereco})"



class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    saldo = Column(Integer)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("user", back_populates="conta")


    def __repr__(self):
        return f"Conta(id={self.id}, tipo={self.tipo}, agencia={self.agencia})"



print(User.__tablename__)
print(Conta.__tablename__)


engine = create_engine("sqlite://")


Base.metadata.create_all(engine)


inspector_engine = inspect(engine)

with Session(engine) as session:
    lais = User(
        name='lais',
        cpf='12345678900',
        conta=[Conta(agencia='1234')]
    )

    session.add_all([lais])
    session.commit()

stnt = select(User).where(User.name.in_(["lais"]))
for user in session.scalars(stnt):
    print(user)

stnt_conta = select(Conta).where(Conta.user_id.in_([2]))
for conta in session.scalars(stnt_conta):
    print(conta)
