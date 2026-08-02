from generator import generate_password

password = generate_password(
    16,
    True,
    True,
    True,
    True,
)

print(password)