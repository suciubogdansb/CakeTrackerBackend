from datetime import date

from DTOs.Member import Member, MemberCreate
from DTOs.MemberMapper import MemberMapper
from Model.model import MemberModel
from Repository.MemberRepository import MemberRepository


class MemberService:
    def __init__(self):
        self.__memberRepository = MemberRepository()
        self.__mapper = MemberMapper()

    def getMembers(self) -> list[Member]:
        return [self.__mapper.toMemberDTO(member) for member in self.__memberRepository.getMembers()]

    def addMember(self, member: MemberCreate) -> Member:
        age = (date.today() - member.birthDate).days / 365.25
        if age < 18:
            raise ValueError("Member must be at least 18 years old")
        memberModel = self.__mapper.fromMemberCreate(member)
        return self.__mapper.toMemberDTO(self.__memberRepository.addMember(memberModel))

    def getMembersSorted(self) -> list[Member]:

        def calculateDaysTillBirthday(member: MemberModel):
            today = date.today()
            birthday = member.birthDate.replace(year=today.year)
            if birthday < today:
                birthday = birthday.replace(year=today.year + 1)
            return (birthday - today).days

        members: list[MemberModel] = self.__memberRepository.getMembers()
        members.sort(key=calculateDaysTillBirthday)
        return [self.__mapper.toMemberDTO(member) for member in members]

