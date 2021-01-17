def is_isogram(string: str) -> bool:
    if len(string) > 0:
        string = string.lower()
    else:
        return True

    for letter in string:
        if string.count(letter) > 1 and letter.isalpha():
            return False

    return True

