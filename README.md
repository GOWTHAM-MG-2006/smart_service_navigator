# Smart Public Service Navigator

A console-based Python application simulating a government public service portal for Indian citizens to apply for various government services.

---

## Project Structure

```
smart_service_navigator/
│
├── main.py              # Entry point — registration + main menu loop
├── user.py              # User class (citizen profile)
├── service.py           # GovernmentService base + 4 service subclasses
├── database.py          # In-memory data store (dict-based)
├── navigator.py         # Core orchestrator — all workflows
├── utils.py             # String utils, Stack, Recursion, UI helpers
├── test_run.py          # Automated test script (all 9 features)
└── __pycache__/         # Python bytecode cache
```

---

## Module Descriptions

### `main.py` (Entry Point)
- `register_user()` — Collects citizen name, age, district; creates `User` object
- `main_menu()` — Displays 10-option menu and routes to `Navigator` methods
- `main()` — Bootstraps the application

### `user.py` (User Model)
- **Class:** `User`
- **Attributes:** `__name`, `__age`, `__district`, `__user_id` (all private — encapsulation)
- **Methods:** `get_name()`, `get_age()`, `get_district()`, `get_user_id()`, `display_profile()`
- **ID Format:** `CIT-{first 3 chars of name}{age:02d}` (e.g., `CIT-RAH25`)

### `service.py` (Service Hierarchy)
- **Base Class:** `GovernmentService` (abstract)
  - Attributes: `_name`, `_department`, `_fee`, `_processing_days`
  - Methods: `show_details()` (overridden), `get_name()`, `get_fee()`, `get_department()`, `get_processing_days()`
- **Subclasses:**

| Class | Service | Dept | Fee | Days |
|-------|---------|------|-----|------|
| `DrivingLicense` | Driving License | RTO | ₹200 | 30 |
| `Passport` | Passport | Passport Seva Kendra | ₹1500 | 45 |
| `IncomeCertificate` | Income Certificate | Tehsildar Office | ₹50 | 15 |
| `RationCard` | Ration Card | Food & Civil Supplies | ₹0 | 20 |

- Each subclass overrides `show_details()` (polymorphism) and has `get_required_docs()`

### `database.py` (In-Memory Store)
- **`SERVICE_DB`** — Dictionary mapping menu keys `"1"`–`"4"` to service objects
- **`application_records`** — Dictionary storing submitted applications by app ID
- **`_app_counter`** — Mutable list `[100]` for sequential ID generation (`APP101`, `APP102`, ...)
- Functions: `generate_app_id()`, `save_application()`, `get_application()`, `get_all_applications()`, `get_service()`, `get_all_services()`

### `navigator.py` (Core Orchestrator)
- **Class:** `Navigator`
- **Composition:** Uses `User` and `DocumentStack` internally
- **Methods:**

| Method | Feature | Concepts Used |
|--------|---------|---------------|
| `show_service_menu()` | Display all services | Dictionary iteration |
| `select_service()` | View service details | Polymorphism |
| `manage_documents()` | Upload/manage docs | Stack (push/pop), Recursion |
| `submit_application()` | Submit application | Recursive doc check, Dictionary save |
| `track_application()` | Track app status | Dictionary lookup |
| `show_guidance()` | Step-by-step guidance | Recursion, String comparison |
| `search_services()` | Search by keyword | Recursion + Strings |
| `show_all_applications()` | View all apps | Dictionary iteration |
| `string_demo()` | String method showcase | String operations |

### `utils.py` (Utilities)

#### String Functions
| Function | Description |
|----------|-------------|
| `clean_input(text)` | Strip + lowercase + remove double spaces |
| `format_title(text)` | Title-case conversion |
| `count_vowels(text)` | Count vowels in string |
| `mask_id(user_id)` | Mask middle chars (e.g., `CIT-RAH25` → `CIT******25`) |
| `words_in_name(full_name)` | Split name into word list |
| `join_with_dash(words)` | Join words with `-` |
| `search_keyword(text, keyword)` | Case-insensitive substring search |

#### `DocumentStack` Class (Stack Data Structure)
| Method | Description |
|--------|-------------|
| `push(document)` | Add document to top of stack |
| `pop()` | Remove and return top document (undo) |
| `peek()` | View top document without removing |
| `is_empty()` | Check if stack is empty |
| `size()` | Return number of documents |
| `get_all()` | Return copy of all documents |
| `display()` | Print all documents (top to bottom) |

#### Recursive Functions
| Function | Description |
|----------|-------------|
| `display_steps(steps, index)` | Recursively print application steps with delay |
| `recursive_doc_check(required, uploaded, index, missing)` | Recursively find missing documents |
| `recursive_search(services, keyword, index, results)` | Recursively filter services by keyword |

#### UI Helpers
| Function | Description |
|----------|-------------|
| `print_banner()` | Print application banner |
| `print_divider()` | Print visual divider line |
| `pause()` | Wait for ENTER key |

### `test_run.py` (Automated Test)
- Tests all 9 features without user interaction
- Creates a hardcoded user, exercises all services, stack operations, recursion, and string demos
- **Note:** Contains hardcoded path — may need adjustment on other machines

---

## CS Concepts Demonstrated

| Concept | Where Used |
|---------|------------|
| **Classes & Objects** | `User`, `Navigator`, `DocumentStack`, `GovernmentService` |
| **Inheritance** | `DrivingLicense`, `Passport`, `IncomeCertificate`, `RationCard` extend `GovernmentService` |
| **Polymorphism** | `show_details()` overridden in each service subclass |
| **Encapsulation** | Private attributes (`__name`, `__stack`) with getter methods |
| **Abstraction** | `GovernmentService` as abstract base class |
| **Composition** | `Navigator` contains `User` and `DocumentStack` |
| **Stack (LIFO)** | `DocumentStack` for document upload/undo |
| **Dictionary** | `SERVICE_DB`, `application_records` for O(1) lookups |
| **Recursion** | `display_steps()`, `recursive_doc_check()`, `recursive_search()` |
| **String Methods** | `.lower()`, `.upper()`, `.title()`, `.split()`, `.join()`, `.replace()`, `.count()`, `.startswith()`, slicing |
| **Modules** | Clean separation across 6 Python files |

---

## Running the Application

```bash
# Interactive mode
python main.py

# Automated test (no user input needed)
python test_run.py
```

---

## Requirements

- Python 3.10+ (uses `str | None` union type syntax)
- No external dependencies — pure Python standard library

---

## Menu Options

| Key | Action |
|-----|--------|
| 1 | View All Services |
| 2 | Service Details |
| 3 | Upload Documents (Stack Demo) |
| 4 | Submit Application |
| 5 | Track Application |
| 6 | Application Guidance (Recursion Demo) |
| 7 | Search Services (Recursion + Strings) |
| 8 | View All My Applications |
| 9 | String Concepts Demo |
| 0 | Exit |
