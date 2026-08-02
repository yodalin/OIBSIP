import secrets
import string

AMBIGUOUS = "0O1lI"


def generate_password(
    length,
    use_upper,
    use_lower,
    use_digits,
    use_symbols,
    exclude_ambiguous=False,
):
    if length < 8:
        raise ValueError("Password length must be at least 8.")

    pools = []

    if use_upper:
        upper = string.ascii_uppercase
        if exclude_ambiguous:
            upper = "".join(c for c in upper if c not in AMBIGUOUS)
        pools.append(upper)

    if use_lower:
        lower = string.ascii_lowercase
        if exclude_ambiguous:
            lower = "".join(c for c in lower if c not in AMBIGUOUS)
        pools.append(lower)

    if use_digits:
        digits = string.digits
        if exclude_ambiguous:
            digits = "".join(c for c in digits if c not in AMBIGUOUS)
        pools.append(digits)

    if use_symbols:
        pools.append("!@#$%^&*()-_=+[]{}<>?/")

    if len(pools) < 2:
        raise ValueError("Select at least two character types.")

    password = []

    # Guarantee at least one character from every selected group
    for pool in pools:
        password.append(secrets.choice(pool))

    all_characters = "".join(pools)

    while len(password) < length:
        password.append(secrets.choice(all_characters))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)