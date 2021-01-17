def check_scores(scores: list):
    if not scores:
        raise Exception("List of scores is empty.")


def latest(scores: list) -> int:
    check_scores(scores)

    return scores[-1]


def personal_best(scores: list) -> int:
    check_scores(scores)

    return max(scores)


def personal_top_three(scores: list) -> list:
    check_scores(scores)

    return sorted(scores, reverse=True)[:3]
