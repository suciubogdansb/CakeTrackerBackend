from datetime import date
from pydantic import BaseModel


class MemberCreate(BaseModel):
    firstName: str
    lastName: str
    birthDate: date
    country: str
    city: str

    def toJSON(self):
        return {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "birthDate": str(self.birthDate),
            "country": self.country,
            "city": self.city
        }

    class Config:
        orm_mode = True


class Member(MemberCreate):
    memberId: str
    daysTillBirthday: int

    def toJSON(self):
        return {
            "memberId": self.memberId,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "birthDate": str(self.birthDate),
            "country": self.country,
            "city": self.city,
            "daysTillBirthday": self.daysTillBirthday
        }

    class Config:
        orm_mode = True


