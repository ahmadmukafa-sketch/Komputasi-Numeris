import numpy as np

def hitung_F(x, y):
    return np.array([
        [y + x**2 - 1 - x],
        [x**2 - 2*y**2 - y]
    ])

def hitung_Matriks_Turunan(x, y):
    return np.array([
        [2*x - 1, 1],
        [2*x, -4*y - 1]
    ])

# x = 0, y = 0
X = np.array([
    [0.0], 
    [0.0]
])

print(f"{'Iterasi':<8} | {'x':<12} | {'y':<12}")
print("-" * 35)

# iterasi
for i in range(5):
    # nilai x dan y saat ini
    x = X[0][0]
    y = X[1][0]
    
    # nilai F(x)
    matriks_F = hitung_F(x, y)
    
    # nilai F'(x)
    matriks_F_aksen = hitung_Matriks_Turunan(x, y)
    
    # F'(x)^-1 
    invers_F_aksen = np.linalg.inv(matriks_F_aksen)
    
    # rumus Newton-Raphson: X = X - (Invers F' * F)
    X = X - np.dot(invers_F_aksen, matriks_F)
    
    print(f"{i+1:<8} | {X[0][0]:<12.6f} | {X[1][0]:<12.6f}")

print("-" * 35)
print(f"Hasil akhir estimasi: x = {X[0][0]:.6f}, y = {X[1][0]:.6f}")