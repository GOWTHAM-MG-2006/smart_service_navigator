# ============================================================
# MODULE: navigator.py
# Concepts: OOP, Strings, Stack, Recursion (via utils),
#           Dictionary lookups, Polymorphism usage
# ============================================================

import datetime
import database as db
from utils import (
    DocumentStack, clean_input, format_title, mask_id,
    words_in_name, join_with_dash, search_keyword,
    display_steps, recursive_doc_check, recursive_search,
    print_divider, pause
)


class Navigator:
    """
    Core Navigator class — orchestrates all service workflows.
    Uses composition with DocumentStack.
    """

    def __init__(self, user):
        self.__user = user                     # Composition with User
        self.__doc_stack = DocumentStack()     # Composition with Stack
        self.__current_service = None

    # ── 1. Show Service Menu ────────────────────────────────
    def show_service_menu(self):
        print("\n" + "=" * 45)
        print("       AVAILABLE GOVERNMENT SERVICES")
        print("=" * 45)
        for key, service in db.get_all_services().items():
            print(f"  [{key}] {service.get_name():<25} | Rs. {service.get_fee()}")
        print("  [0] Back to Main Menu")
        print("=" * 45)

    # ── 2. Select & Show Service Details ───────────────────
    def select_service(self):
        self.show_service_menu()
        choice = input("\n  Select service number: ").strip()
        service = db.get_service(choice)
        if service is None:
            print("\n  [!] Invalid choice.")
            return

        # Polymorphism: show_details() behaves differently per service
        service.show_details()
        self.__current_service = service
        pause()

    # ── 3. Document Upload with Stack ───────────────────────
    def manage_documents(self):
        """Upload and manage documents using Stack data structure."""
        self.show_service_menu()
        choice = input("\n  Select service to upload docs for: ").strip()
        service = db.get_service(choice)
        if service is None:
            print("\n  [!] Invalid service.")
            return

        self.__current_service = service
        required = service.get_required_docs()

        # Reset stack for fresh uploads
        self.__doc_stack = DocumentStack()

        while True:
            print_divider()
            print(f"\n  Service : {service.get_name()}")
            print("\n  Required Documents:")
            for i, doc in enumerate(required, 1):
                print(f"    {i}. {doc.title()}")

            self.__doc_stack.display()

            print("\n  Options:")
            print("  [A] Add Document")
            print("  [U] Undo Last Upload")
            print("  [C] Check Missing Documents")
            print("  [D] Done")

            action = clean_input(input("\n  Choose action: "))

            if action == "a":
                doc_name = input("  Enter document name: ")
                # String manipulation on input
                cleaned = clean_input(doc_name)
                self.__doc_stack.push(cleaned)

            elif action == "u":
                self.__doc_stack.pop()

            elif action == "c":
                uploaded = self.__doc_stack.get_all()
                # Recursion: check missing documents recursively
                missing = recursive_doc_check(required, uploaded)
                print("\n  ── Document Verification ──")
                if missing:
                    print("  Missing Documents:")
                    for m in missing:
                        print(f"    ✗ {m.title()}")
                else:
                    print("  ✓ All required documents uploaded!")

            elif action == "d":
                break

        pause()

    # ── 4. Application Submission ───────────────────────────
    def submit_application(self):
        """Submit application after document verification."""
        if self.__current_service is None:
            print("\n  [!] Please select a service first (Option 2).")
            pause()
            return

        uploaded = self.__doc_stack.get_all()
        required = self.__current_service.get_required_docs()

        # Recursive missing doc check
        missing = recursive_doc_check(required, uploaded)

        if missing:
            print("\n  [!] Cannot submit. Missing documents:")
            for m in missing:
                print(f"    ✗ {m.title()}")
            pause()
            return

        # Generate application ID
        app_id = db.generate_app_id()
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

        record = {
            "app_id": app_id,
            "citizen_id": self.__user.get_user_id(),
            "citizen_name": self.__user.get_name(),
            "service": self.__current_service.get_name(),
            "department": self.__current_service.get_department(),
            "fee": self.__current_service.get_fee(),
            "documents": uploaded,
            "status": "Submitted",
            "submitted_on": timestamp,
        }

        db.save_application(app_id, record)

        print("\n" + "=" * 45)
        print("      APPLICATION SUBMITTED SUCCESSFULLY")
        print("=" * 45)
        print(f"  Application ID   : {app_id}")
        print(f"  Service          : {self.__current_service.get_name()}")
        print(f"  Department       : {self.__current_service.get_department()}")
        print(f"  Fee Payable      : Rs. {self.__current_service.get_fee()}")
        print(f"  Submitted On     : {timestamp}")
        print(f"  Status           : Submitted ✓")
        print("=" * 45)
        print(f"\n  [Save your Application ID: {app_id}]")
        pause()

    # ── 5. Application Guidance with Recursion ──────────────
    def show_guidance(self):
        """Show step-by-step guidance using recursion."""
        self.show_service_menu()
        choice = input("\n  Select service for guidance: ").strip()
        service = db.get_service(choice)
        if service is None:
            print("\n  [!] Invalid choice.")
            return

        # Steps depend on service — string comparison
        name = service.get_name().lower()

        if "driving" in name:
            steps = [
                "Visit official RTO website or go to RTO office",
                "Fill Form LL (Learner's Licence application)",
                "Attach Aadhaar Card and Address Proof",
                "Pay fee of Rs. 200 at the counter",
                "Appear for Written Test at RTO",
                "Collect Learner's Licence (valid 6 months)",
                "Practice driving for minimum 30 days",
                "Appear for Driving Skill Test",
                "Permanent Driving Licence issued within 30 days",
            ]
        elif "passport" in name:
            steps = [
                "Register on Passport Seva Portal (passportindia.gov.in)",
                "Fill online application form",
                "Upload scanned documents",
                "Pay fee of Rs. 1500 online",
                "Book appointment at nearest Passport Seva Kendra",
                "Visit PSK on appointment date with originals",
                "Biometrics and document verification",
                "Police verification at your address",
                "Passport delivered to address within 45 days",
            ]
        elif "income" in name:
            steps = [
                "Visit local Tehsildar or Revenue office",
                "Collect application form (free of charge)",
                "Fill in family income details",
                "Attach Aadhaar Card and Ration Card",
                "Submit form with Rs. 50 stamp fee",
                "Officer will verify details",
                "Certificate issued within 15 working days",
            ]
        else:
            steps = [
                "Visit the Food & Civil Supplies Department",
                "Fill Ration Card application form",
                "Attach family Aadhaar cards and address proof",
                "Submit form to designated officer",
                "Field verification by inspector",
                "Ration Card issued within 20 working days",
            ]

        print(f"\n  ── Guidance for {service.get_name()} ──")
        print("  (Steps loaded using Recursion)\n")

        # RECURSION used here
        display_steps(steps)

        print("\n\n  ✓ End of Application Steps")
        pause()

    # ── 6. Application Tracking ─────────────────────────────
    def track_application(self):
        """Track application status using Dictionary lookup."""
        print_divider()
        app_id = input("\n  Enter Application ID (e.g. APP101): ").strip().upper()

        # Dictionary lookup
        record = db.get_application(app_id)

        if record is None:
            print(f"\n  [!] Application '{app_id}' not found.")
        else:
            print("\n" + "=" * 45)
            print("        APPLICATION STATUS REPORT")
            print("=" * 45)
            print(f"  Application ID  : {record['app_id']}")
            print(f"  Citizen ID      : {record['citizen_id']}")
            print(f"  Citizen Name    : {format_title(record['citizen_name'])}")
            print(f"  Service         : {record['service']}")
            print(f"  Department      : {record['department']}")
            print(f"  Fee Paid        : Rs. {record['fee']}")
            print(f"  Status          : {record['status']} ✓")
            print(f"  Submitted On    : {record['submitted_on']}")
            print("  Uploaded Docs   :")
            for doc in record['documents']:
                print(f"    - {doc.title()}")
            print("=" * 45)

        pause()

    # ── 7. Search Services ──────────────────────────────────
    def search_services(self):
        """Search services using recursive keyword search + string methods."""
        print_divider()
        keyword = input("\n  Enter keyword to search services: ").strip()

        service_names = [s.get_name() for s in db.get_all_services().values()]

        # Recursion: search recursively
        results = recursive_search(service_names, keyword)

        # String info
        print(f"\n  Keyword          : '{keyword}'")
        print(f"  Keyword (upper)  : '{keyword.upper()}'")
        print(f"  Character count  : {len(keyword)}")

        print(f"\n  Search Results for '{keyword}':")
        if results:
            for r in results:
                print(f"    ✓ {r}")
        else:
            print("    No services matched your keyword.")

        pause()

    # ── 8. All Applications ─────────────────────────────────
    def show_all_applications(self):
        """Show all submitted applications — Dictionary iteration."""
        all_apps = db.get_all_applications()
        print_divider()
        if not all_apps:
            print("\n  No applications submitted yet.")
        else:
            print(f"\n  Total Applications: {len(all_apps)}\n")
            for app_id, record in all_apps.items():
                print(f"  {app_id} | {record['service']:<22} | {record['citizen_name'].title()} | {record['status']}")
        pause()

    # ── 9. String Demo ──────────────────────────────────────
    def string_demo(self):
        """Showcase multiple String operations."""
        print_divider()
        print("\n  ── String Concepts Demo ──")
        sample = input("\n  Enter any text: ")

        print(f"\n  Original          : {sample}")
        print(f"  lower()           : {sample.lower()}")
        print(f"  upper()           : {sample.upper()}")
        print(f"  title()           : {sample.title()}")
        print(f"  strip()           : '{sample.strip()}'")
        print(f"  replace(' ','-')  : {sample.replace(' ', '-')}")
        print(f"  split()           : {sample.split()}")
        print(f"  len()             : {len(sample)}")
        print(f"  count('a')        : {sample.count('a')}")
        print(f"  Starts with 'A'?  : {sample.startswith('A')}")
        print(f"  join with '-'     : {join_with_dash(words_in_name(sample))}")
        pause()
