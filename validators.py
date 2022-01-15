from functions import myAll


def check_grade(number):
    if number < 0 or number > 10:
        raise Exception
    return number


def name_is_valid(name):
    return myAll(lambda x: x.isalpha() or x == ' ', name)