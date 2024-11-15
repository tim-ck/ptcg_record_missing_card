# Card Manager

This project is a simple card management system that allows you to manage missing cards, assign packs to cards, and view the results.

## Features

- Add missing cards
- Assign packs to missing cards
- Remove a missing card
- Change or add which pack a card belongs to
- Read results of missing cards per pack

## Files

- `card_manager.py`: Contains the main logic for managing cards.
- `main.py`: Entry point for the application.
- `card_index.txt`: Stores the list of missing card indices.
- `card_lookup.txt`: Stores the mapping of card indices to packs.

## Usage

1. Run the application:
    ```sh
    python main.py
    ```

2. Follow the on-screen prompts to manage your cards.

## Functions

### card_manager.py

- `load_lookup_table()`: Loads the lookup table from `card_lookup.txt`.
- `save_lookup_table(lookup)`: Saves the lookup table to `card_lookup.txt`.
- `load_card_index()`: Loads the card index from `card_index.txt`.
- `save_card_index(cards)`: Saves the card index to `card_index.txt`.
- `insertion_sort(cards)`: Sorts the list of cards using insertion sort.
- `add_missing_cards()`: Adds missing cards to the index.
- `assign_pack_to_card(lookup, card_index)`: Assigns a pack to a card.
- `assign_packs_to_missing_cards()`: Assigns packs to all missing cards.
- `change_card_pack()`: Changes the pack assignment for a card.
- `remove_card()`: Removes a card from the missing list.
- `read_results()`: Reads and displays the results of missing cards per pack.
- `list_missing_cards()`: Lists all missing cards.

### main.py

- `main()`: Main function to run the application.

## License

This project is licensed under the MIT License.