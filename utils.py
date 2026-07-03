# ============================================================
# MODULE: utils.py
# Concepts: Strings, Stack Data Structure, Recursion
# ============================================================

import time


# ══════════════════════════════════════════════════════════
# STRING UTILITIES
# ══════════════════════════════════════════════════════════

def clean_input(text: str) -> str:
    """Remove extra spaces and lowercase — String Manipulation."""
    return text.strip().lower().replace("  ", " ")


def format_title(text: str) -> str:
    """Title-case a string — String Manipulation."""
    return text.title()


def count_vowels(text: str) -> int:
    """Count vowels using string methods — String Concept."""
    vowels = "aeiouAEIOU"
    return sum(text.count(v) for v in vowels)


def mask_id(user_id: str) -> str:
    """Mask middle characters of ID — String Slicing."""
    if len(user_id) <= 4:
        return user_id
    return user_id[:3] + "*" * (len(user_id) - 5) + user_id[-2:]


def words_in_name(full_name: str) -> list:
    """Split name into word list — String split()."""
    return full_name.strip().split()


def join_with_dash(words: list) -> str:
    """Join words using dash — String join()."""
    return "-".join(words)


def search_keyword(text: str, keyword: str) -> bool:
    """Case-insensitive keyword search in a string."""
    return keyword.lower() in text.lower()


# ══════════════════════════════════════════════════════════
# STACK DATA STRUCTURE
# ══════════════════════════════════════════════════════════

class DocumentStack:
    """
    Stack for managing document uploads.
    Supports push (add), pop (undo), and peek.
    Data Structure: Stack (LIFO — Last In First Out)
    """

    def __init__(self):
        self.__stack: list = []   # Internal list as stack storage

    def push(self, document: str):
        """Add a document to the stack."""
        self.__stack.append(document.lower().strip())
        print(f"\n  [+] Document Added  : {document.title()}")

    def pop(self) -> str | None:
        """Remove the last added document (undo)."""
        if self.is_empty():
            print("\n  [!] No documents to remove.")
            return None
        removed = self.__stack.pop()
        print(f"\n  [-] Removed (Undo)  : {removed.title()}")
        return removed

    def peek(self) -> str | None:
        """See the last uploaded document without removing."""
        if self.is_empty():
            return None
        return self.__stack[-1]

    def is_empty(self) -> bool:
        return len(self.__stack) == 0

    def size(self) -> int:
        return len(self.__stack)

    def get_all(self) -> list:
        return list(self.__stack)

    def display(self):
        print("\n  -- Uploaded Documents --")
        if self.is_empty():
            print("  (none)")
        else:
            for i, doc in enumerate(reversed(self.__stack), 1):
                print(f"  {i}. {doc.title()}")


# ══════════════════════════════════════════════════════════
# RECURSION
# ══════════════════════════════════════════════════════════

def display_steps(steps: list, index: int = 0):
    """
    Recursively display application steps.
    Concept: Recursion (Base case + Recursive call)
    """
    if index == len(steps):          # Base case
        return
    print(f"\n  Step {index + 1}: {steps[index]}")
    time.sleep(0.3)
    display_steps(steps, index + 1)  # Recursive call


def recursive_doc_check(required: list, uploaded: list, index: int = 0, missing: list = None) -> list:
    """
    Recursively check which required documents are missing.
    Concept: Recursion
    """
    if missing is None:
        missing = []
    if index == len(required):       # Base case
        return missing
    if required[index] not in uploaded:
        missing.append(required[index])
    return recursive_doc_check(required, uploaded, index + 1, missing)  # Recursive call


def recursive_search(services: list, keyword: str, index: int = 0, results: list = None) -> list:
    """
    Recursively search services list for a keyword.
    Concept: Recursion + Strings
    """
    if results is None:
        results = []
    if index == len(services):       # Base case
        return results
    if keyword.lower() in services[index].lower():
        results.append(services[index])
    return recursive_search(services, keyword, index + 1, results)  # Recursive call


# ══════════════════════════════════════════════════════════
# UI HELPERS
# ══════════════════════════════════════════════════════════

def print_banner():
    print("\n" + "+" + "=" * 48 + "+")
    print("|    SMART PUBLIC SERVICE NAVIGATOR v1.0     |")
    print("|        Government of India -- Console App   |")
    print("+" + "=" * 48 + "+")


def print_divider():
    print("\n" + "--" * 25)


def pause():
    input("\n  Press ENTER to continue...")
