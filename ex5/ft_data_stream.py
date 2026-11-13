import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players: list[str] = ["alice", "bob", "charlie", "dylan"]
    actions: list[str] = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use",
    ]
    while True:
        name: str = random.choice(players)
        action: str = random.choice(actions)
        yield (name, action)


def consume_event(
    events_list: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while events_list:
        idx: int = random.randrange(len(events_list))
        event: tuple[str, str] = events_list.pop(idx)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    generator: typing.Generator[tuple[str, str], None, None] = gen_event()

    for i in range(1000):
        event: tuple[str, str] = next(generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    list_10: list[tuple[str, str]] = [next(generator) for _ in range(10)]
    print(f"Built list of 10 events: {list_10}")

    for event in consume_event(list_10):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {list_10}")


if __name__ == "__main__":
    main()
