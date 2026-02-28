import math

def f(x):
    return x - math.cos(x)

def df(x):
    return 1 + math.sin(x)

# target presisi: > 13 digit
TOLERANSI = 1e-14

print(f"{'Metode':<15} | {'Jumlah Iterasi':<15} | {'Hasil Akhir (x)':<20}")
print("-" * 55)

# 1. METODE NEWTON (x0 = 0.8)
x_n = 0.8
iter_newton = 0

while True:
    iter_newton += 1
    x_baru = x_n - f(x_n) / df(x_n)
    
    if abs(x_baru - x_n) < TOLERANSI:
        break
    x_n = x_baru

print(f"{'Newton':<15} | {iter_newton:<15} | {x_n:.15f}")

# 2. METODE SECANT (x0 = 0.6, x1 = 0.8)
x_s0 = 0.6
x_s1 = 0.8
iter_secant = 0

while True:
    iter_secant += 1
    # Rumus Secant
    x_baru = x_s1 - f(x_s1) * (x_s1 - x_s0) / (f(x_s1) - f(x_s0))
    
    if abs(x_baru - x_s1) < TOLERANSI:
        break
        
    x_s0 = x_s1
    x_s1 = x_baru

print(f"{'Secant':<15} | {iter_secant:<15} | {x_s1:.15f}")

# 3. METODE BISECTION (a = 0.6, b = 0.8)
a = 0.6
b = 0.8
iter_bisection = 0

while True:
    iter_bisection += 1
    c = (a + b) / 2.0
    
    # batas toleransi diukur dari lebar interval
    if (b - a) / 2.0 < TOLERANSI:
        break
        
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

print(f"{'Bisection':<15} | {iter_bisection:<15} | {c:.15f}")
print("-" * 55)