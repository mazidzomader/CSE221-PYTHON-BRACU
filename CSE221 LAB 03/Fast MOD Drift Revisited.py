def mod_exponentiate(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def sum_mod(base, exp, mod):
    if base == 1:
        return exp % mod 
    
    x = mod_exponentiate(base, exp, mod * (base - 1))
    numerator = (base * (x - 1)) % (mod * (base - 1))
    denominator = base - 1  
    
    return (numerator // denominator) % mod  

t = int(input())
for _ in range(t):
    a, n, m = map(int, input().split())
    print(sum_mod(a, n, m))
