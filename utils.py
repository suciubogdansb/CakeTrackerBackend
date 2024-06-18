from datetime import date


def calculateDaysTillBirthday(birthday: date):
    today = date.today()
    birthday = birthday.replace(year=today.year)
    if today > birthday:
        birthday = birthday.replace(year=today.year + 1)
    return (birthday - today).days