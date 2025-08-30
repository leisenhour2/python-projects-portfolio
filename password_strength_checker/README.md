# Password Strength Checker

A beginner-friendly Python project that validates password strength against configurable rules.
Rules are stored in a `config.json` file, making the script easy to customize.

---

## Features

- Checks password against multiple rules:
  - Minimum length
  - Maximum length
  - Requires symbols
  - Requires uppercase letters
  - Requires lowercase letters
  - Requires digits
- Reads rules from `config.json`
- Loops until the user enters a valid password
- Clear error messages for failed rules
- Optional Unicode icons (✅ / ❌) for friendly output

---

## Example Run

```bash
Enter a password: weakpass
❌ Password failed:
 - Password must be at least 12 characters.
 - Password must contain at least one symbol (!@#$...).
 - Password must contain at least one uppercase letter.
 - Password must contain at least one number (0-9).
Try again.

Enter a password: StrongPass123!
✅ Password passed all checks!
```
