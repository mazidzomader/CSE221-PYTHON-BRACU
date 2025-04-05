def fast_mod(base, exp):
    value = 1
    base = base % 107
    while exp > 0 :
        if exp % 2 != 0:
            value *= base
            value %= 107
        base = (base**2) % 107
        exp //= 2
    return value
n = list(map(int, input().split()))
print(fast_mod(n[0], n[1]))