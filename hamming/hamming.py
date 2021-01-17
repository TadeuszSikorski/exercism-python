def distance(strand_a: str, strand_b: str) -> int:
    distance = 0

    if len(strand_a) != len(strand_b):
        raise ValueError("Sequences are different")
    else:
        for a, b in zip(strand_a, strand_b):
            if a != b:
                distance += 1

    return distance
