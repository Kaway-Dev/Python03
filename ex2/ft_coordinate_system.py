import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw_input: str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        try:
            x_str, y_str, z_str = raw_input.split(",")
        except ValueError:
            print("Invalid syntax")
            continue

        clean_parts: list[str] = [
            x_str.strip(), y_str.strip(), z_str.strip()
        ]
        floats: list[float] = []
        error_found: bool = False

        for part in clean_parts:
            try:
                floats.append(float(part))
            except ValueError as err:
                print(f"Error on parameter '{part}': {err}")
                error_found = True
                break

        if not error_found:
            return (floats[0], floats[1], floats[2])


def calculate_distance(
    pos1: tuple[float, float, float], pos2: tuple[float, float, float]
) -> float:
    dx: float = pos2[0] - pos1[0]
    dy: float = pos2[1] - pos1[1]
    dz: float = pos2[2] - pos1[2]
    return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    dist_center: float = round(calculate_distance((0.0, 0.0, 0.0), pos1), 4)
    print(f"Distance to center: {dist_center}")
    print()
    print("Get a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()
    dist_between: float = round(calculate_distance(pos1, pos2), 4)
    print(f"Distance between the 2 sets of coordinates: {dist_between}")


if __name__ == "__main__":
    main()
