def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def linear_congruence(A, B, M):
    A = A % M
    B = B % M
    u = 0
    v = 0
    d, u, v = extended_euclidean(A, M)

    if (B % d != 0):
        print(-1)
        return
    x0 = (u * (B // d)) % M
    if (x0 < 0):
        x0 += M

    for i in range(d):
        print((x0 + i * (M // d)) % M, end = " ")

A = 7
B = 13
M = 17

print("7x ≡ 13 mod 17")
print("x ≡ ")
linear_congruence(A, B, M)
