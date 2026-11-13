import random

ACHIEVEMENTS: list[str] = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Speed Runner",
    "Unstoppable",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    count: int = random.randint(9, 10)
    chosen: list[str] = random.sample(ACHIEVEMENTS, count)
    return set(chosen)


def main() -> None:
    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()

    print("=== Achievement Tracker System ===")
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()

    all_distinct: set[str] = alice.union(bob, charlie, dylan)
    common: set[str] = alice.intersection(bob, charlie, dylan)

    print(f"All distinct achievements: {all_distinct}")
    print(f"Common achievements: {common}")
    print()

    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    print()

    total_pool: set[str] = set(ACHIEVEMENTS)
    print(f"Alice is missing: {total_pool.difference(alice)}")
    print(f"Bob is missing: {total_pool.difference(bob)}")
    print(f"Charlie is missing: {total_pool.difference(charlie)}")
    print(f"Dylan is missing: {total_pool.difference(dylan)}")


if __name__ == "__main__":
    main()
