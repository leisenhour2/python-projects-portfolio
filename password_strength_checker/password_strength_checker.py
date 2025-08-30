# MODULES USED
from pathlib import Path
import json, re, string

# DIRECTORIES USED
MAIN_DIR = Path(__file__).resolve().parent
CONFIG = MAIN_DIR / "config.json"

# LOADS OPTIONS FROM CONFIG FILE
with open(CONFIG, "r") as f:
    config_options = json.load(f)

USE_ICONS = config_options["use_icons"]
OK = "✅" if USE_ICONS else "[OK]"
FAIL = "❌" if USE_ICONS else "[FAIL]"


# SETS UP RULELIST FOR PASSWORD TO RUN THROUGH
rules = {
    "minimum_length": (
        lambda pw: len(pw) >= config_options["minimum_length"],
        f"Password must be at least {config_options['minimum_length']} characters.",
    ),
    "maximum_length": (
        lambda pw: len(pw) <= config_options["max_length"],
        f"Password must be no more than {config_options['max_length']} characters.",
    ),
    "symbols": (
        lambda pw: bool(re.search(f"[{re.escape(string.punctuation)}]", pw)),
        "Password must contain at least one symbol (!@#$...).",
    ),
    "uppercase": (
        lambda pw: bool(re.search(r"[A-Z]", pw)),
        "Password must contain at least one uppercase letter.",
    ),
    "lowercase": (
        lambda pw: bool(re.search(r"[a-z]", pw)),
        "Password must contain at least one lowercase letter.",
    ),
    "digits": (
        lambda pw: bool(re.search(r"[0-9]", pw)),
        "Password must contain at least one number (0-9).",
    ),
}


# FUNCTION THAT RUNS PASSWORD ENTERED INTO RULE LIST AND RETURNS ERRORS
def evaluate_password(pw: str) -> list:
    errors = []
    for _, (check, message) in rules.items():
        if not check(pw):
            errors.append(message)
    return errors


# ITERATES THROUGH EVALUATE_PASSWORD FUNCTION UNTIL SUCCESSFUL
while True:
    password = input("Enter a password: ")
    errors = evaluate_password(password)

    if not errors:
        print(f"{OK} Password passed all checks!")
        break

    print(f"{FAIL} Password failed:")
    for msg in errors:
        print(" -", msg)
    print("Try again.\n")
