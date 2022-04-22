import pcbnew
import csv
import sqlite3

from dataclasses import dataclass

@dataclass
class InventoryItem:
    #item_type: str # resistor/etc
    value: int # ohms
    tolerance: int # percent tolerance
    current: float # current rating in W
    package: int # us package size (0805)
    quantity: int

def main():
    con = sqlite3.connect('example.db')

if __name__ == "__main__":
    main()
