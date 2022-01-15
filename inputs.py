from validators import check_grade, name_is_valid


def inputGrade(text) -> float:
    while True:
        try:
            n = check_grade(float(input(text)))
        except Exception:
            continue
        else:
            return n
        
        
def inputName(text) -> str:
    userInput = input(text).strip()
    if not name_is_valid(userInput) or len(userInput) == 0:
        return inputName(text)
    return userInput
    
        