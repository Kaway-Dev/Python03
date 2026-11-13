import sys


def parse_command_line() -> None:
    print("=== Command Quest ===")
    program_name: str = sys.argv[0]
    args: list[str] = sys.argv[1:]
    total_args: int = len(sys.argv)

    print(f"Program name: {program_name}")
    if not args:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args)}")
    index: int = 0
    while index < len(args):
        print(f"Argument {index + 1}: {args[index]}")
        index += 1
    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    parse_command_line()
