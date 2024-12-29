import datetime


def is_adult(user_birth):
    user_birth_to_date = datetime.datetime.strptime(user_birth, "%Y-%m-%d")
    today = datetime.datetime.today()
    if 105 >= (int((today - user_birth_to_date).days) // 365) >= 18:
        return True
    else:
        return False
