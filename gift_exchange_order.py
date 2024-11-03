from math import gcd
from itertools import permutations


def has_common_factor(x, y):
    return any(gcd(x, y) % factor == 0 for factor in (2, 3, 5))


def find_order(participants):
    for perm in permutations(participants):
        if all(
            has_common_factor(perm[i], perm[(i + 1) % len(perm)])
            for i in range(len(perm))
        ):
            return perm
    return None


if __name__ == "__main__":
    participants = [
        210,
        330,
        78,
        51,
        114,
        69,
        870,
        930,
        555,
        246,
        645,
        1410,
        159,
        1770,
        1830,
        2010,
        426,
        1095,
        395,
        2490,
        1335,
        1455,
        606,
        618,
        535,
        545,
        565,
        635,
        393,
        411,
        278,
        298,
    ]

    ordered_participants = find_order(participants)

    if ordered_participants:
        for participant in ordered_participants:
            print(participant)
    else:
        print("No valid order found.")
