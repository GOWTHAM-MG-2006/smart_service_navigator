# ============================================================
# MODULE: service.py
# Concepts: Inheritance, Polymorphism, Method Overriding,
#           Abstraction, Encapsulation
# ============================================================


class GovernmentService:
    """Abstract Base Class for all government services."""

    def __init__(self, name: str, department: str, fee: int, days: int):
        self._name = name
        self._department = department
        self._fee = fee
        self._processing_days = days

    def show_details(self):
        """Abstract method — overridden in every child class."""
        pass

    def get_name(self) -> str:
        return self._name

    def get_fee(self) -> int:
        return self._fee

    def get_department(self) -> str:
        return self._department

    def get_processing_days(self) -> int:
        return self._processing_days

    def _print_header(self):
        print("\n" + "=" * 45)
        print(f"  SERVICE : {self._name.upper()}")
        print("=" * 45)
        print(f"  Department        : {self._department}")
        print(f"  Processing Fee    : Rs. {self._fee}")
        print(f"  Processing Time   : {self._processing_days} working days")


# ── Child Class 1 ─────────────────────────────────────────
class DrivingLicense(GovernmentService):
    """Driving Licence service (inherits GovernmentService)."""

    def __init__(self):
        super().__init__(
            name="Driving License",
            department="Regional Transport Office (RTO)",
            fee=200,
            days=30,
        )
        self.__required_docs = [
            "aadhaar card",
            "address proof",
            "passport photo",
            "age proof",
            "medical certificate",
        ]

    # Method Overriding — Polymorphism
    def show_details(self):
        self._print_header()
        print(f"  Eligibility       : Age 18+")
        print(f"  Test Required     : Yes (Written + Driving)")
        print("  Required Documents:")
        for doc in self.__required_docs:
            print(f"    - {doc.title()}")
        print("=" * 45)

    def get_required_docs(self):
        return self.__required_docs


# ── Child Class 2 ─────────────────────────────────────────
class Passport(GovernmentService):
    """Passport service (inherits GovernmentService)."""

    def __init__(self):
        super().__init__(
            name="Passport",
            department="Passport Seva Kendra",
            fee=1500,
            days=45,
        )
        self.__required_docs = [
            "aadhaar card",
            "address proof",
            "passport photo",
            "birth certificate",
            "10th marksheet",
        ]

    # Method Overriding — Polymorphism
    def show_details(self):
        self._print_header()
        print(f"  Eligibility       : All citizens")
        print(f"  Police Verify.    : Yes")
        print("  Required Documents:")
        for doc in self.__required_docs:
            print(f"    - {doc.title()}")
        print("=" * 45)

    def get_required_docs(self):
        return self.__required_docs


# ── Child Class 3 ─────────────────────────────────────────
class IncomeCertificate(GovernmentService):
    """Income Certificate service (inherits GovernmentService)."""

    def __init__(self):
        super().__init__(
            name="Income Certificate",
            department="Tehsildar Office",
            fee=50,
            days=15,
        )
        self.__required_docs = [
            "aadhaar card",
            "address proof",
            "passport photo",
            "salary slip or ration card",
        ]

    # Method Overriding — Polymorphism
    def show_details(self):
        self._print_header()
        print(f"  Eligibility       : All citizens")
        print(f"  Valid For         : 1 Year")
        print("  Required Documents:")
        for doc in self.__required_docs:
            print(f"    - {doc.title()}")
        print("=" * 45)

    def get_required_docs(self):
        return self.__required_docs


# ── Child Class 4 ─────────────────────────────────────────
class RationCard(GovernmentService):
    """Ration Card service (inherits GovernmentService)."""

    def __init__(self):
        super().__init__(
            name="Ration Card",
            department="Food & Civil Supplies Department",
            fee=0,
            days=20,
        )
        self.__required_docs = [
            "aadhaar card",
            "address proof",
            "passport photo",
            "family members aadhaar",
            "gas connection proof",
        ]

    # Method Overriding — Polymorphism
    def show_details(self):
        self._print_header()
        print(f"  Eligibility       : BPL / APL families")
        print(f"  Fee               : FREE")
        print(f"  Household Limit   : One per family")
        print("  Required Documents:")
        for doc in self.__required_docs:
            print(f"    - {doc.title()}")
        print("=" * 45)

    def get_required_docs(self):
        return self.__required_docs
