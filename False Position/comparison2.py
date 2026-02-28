import math

def f(x):
    return x - math.cos(x)

def df(x):
    return 1 + math.sin(x)

TOLERANSI = 1e-14
MAKS_ITERASI = 1000 # agar tidak infinite loop

print(f"{'Metode':<15} | {'Jumlah Iterasi':<15} | {'Estimasi Akar Akhir (x)':<20}")
print("-" * 55)

# 1. METODE NEWTON (x0 = 0.8)
x_n = 0.8
iter_newton = 0
for _ in range(MAKS_ITERASI):
    iter_newton += 1
    x_baru = x_n - f(x_n) / df(x_n)
    if abs(x_baru - x_n) < TOLERANSI:
        x_n = x_baru
        break
    x_n = x_baru
print(f"{'Newton':<15} | {iter_newton:<15} | {x_n:.15f}")

# 2. METODE SECANT (x0 = 0.6, x1 = 0.8)
x_s0 = 0.6
x_s1 = 0.8
iter_secant = 0
for _ in range(MAKS_ITERASI):
    iter_secant += 1
    x_baru = x_s1 - f(x_s1) * (x_s1 - x_s0) / (f(x_s1) - f(x_s0))
    if abs(x_baru - x_s1) < TOLERANSI:
        x_s1 = x_baru
        break
    x_s0 = x_s1
    x_s1 = x_baru
print(f"{'Secant':<15} | {iter_secant:<15} | {x_s1:.15f}")

# 3. METODE BISECTION (a = 0.6, b = 0.8)
a_b = 0.6
b_b = 0.8
iter_bisection = 0
for _ in range(MAKS_ITERASI):
    iter_bisection += 1
    c_b = (a_b + b_b) / 2.0
    if (b_b - a_b) / 2.0 < TOLERANSI:
        break
    if f(a_b) * f(c_b) < 0:
        b_b = c_b
    else:
        a_b = c_b
print(f"{'Bisection':<15} | {iter_bisection:<15} | {c_b:.15f}")

# 4. METODE FALSE POSITION (a = 0.6, b = 0.8)
a_fp = 0.6
b_fp = 0.8
iter_fp = 0
c_fp = a_fp
for _ in range(MAKS_ITERASI):
    iter_fp += 1
    fa = f(a_fp)
    fb = f(b_fp)
    
    c_baru = (a_fp * fb - b_fp * fa) / (fb - fa)
    fc = f(c_baru)
    
    if abs(c_baru - c_fp) < TOLERANSI or abs(fc) < TOLERANSI:
        c_fp = c_baru
        break
        
    c_fp = c_baru
    
    if fa * fc < 0:
        b_fp = c_fp
    else:
        a_fp = c_fp
print(f"{'False Position':<15} | {iter_fp:<15} | {c_fp:.15f}")
print("-" * 55)