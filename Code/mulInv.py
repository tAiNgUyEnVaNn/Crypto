def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"No multiplicative inverse for {a} mod {m}")
    else:
        return x % m

# Example usage:
a = 37
m = 900
inverse = mod_inverse(a, m)
print(f"The multiplicative inverse of {a} modulo {m} is {inverse}")
