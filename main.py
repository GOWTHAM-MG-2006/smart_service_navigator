# ============================================================
# MODULE: main.py
# Smart Public Service Navigator
# Concepts: All OOP, Strings, Stack, Recursion, Modules
# ============================================================

import sys
from user import User 
from navigator import Navigator
from utils import print_banner, print_divider, clean_input


def register_user() -> User:
    """Citizen registration — returns a User object."""
    print("\n" + "=" * 45)
    print("          CITIZEN REGISTRATION")
    print("=" * 45)

    while True:
        name = input("  Enter your Full Name     : ").strip()
        if name:
            break
        print("  [!] Name cannot be empty.")

    while True:
        age_str = input("  Enter your Age           : ").strip()
        if age_str.isdigit() and 5 <= int(age_str) <= 110:
            age = int(age_str)
            break
        print("  [!] Please enter a valid age (5-110).")

    district = input("  Enter your District      : ").strip()
    if not district:
        district = "Unknown"

    user = User(name, age, district)
    user.display_profile()
    return user


def main_menu(navigator: Navigator, user: User):
    """Main application menu loop."""
    while True:
        print("\n" + "=" * 45)
        print(f"  Welcome, {user.get_name().title()}  [{user.get_user_id()}]")
        print("=" * 45)
        print("  [1]  View All Services")
        print("  [2]  Service Details")
        print("  [3]  Upload Documents (Stack Demo)")
        print("  [4]  Application Guidance (Recursion Demo)")
        print("  [0]  Exit")
        print("--" * 22 + "-")

        choice = input("  Enter choice: ").strip()

        if choice == "1":
            navigator.show_service_menu()
            input("\n  Press ENTER to continue...")
        elif choice == "2":
            navigator.select_service()
        elif choice == "3":
            navigator.manage_documents()
        elif choice == "4":
            navigator.show_guidance()
        elif choice == "0":
            print("\n  Thank you for using Smart Public Service Navigator!")
            print("  Jai Hind!\n")
            sys.exit(0)
        else:
            print("\n  [!] Invalid option. Please choose 0-4.")


def main():
    print_banner()
    print("\n  Please register to use the service.")
    user = register_user()
    navigator = Navigator(user)
    main_menu(navigator, user)


if __name__ == "__main__":
    main()
