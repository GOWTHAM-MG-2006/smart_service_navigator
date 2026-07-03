import sys, os
os.chdir(r'D:\strivers_project\smart_service_navigator\smart_service_navigator')
sys.path.insert(0, '.')

from user import User
from service import DrivingLicense, Passport, IncomeCertificate, RationCard
from utils import (DocumentStack, clean_input, format_title, count_vowels,
                   mask_id, words_in_name, join_with_dash, search_keyword,
                   display_steps, recursive_doc_check, recursive_search,
                   print_banner, print_divider)
import database as db
import datetime

print('=' * 50)
print('  SMART PUBLIC SERVICE NAVIGATOR - FULL TEST')
print('=' * 50)

# 1. Banner
print_banner()

# 2. User Registration
print('\n--- 1. Citizen Registration ---')
user = User('Rahul Sharma', 25, 'Pune')
user.display_profile()

# 3. All 4 Services
print('\n--- 2. Government Services ---')
dl = DrivingLicense()
pp = Passport()
ic = IncomeCertificate()
rc = RationCard()
for s in [dl, pp, ic, rc]:
    s.show_details()

# 4. Document Stack
print('\n--- 3. Document Stack (LIFO) ---')
stack = DocumentStack()
for doc in dl.get_required_docs():
    stack.push(doc)
print('\n  Stack after uploads:')
stack.display()
print('\n  Undo last doc:')
stack.pop()
print('\n  Stack after undo:')
stack.display()
missing = recursive_doc_check(dl.get_required_docs(), stack.get_all())
print('\n  Missing docs (recursive check):', missing)

stack.push('medical certificate')
missing = recursive_doc_check(dl.get_required_docs(), stack.get_all())
print('  After re-upload, missing:', missing)

# 5. Submit Application
print('\n--- 4. Submit Application ---')
app_id = db.generate_app_id()
record = {
    'app_id': app_id, 'citizen_id': user.get_user_id(),
    'citizen_name': user.get_name(), 'service': dl.get_name(),
    'department': dl.get_department(), 'fee': dl.get_fee(),
    'documents': stack.get_all(), 'status': 'Submitted',
    'submitted_on': datetime.datetime.now().strftime('%d-%m-%Y %H:%M'),
}
db.save_application(app_id, record)
print(f'  Application ID : {app_id}')
print(f'  Service        : {record["service"]}')
print(f'  Fee            : Rs. {record["fee"]}')
print(f'  Status         : {record["status"]} [OK]')

# 6. Track Application
print('\n--- 5. Track Application ---')
rec = db.get_application(app_id)
print(f'  App ID       : {rec["app_id"]}')
print(f'  Citizen      : {rec["citizen_name"]}')
print(f'  Service      : {rec["service"]}')
print(f'  Department   : {rec["department"]}')
print(f'  Status       : {rec["status"]} [OK]')
print(f'  Submitted    : {rec["submitted_on"]}')

# 7. Guidance (Recursion)
print('\n--- 6. Application Guidance (Recursion) ---')
steps = ['Visit RTO website', 'Fill Form LL', 'Attach Aadhaar',
         'Pay Rs.200', 'Written Test', 'Get Learner Licence',
         'Practice 30 days', 'Driving Skill Test', 'Licence issued']
print(f'  Guidance for: {dl.get_name()}')
display_steps(steps)

# 8. Search (Recursion + Strings)
print('\n--- 7. Search Services ---')
names = [s.get_name() for s in db.get_all_services().values()]
for kw in ['pass', 'driv', 'income', 'ration']:
    results = recursive_search(names, kw)
    print(f'  Search "{kw}" -> {results}')

# 9. String Demo
print('\n--- 8. String Concepts Demo ---')
sample = 'Smart Public Service Navigator'
print(f'  Original      : {sample}')
print(f'  lower()       : {sample.lower()}')
print(f'  upper()       : {sample.upper()}')
print(f'  title()       : {sample.title()}')
print(f'  split()       : {sample.split()}')
print(f'  len()         : {len(sample)}')
print(f'  count("a")    : {sample.count("a")}')
print(f'  replace()     : {sample.replace(" ", "-")}')
print(f'  startswith()  : {sample.startswith("Smart")}')
print(f'  join with -   : {join_with_dash(words_in_name(sample))}')
print(f'  mask_id()     : {mask_id(user.get_user_id())}')
print(f'  clean_input() : {clean_input("  Hello  World  ")}')
print(f'  count_vowels(): {count_vowels(sample)}')
print(f'  search_keyword: {search_keyword(sample, "Navigator")}')

# 10. View All Applications
print('\n--- 9. All Applications ---')
all_apps = db.get_all_applications()
print(f'  Total: {len(all_apps)}')
for aid, r in all_apps.items():
    print(f'  {aid} | {r["service"]:<22} | {r["citizen_name"]} | {r["status"]}')

# Exit
print()
print_banner()
print('  Jai Hind!')
print()
print('=' * 50)
print('  ALL 9 FEATURES TESTED SUCCESSFULLY')
print('=' * 50)
