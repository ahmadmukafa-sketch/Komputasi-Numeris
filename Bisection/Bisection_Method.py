def f(x):
    return x**3 - 3*x + 1

def bisection_method(a, b, epsilon):
    print(f"{'Iterasi':<10} | {'a':<10} | {'b':<10} | {'c (mid)':<10} | {'f(c) / w':<10}")
    print("-" * 60)
    
    u = f(a)
    v = f(b)
    
    if u * v >= 0:
        print("Syarat awal gagal: f(a) dan f(b) harus memiliki tanda yang berbeda.")
        return None
        
    iterasi = 1
    
    while True:
        # titik tengah c dan evaluasi w = f(c)
        c = (a + b) / 2
        w = f(c)
        
        print(f"{iterasi:<10} | {a:<10.6f} | {b:<10.6f} | {c:<10.6f} | {w:<10.6f}")
        
        # Evaluasi: is u * w < 0 ?
        if u * w < 0:
            # yes: b = c; v = w
            b = c
            v = w
        else:
            # no: a = c; u = w
            a = c
            u = w
            
        # Evaluasi Kriteria Berhenti: is (b-a)/2 < epsilon ?
        if (b - a) / 2 < epsilon:
            # yes: Stop
            break
            
        iterasi += 1
        
    return c

# interval [0, 1]
a_init = 0.0
b_init = 1.0
eps = 1e-5 #error
akar = bisection_method(a_init, b_init, eps)

print("-" * 60)
print(f"Proses berhenti (Stop).")
print(f"Akar persamaan x = {akar:.6f}")