# Q18: Employee Salary Calculator
# Why a function? The same calculation is repeated for every employee,
# so we write it once and call it for each one.
# Why a for loop? We process a known list of employees (five or more).
#
# Formulas:
#   bonus_amount = basic * bonus_pct / 100
#   gross        = basic + bonus_amount
#   tax_amount   = gross * tax_pct / 100     (tax is on gross salary)
#   final        = gross - tax_amount


def calculate_salary(name, basic, bonus_pct, tax_pct):
    """Return a dictionary with gross salary, tax amount and final salary.
    If any input is invalid, return a dictionary with an 'error' key instead."""
    if basic < 0:
        return {"error": f"{name}: basic salary cannot be negative."}
    if bonus_pct < 0:
        return {"error": f"{name}: bonus percentage cannot be negative."}
    if tax_pct < 0 or tax_pct > 100:
        return {"error": f"{name}: tax percentage must be between 0 and 100."}

    bonus_amount = basic * bonus_pct / 100
    gross = basic + bonus_amount
    tax_amount = gross * tax_pct / 100
    final = gross - tax_amount

    return {
        "name": name,
        "gross": gross,
        "tax": tax_amount,
        "final": final,
    }


# ---------- Main program ----------
employees = [
    ("Aarav", 50000, 10, 12),
    ("Priya", 65000, 15, 18),
    ("Rohan", 40000, 5, 8),
    ("Sneha", 80000, 20, 25),
    ("Vikram", 55000, 12, 15),
]

print(f"{'Name':<10}{'Gross':>12}{'Tax':>12}{'Final':>12}")
print("-" * 46)

total_final = 0
for emp in employees:
    name, basic, bonus_pct, tax_pct = emp
    result = calculate_salary(name, basic, bonus_pct, tax_pct)

    if "error" in result:
        print(result["error"])
        continue

    print(f"{result['name']:<10}{result['gross']:>12,.2f}{result['tax']:>12,.2f}{result['final']:>12,.2f}")
    total_final += result["final"]

print("-" * 46)
print(f"{'Total payout':<34}{total_final:>12,.2f}")