
"""
A simple inventory management system module.

This module allows for adding, removing, and querying item quantities,
as well as loading from and saving to a JSON file.
"""

import json
from datetime import datetime
from typing import Dict, List

# Logging is not strictly needed for this file's logic once print is used,
# but it's often imported in real-world scenarios. Removed for Pylint strictness.

def add_item(inventory: Dict[str, int], item: str, qty: int) -> None:
    """
    Add a specified quantity of an item to the inventory.

    Args:
        inventory (Dict[str, int]): The inventory dictionary to modify.
        item (str): The name of the item to add.
        qty (int): The quantity to add.
    """
        # Input Validation: Prevents TypeError
    if not isinstance(item, str) or not isinstance(qty, int):
        print(f"Error: Invalid types for item ({type(item)}) or qty ({type(qty)}).")
        return
    inventory[item] = inventory.get(item, 0) + qty
    # E501: Line is compliant
    print(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(inventory: Dict[str, int], item: str, qty: int) -> None:
    """
    Remove a specified quantity of an item from the inventory.

    Args:
        inventory (Dict[str, int]): The inventory dictionary to modify.
        item (str): The name of the item to remove.
        qty (int): The quantity to remove.
    """
    if item not in inventory:
        print(f"Warning: Item '{item}' not in stock. Cannot remove.")
        return

    try:
        inventory[item] -= qty
        if inventory[item] <= 0:
            del inventory[item]
            print(f"Removed all of item '{item}'.")
        else:
            print(f"Removed {qty} of '{item}'. New total: {inventory[item]}")
    # FIX: Catch a more specific error than just TypeError/ValueError
    except (TypeError, ValueError):
        print(f"Error: Invalid quantity '{qty}' for item '{item}'.")


def get_qty(inventory: Dict[str, int], item: str) -> int:
    """
    Get the current quantity of a specific item.

    Args:
        inventory (Dict[str, int]): The inventory dictionary.
        item (str): The name of the item to query.

    Returns:
        int: The quantity of the item, or 0 if not found.
    """
    return inventory.get(item, 0)


def load_data(filename: str = "inventory.json") -> Dict[str, int]:
    """
    Load inventory data from a JSON file.

    Args:
        filename (str): The name of the file to load.

    Returns:
        Dict[str, int]: The loaded inventory dictionary.
    """
    try:
        # W1514: Added encoding="utf-8"
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Add a check to ensure data is in the expected format
            if not isinstance(data, dict):
                print("Error: Data in file is not a dictionary. Starting fresh.")
                return {}
            return data
    except FileNotFoundError:
        # E501: Line broken for compliance
        print(f"Warning: Data file '{filename}' not found. "
              "Starting fresh inventory.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{filename}'. Starting fresh.")
        return {}


def save_data(inventory: Dict[str, int], filename: str = "inventory.json") -> None:
    """
    Save the current inventory data to a JSON file.

    Args:
        inventory (Dict[str, int]): The inventory dictionary to save.
        filename (str): The name of the file to save to.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(inventory, f, indent=4)
        print(f"Inventory saved to {filename}.")
    except IOError as e:
        print(f"Error saving data to {filename}: {e}")


def print_data(inventory: Dict[str, int]) -> None:
    """
    Print a report of all items and their quantities.

    Args:
        inventory (Dict[str, int]): The inventory to print.
    """
    print("\n--- Items Report ---")
    if not inventory:
        print("Inventory is empty.")
    else:
        for item, qty in inventory.items():
            print(f"{item} -> {qty}")
    print("--------------------\n")


def check_low_items(inventory: Dict[str, int], threshold: int = 5) -> List[str]:
    """
    Return a list of items with quantities below the threshold.

    Args:
        inventory (Dict[str, int]): The inventory to check.
        threshold (int): The low-stock threshold.

    Returns:
        List[str]: A list of item names that are low in stock.
    """
    # This is a more "Pythonic" way to build the list (list comprehension)
    return [item for item, qty in inventory.items() if qty < threshold]


def main() -> None:
    """
    Main function to run the inventory management program.
    """
    # FIX: stock_data is now a local variable, initialized by load_data()
    stock_data = load_data()

    # Pass stock_data as the first argument to all functions
    add_item(stock_data, "apple", 10)
    add_item(stock_data, "banana", 2)
    add_item(stock_data, 123, "ten")  # Safely handled by type check
    remove_item(stock_data, "apple", 3)
    remove_item(stock_data, "orange", 1)  # Safely handled

    print(f"Apple stock: {get_qty(stock_data, 'apple')}")

    low_items = check_low_items(stock_data)
    print(f"Low items: {low_items}")

    print_data(stock_data)
    save_data(stock_data)
    print("Program finished.")


# FIX: Use a standard __name__ == "__main__" guard.
if __name__ == "__main__":
    main()
# This command reads the file, removes trailing spaces/tabs,
# and writes the result back to the same file.
