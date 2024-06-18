import uuid

from sqlalchemy import Column, UUID, String, Date, UniqueConstraint

from Model.DatabaseSetup import Base


class MemberModel(Base):
    __tablename__ = "users"

    memberId = Column(UUID, primary_key=True, default=uuid.uuid4)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    birthDate = Column(Date, nullable=False)
    country = Column(String, nullable=False)
    city = Column(String, nullable=False)

    __table_args__ = (UniqueConstraint('firstName', 'lastName', 'country', 'city', name='_unique_member_uc'),)
