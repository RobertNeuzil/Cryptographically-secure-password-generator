import secrets
import string
import random

def generate_password(length=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True, avoid_ambiguous=False):
    """
    Generate a secure password.
    - length: total length of password (int)
    - use_lower/use_upper/use_digits/use_symbols: include those character sets (bool)
    - avoid_ambiguous: if True, remove characters that are often confused (like l, 1, O, 0)
    Returns: password string
    """
    if length <= 0:
        raise ValueError("length must be a positive integer")
    
    pools = []
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("!@#$%^&*()-_=+[]{};:,.<>?/")  # adjust if your system disallows some symbols
    
    if not pools:
        raise ValueError("At least one character type must be enabled")
    
    if avoid_ambiguous:
        ambiguous = {'l','I','1','O','0'}
        pools = [''.join(ch for ch in pool if ch not in ambiguous) for pool in pools]
        pools = [p for p in pools if p]
        if not pools:
            raise ValueError("No characters left after removing ambiguous characters")
    
    # Guarantee at least one char from each selected pool
    password_chars = [secrets.choice(pool) for pool in pools]
    
    if length < len(password_chars):
        raise ValueError(f"length too small for guaranteeing one of each selected type (need at least {len(password_chars)})")
    
    combined = ''.join(pools)
    for _ in range(length - len(password_chars)):
        password_chars.append(secrets.choice(combined))
    
    # Shuffle using a system RNG to avoid predictable placement
    sysrand = random.SystemRandom()
    sysrand.shuffle(password_chars)
    
    return ''.join(password_chars)

def generate_multiple(n=5, **kwargs):
    """Generate n passwords with same kwargs. Returns list of passwords."""
    return [generate_password(**kwargs) for _ in range(n)]

if __name__ == "__main__":
    print("=== Secure Password Generator ===")
    length = int(input("Enter password length (e.g. 12): ") or 12)

    use_lower = input("Include lowercase letters? (y/n) [y]: ").strip().lower() != "n"
    use_upper = input("Include uppercase letters? (y/n) [y]: ").strip().lower() != "n"
    use_digits = input("Include digits? (y/n) [y]: ").strip().lower() != "n"
    use_symbols = input("Include symbols? (y/n) [y]: ").strip().lower() != "n"
    avoid_ambiguous = input("Avoid ambiguous characters (1, l, O, 0)? (y/n) [n]: ").strip().lower() == "y"

    password = generate_password(length=length,
                                 use_lower=use_lower,
                                 use_upper=use_upper,
                                 use_digits=use_digits,
                                 use_symbols=use_symbols,
                                 avoid_ambiguous=avoid_ambiguous)

    print("\nYour password:\n", password)


input("\nPress Enter to exit...")
