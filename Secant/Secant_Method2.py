def f(x):
    return x**6 - x - 1

x_sebelumnya = 1.0  
x_sekarang = 1.5  

toleransi = 0.0001
maks_iterasi = 10 

print(f"{'Iterasi':<8} | {'x_sebelumnya':<15} | {'x_sekarang':<15} | {'x_baru':<15}")
print("-" * 60)

for i in range(1, maks_iterasi + 1):
    f_sekarang = f(x_sekarang)
    f_sebelumnya = f(x_sebelumnya)
    
    # Rumus Metode Secant
    # x_baru = x_i - f(x_i) * (x_i - x_{i-1}) / (f(x_i) - f(x_{i-1}))
    x_baru = x_sekarang - f_sekarang * (x_sekarang - x_sebelumnya) / (f_sekarang - f_sebelumnya)
    
    print(f"{i:<8} | {x_sebelumnya:<15.6f} | {x_sekarang:<15.6f} | {x_baru:<15.6f}")
    
    if abs(x_baru - x_sekarang) < toleransi:
        print("-" * 60)
        print(f"Akar ditemukan pada x = {x_baru:.6f}")
        break
        
    x_sebelumnya = x_sekarang
    x_sekarang = x_baru