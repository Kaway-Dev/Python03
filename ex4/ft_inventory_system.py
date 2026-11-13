import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        parts: list[str] = arg.split(":")
        if len(parts) != 2 or not parts[0]:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item: str = parts[0].strip()
        val_str: str = parts[1].strip()

        if not item:
            print(f"Error - invalid parameter '{arg}'")
            continue

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            qty: int = int(val_str)
            inventory[item] = qty
        except ValueError as err:
            print(f"Quantity error for '{item}': {err}")

    return inventory


def analyze_inventory(inventory: dict[str, int]) -> None:
    items_list: list[str] = list(inventory.keys())
    quantities: list[int] = list(inventory.values())
    total_qty: int = sum(quantities)

    print(f"Got inventory: {inventory}")
    print(f"Item list: {items_list}")
    print(f"Total quantity of the {len(items_list)} items: {total_qty}")

    for item in items_list:
        qty: int = inventory[item]
        pct: float = (
            round((qty / total_qty) * 100, 1) if total_qty > 0 else 0.0
        )
        print(f"Item {item} represents {pct:.1f}%")

    if items_list:
        most_item: str = items_list[0]
        least_item: str = items_list[0]
        for item in items_list:
            if inventory[item] > inventory[most_item]:
                most_item = item
            if inventory[item] < inventory[least_item]:
                least_item = item

        print(
            f"Item most abundant: {most_item} "
            f"with quantity {inventory[most_item]}"
        )
        print(
            f"Item least abundant: {least_item} "
            f"with quantity {inventory[least_item]}"
        )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    args: list[str] = sys.argv[1:]
    inventory: dict[str, int] = parse_inventory(args)
    analyze_inventory(inventory)


if __name__ == "__main__":
    main()
