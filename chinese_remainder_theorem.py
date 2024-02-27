from os import system

def chinese_remainder_theorem(m, b):
    A = {1: 1, 2: 0, 3: m}
    B = {1: 0, 2: 1, 3: b}
    T = {1: 0, 2: 0, 3: 0}
    Q = 0
    while True:
        if B[3] == 0:
            return A[3]  
        if B[3] == 1:
            return B[2]  
        Q = A[3] // B[3]
        T[1] = (A[1] - (Q * B[1]))
        T[2] = (A[2] - (Q * B[2]))
        T[3] = (A[3] - (Q * B[3]))
        A = B.copy()
        B = T.copy()

eqs = []
for i in range(int(input("Number of Equations : "))):
    eqs.append(
        {
            "a": int(input(f"a{i+1} : ")),
            "n": int(input(f"n{i+1} : "))
        })

N = 1
for i in eqs:
    N *= i['n']

sum = 0
for i in eqs:
    sum += (i['a'] * (N//i['n']) * chinese_remainder_theorem(m=i['n'], b=N/i['n']))
while sum < 0:
    sum += N

print("x ≡ ", sum)