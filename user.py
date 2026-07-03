# ============================================================
# MODULE: user.py
# Concepts: Class, Object, Constructor, Encapsulation
# ============================================================

class User:
    """Represents a registered citizen."""

    def __init__(self, name: str, age: int, district: str):
        # Encapsulation: private attributes
        self.__name = name
        self.__age = age
        self.__district = district
        self.__user_id = self._generate_id()

    def _generate_id(self) -> str:
        """Generate a unique citizen ID from name and age."""
        prefix = self.__name[:3].upper()
        return f"CIT-{prefix}{self.__age:02d}"

    # Getters (Encapsulation: controlled access)
    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def get_district(self) -> str:
        return self.__district

    def get_user_id(self) -> str:
        return self.__user_id

    def display_profile(self):
        print("\n" + "=" * 40)
        print("        CITIZEN PROFILE")
        print("=" * 40)
        print(f"  Citizen ID : {self.__user_id}")
        print(f"  Name       : {self.__name.title()}")
        print(f"  Age        : {self.__age}")
        print(f"  District   : {self.__district.title()}")
        print("=" * 40)
