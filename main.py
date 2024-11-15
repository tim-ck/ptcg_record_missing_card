from card_manager import (
    add_missing_cards,
    assign_packs_to_missing_cards,
    change_card_pack,
    remove_card,
    read_results
)

def main():
    while True:
        print("\nSelect an action:")
        print("1. Add missing cards")
        print("2. Assign packs to missing cards")
        print("3. Remove a missing card")
        print("4. Change or add which pack a card belongs to")
        print("5. Read results")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_missing_cards()
        elif choice == '2':
            assign_packs_to_missing_cards()
        elif choice == '3':
            remove_card()
        elif choice == '4':
            change_card_pack()
        elif choice == '5':
            read_results()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()