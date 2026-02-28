def f(x):
    return x**3 - 3*x + 1

a = 0.0
b = 1.0
toleransi = 1e-5
maks_iterasi = 20

print(f"{'Iterasi':<8} | {'a':<10} | {'b':<10} | {'c (Estimasi)':<15} | {'f(c)':<12}")
print("-" * 65)

for i in range(1, maks_iterasi + 1):
    fa = f(a)
    fb = f(b)
    
    # rumus False Position
    c = (a * fb - b * fa) / (fb - fa)
    fc = f(c)
    
    print(f"{i:<8} | {a:<10.5f} | {b:<10.5f} | {c:<15.5f} | {fc:<12.5f}")
    
    # stopping criteria: jika nilai fungsi sudah sangat mendekati nol
    if abs(fc) < toleransi:
        print("-" * 65)
        print(f"Konvergen! Akar ditemukan pada iterasi ke-{i}")
        break
        
    # evaluasi pergeseran batas (seperti Bisection)
    if fa * fc < 0:
        b = c  # akar masih berada di antara a dan c
    else:
        a = c  # akar berada di antara c dan b

print(f"\nEstimasi akar terbaik: x = {c:.6f}")