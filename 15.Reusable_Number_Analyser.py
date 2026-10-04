# Q15: Reusable Number Analysis Function
# Why a function? The analysis can be reused for any number, and it RETURNS
# the results so the caller decides what to do with them (print, store, test).
# Why a for loop inside? Checking divisors is a known range, so for + range() fits.

def analyze_number(number):
    """Return a dictionary describing the sign, parity and primality of an integer."""
    # Sign
    if number > 0:
        sign = "Positive"
    elif number < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    # Parity (works for negatives too, since -4 % 2 == 0)
    if number % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    # Prime check (same logic as Q7)
    is_prime = True
    if number < 2:
        is_prime = False
    else:
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break

    return {
        "sign": sign,
        "parity": parity,
        "prime": "Prime" if is_prime else "Not Prime",
    }


# ---------- Main program ----------
try:
    num = int(input("Enter a whole number: "))
except ValueError:
    print("Please enter a valid whole number.")
    exit()

result = analyze_number(num)

print(f"\nAnalysis of {num}:")
print(f"Sign:   {result['sign']}")
print(f"Parity: {result['parity']}")
print(f"Prime:  {result['prime']}")

# ---------- Quick self-tests ----------
print("\nSelf-tests:")
print(analyze_number(7))     # Positive, Odd, Prime
print(analyze_number(0))     # Zero, Even, Not Prime
print(analyze_number(-4))    # Negative, Even, Not Prime
print(analyze_number(1))     # Positive, Odd, Not Prime
print(analyze_number(2))     # Positive, Even, Prime