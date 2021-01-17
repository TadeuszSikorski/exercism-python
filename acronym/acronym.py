import re


def abbreviate(words: str) -> str:
    acronym = ""

    for word in re.findall(r"[A-Z0-9]+'?[A-Z]*(?<!')", words.upper()):
        acronym += word[0]

    return acronym
