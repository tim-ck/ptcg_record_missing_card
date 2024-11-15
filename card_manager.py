import os

DATA_DIR = 'data'
INDEX_FILE_PATH = os.path.join(DATA_DIR, 'card_index.txt')
LOOKUP_FILE_PATH = os.path.join(DATA_DIR, 'card_lookup.txt')

def load_lookup_table():
    lookup = {}
    if os.path.exists(LOOKUP_FILE_PATH):
        with open(LOOKUP_FILE_PATH, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if parts:
                    card_index = parts[0]
                    packs = parts[1:]
                    lookup[card_index] = packs
    return lookup

def save_lookup_table(lookup):
    with open(LOOKUP_FILE_PATH, 'w') as file:
        for card_index, packs in lookup.items():
            file.write(f"{card_index} {' '.join(packs)}\n")

def load_card_index():
    cards = []
    if os.path.exists(INDEX_FILE_PATH):
        with open(INDEX_FILE_PATH, 'r') as file:
            for line in file:
                card_index = line.strip()
                if card_index:
                    cards.append(card_index)
    return cards

def save_card_index(cards):
    with open(INDEX_FILE_PATH, 'w') as file:
        for card_index in cards:
            file.write(f"{card_index}\n")

def insertion_sort(cards):
    for i in range(1, len(cards)):
        key = cards[i]
        j = i - 1
        while j >= 0 and int(cards[j]) > int(key):
            cards[j + 1] = cards[j]
            j -= 1
        cards[j + 1] = key
    return cards

def add_missing_cards():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    lookup = load_lookup_table()
    cards = load_card_index()
    while True:
        card_input = input("Enter the missing card index (or 'stop' to finish): ")
        if card_input.lower() == 'stop':
            break
        elif '-' in card_input:
            try:
                start, end = map(int, card_input.split('-'))
                for i in range(start, end + 1):
                    card_index = str(i)
                    if card_index not in cards:
                        cards.append(card_index)
                        if card_index not in lookup:
                            assign_pack_to_card(lookup, card_index)
                    else:
                        print(f"Card {card_index} is already in the missing list.")
            except ValueError:
                print("Invalid range format. Please enter a valid range (e.g., 1-5).")
        else:
            card_index = card_input
            if card_index not in cards:
                cards.append(card_index)
                if card_index not in lookup:
                    assign_pack_to_card(lookup, card_index)
            else:
                print(f"Card {card_index} is already in the missing list.")
    cards = insertion_sort(cards)  # Sort the cards after adding new ones
    save_card_index(cards)
    save_lookup_table(lookup)
    print("Missing cards have been updated.")

def assign_pack_to_card(lookup, card_index):
    if card_index in lookup:
        print(f"Card {card_index} is already assigned to pack(s): {', '.join(lookup[card_index])}")
    else:
        while True:
            pack_input = input(f"Which pack does card {card_index} belong to? Enter pack numbers separated by spaces (1/2/3): ")
            packs = pack_input.strip().split()
            if all(pack in ['1', '2', '3'] for pack in packs):
                lookup[card_index] = packs
                break
            else:
                print("Invalid input. Please enter pack numbers (1, 2, or 3) separated by spaces.")
    print(f"Card {card_index} assigned to pack(s): {', '.join(lookup[card_index])}")

def assign_packs_to_missing_cards():
    lookup = load_lookup_table()
    cards = load_card_index()
    updated = False
    for card_index in cards:
        if card_index not in lookup:
            assign_pack_to_card(lookup, card_index)
            updated = True
    if updated:
        save_lookup_table(lookup)
        print("Lookup table has been updated with pack numbers.")
    else:
        print("All missing cards have assigned pack numbers.")

def change_card_pack():
    lookup = load_lookup_table()
    while True:
        card_index = input("Enter the card index to change pack(s) (or 'stop' to finish): ")
        if card_index.lower() == 'stop':
            break
        if card_index in lookup:
            print(f"Current pack(s) for card {card_index}: {', '.join(lookup[card_index])}")
        else:
            print(f"Card {card_index} is not in the lookup table.")
        assign_pack_to_card(lookup, card_index)
        save_lookup_table(lookup)
        print(f"Pack(s) for card {card_index} have been updated.")

def remove_card():
    cards = load_card_index()
    while True:
        card_to_remove = input("Enter the card index to remove (or 'stop' to finish): ")
        if card_to_remove.lower() == 'stop':
            break
        if card_to_remove in cards:
            cards.remove(card_to_remove)
            save_card_index(cards)
            print(f"Card '{card_to_remove}' removed from missing cards.")
        else:
            print(f"Card '{card_to_remove}' is not in the missing list.")

def read_results():
    lookup = load_lookup_table()
    cards = load_card_index()
    pack_counts = {1: 0, 2: 0, 3: 0}
    for card_index in cards:
        packs = lookup.get(card_index, [])
        for pack in packs:
            pack_counts[int(pack)] += 1
    print("\nMissing cards per pack:")
    for pack_num in sorted(pack_counts.keys()):
        print(f"Pack {pack_num}: {pack_counts[pack_num]} missing cards")
    total_missing = len(cards)
    print(f"\nTotal missing cards: {total_missing}")

def list_missing_cards():
    cards = load_card_index()
    if cards:
        cards = insertion_sort(cards)  # Ensure the list is sorted before printing
        print("Missing cards:")
        print(' '.join(cards))
    else:
        print("No missing cards.")