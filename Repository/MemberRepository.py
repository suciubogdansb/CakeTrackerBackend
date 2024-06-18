from sqlalchemy.orm import Session

from Model.DatabaseSetup import SessionLocal
from Model.model import MemberModel


class MemberRepository:
    def __init__(self):
        self.__db: Session = SessionLocal()

    def getMembers(self):
        return self.__db.query(MemberModel).all()

    def addMember(self, member: MemberModel):
        self.__db.add(member)
        self.__db.commit()
        self.__db.refresh(member)
        return member


