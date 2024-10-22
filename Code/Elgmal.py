def is_primitive_root(g, p):
    p_minus_1 = p - 1
    factors = prime_factors(p_minus_1)
    for q in factors:
        if pow(g, p_minus_1 // q, p) == 1:
            return False
    return True

def prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

def find_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    return None

# Example usage
p = 7
primitive_root = find_primitive_root(p)
print(f"The primitive root of {p} is {primitive_root}")
