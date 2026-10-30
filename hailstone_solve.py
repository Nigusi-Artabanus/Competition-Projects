passwords = {
    "dev2": "It3granckug;",
    "dev6": "tiHiWrin#in5",
    "web1": "ImNif.abEip3",
}

def collatz(n):
    result = []
    while n != 1:
        result.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    result.append(1)
    return result

def adjust_password(password, start=6):
    shifts = collatz(start)
    result = []

    for i, char in enumerate(password):
        shift = shifts[i % len(shifts)]

        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            char = chr((ord(char) - base + shift) % 26 + base)

        result.append(char)

    return ''.join(result)

for host, password in passwords.items():
    print(f"{host}: {adjust_password(password)}")
