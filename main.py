from cli import play_round
from storage import save_score, get_top_scores


def show_menu():
    print()
    print("=== Word Guess Game ===")
    print("1. Play a round")
    print("2. View top scores")
    print("3. Exit")


def view_scores():
    print()
    print("Top scores:")
    top = get_top_scores()
    if not top:
        print("No scores yet.")
    for entry in top:
        print(f"{entry['name']}: {entry['points']}")


def main():
    name = input("Enter your name: ")

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            points = play_round()
            print(f"You scored {points} points.")
            save_score(name, points)
        elif choice == "2":
            view_scores()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()