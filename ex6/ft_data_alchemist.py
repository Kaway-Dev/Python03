import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players: list[str] = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]

    all_cap: list[str] = [name.capitalize() for name in players]
    cap_only: list[str] = [name for name in players if name[0].isupper()]

    score_dict: dict[str, int] = {
        name: random.randint(1, 1000) for name in all_cap
    }

    avg: float = round(sum(score_dict.values()) / len(score_dict), 2)

    high_scores: dict[str, int] = {
        name: score for name, score in score_dict.items() if score > avg
    }

    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {all_cap}")
    print(f"New list of capitalized names only: {cap_only}")
    print(f"Score dict: {score_dict}")
    print(f"Score average is {avg}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
