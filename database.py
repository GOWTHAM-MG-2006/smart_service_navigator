# ============================================================
# MODULE: database.py
# Concepts: Dictionary, List, Data Structures
# ============================================================

from service import DrivingLicense, Passport, IncomeCertificate, RationCard

# ── Service Registry (Dictionary Data Structure) ───────────
SERVICE_DB: dict = {
    "1": DrivingLicense(),
    "2": Passport(),
    "3": IncomeCertificate(),
    "4": RationCard(),
}

# ── Application Records (Dictionary) ───────────────────────
application_records: dict = {}

# ── Application Counter ─────────────────────────────────────
_app_counter: list = [100]  # Using list so mutable inside functions


def generate_app_id() -> str:
    """Generate sequential application IDs like APP101, APP102 ..."""
    _app_counter[0] += 1
    return f"APP{_app_counter[0]}"


def save_application(app_id: str, record: dict):
    """Save an application to the in-memory database."""
    application_records[app_id] = record


def get_application(app_id: str) -> dict | None:
    """Retrieve an application by ID."""
    return application_records.get(app_id, None)


def get_all_applications() -> dict:
    """Return all saved applications."""
    return application_records


def get_service(key: str):
    """Return a service object by menu key."""
    return SERVICE_DB.get(key, None)


def get_all_services() -> dict:
    return SERVICE_DB
