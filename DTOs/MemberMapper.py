from DTOs.Member import MemberCreate, Member
from Model.model import MemberModel

from utils import calculateDaysTillBirthday


class MemberMapper:
    def fromMemberCreate(self, memberCreate: MemberCreate) -> MemberModel:
        return MemberModel(firstName=memberCreate.firstName, lastName=memberCreate.lastName,
                           birthDate=memberCreate.birthDate, country=memberCreate.country, city=memberCreate.city)

    def toMemberDTO(self, member: MemberModel) -> Member:
        return Member(firstName=member.firstName, lastName=member.lastName,
                      birthDate=member.birthDate, country=member.country, city=member.city,
                      memberId=str(member.memberId), daysTillBirthday=calculateDaysTillBirthday(member.birthDate))
