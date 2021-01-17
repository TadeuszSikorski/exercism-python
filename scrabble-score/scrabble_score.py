LETTERS_AND_SCORES = {
    1: "A, E, I, O, U, L, N, R, S, T",
    2: "D, G",
    3: "B, C, M, P",
    4: "F, H, V, W, Y",
    5: "K",
    8: "J, X",
    10: "Q, Z",
}

LETTERS_TO_SCORES = {
    letter: score
    for score, letters in LETTERS_AND_SCORES.items()
    for letter in letters.split(", ")
}


def score(word: str) -> int:
    final_score: int = 0

    for character in word.upper():
        final_score += LETTERS_TO_SCORES[character]

    return final_score
