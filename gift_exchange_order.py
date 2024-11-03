import time
import random
from math import gcd
from itertools import permutations


def has_common_factor(x, y):
    return any(gcd(x, y) % factor == 0 for factor in (2, 3, 5))


def find_order(participants, max_duration=10):
    print("Processing started...")
    start_time = time.time()

    random.shuffle(participants)

    for perm in permutations(participants):
        if time.time() - start_time > max_duration:
            print("Processing took too long. It is likely impossible.")
            return None

        if all(
            has_common_factor(perm[i], perm[(i + 1) % len(perm)])
            for i in range(len(perm))
        ):
            print("A valid order has been found!")
            return perm

    print("No valid order found. It is likely impossible.")
    return None


if __name__ == "__main__":
    participants = [30, 75, 20, 45, 50, 90]

    ordered_participants = find_order(participants)

    if ordered_participants:
        for participant in ordered_participants:
            print(participant)
    else:
        print("No valid order found.")
