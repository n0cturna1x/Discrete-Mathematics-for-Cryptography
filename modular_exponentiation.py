def modular_exponentiation(int, exp, mod):
    result = 1
    while exp > 0:
        if exp & 1 == 1:
            result = (result * int) % mod
        int = (int * int) % mod
        exp >>= 1
    return result

print("219^222 mod 348 = ", modular_exponentiation(219, 222, 348))
print("\n3^98765432 mod 11 = ", modular_exponentiation(3, 98765432, 11))