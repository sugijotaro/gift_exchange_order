import time
import random
from math import gcd


def has_common_factor(x, y):
    return any(gcd(x, y) % factor == 0 for factor in (2, 3, 5, 7))


def validate_sequence(participants):
    for i in range(len(participants)):
        if not has_common_factor(
            participants[i], participants[(i + 1) % len(participants)]
        ):
            return False
    return True


def adjust_sequence(participants):
    for i in range(len(participants) - 1):
        if not has_common_factor(participants[i], participants[i + 1]):
            for j in range(i + 2, len(participants)):
                if has_common_factor(participants[i], participants[j]):
                    participants[i + 1], participants[j] = (
                        participants[j],
                        participants[i + 1],
                    )
                    break
            else:
                return False
    return has_common_factor(participants[-1], participants[0])


def find_valid_order(participants, max_attempts=10):
    for attempt in range(max_attempts):
        print(f"Attempt {attempt + 1}...")
        random.shuffle(participants)

        if adjust_sequence(participants) and validate_sequence(participants):
            print("A valid order has been found!")
            return participants
        else:
            print("Attempt failed. Retrying...")

    print("No valid order found after maximum attempts.")
    return None


if __name__ == "__main__":
    participants = [30, 75, 20, 45, 50, 90]

    ordered_participants = find_valid_order(participants)

    if ordered_participants:
        for participant in ordered_participants:
            print(participant)
    else:
        print("No valid order found.")
