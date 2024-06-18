from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from starlette.middleware.cors import CORSMiddleware

from DTOs.Member import MemberCreate
from Model import model
from Model.DatabaseSetup import engine
from Service.MemberService import MemberService

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    f"http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memberService = MemberService()


@app.get("/members")
def getMembers():
    try:
        return memberService.getMembers()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/members", status_code=201)
def addMember(member: MemberCreate):
    try:
        return memberService.addMember(member)
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail="Integrity constraint violation")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/members/sorted")
def getMembersSorted():
    try:
        return memberService.getMembersSorted()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
