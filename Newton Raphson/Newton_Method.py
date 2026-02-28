def f(x):
    return x**3 - 2*x**2 + x - 3

def df(x):
    return 3*x**2 - 4*x + 1

x_sekarang = 4.0  # x0
toleransi = 1e-6  # batas error agar berhenti
maks_iterasi = 10 # batas maksimal iterasi

print(f"{'Iterasi':<8} | {'x_sekarang':<12} | {'f(x)':<12} | {'f\'(x)':<12} | {'x_baru':<12}")
print("-" * 65)

for i in range(maks_iterasi):
    # nilai fungsi dan turunannya pada x0
    fx = f(x_sekarang)
    dfx = df(x_sekarang)
    
    if dfx == 0:
        print("Turunan bernilai nol! Program dihentikan.")
        break
        
    # rumus Newton-Raphson
    x_baru = x_sekarang - (fx / dfx)
    
    print(f"{i+1:<8} | {x_sekarang:<12.6f} | {fx:<12.6f} | {dfx:<12.6f} | {x_baru:<12.6f}")
    
    # stopping Criteria: jika selisih x_baru dan x_sekarang sangat kecil
    if abs(x_baru - x_sekarang) < toleransi:
        print("-" * 65)
        print(f"Konvergen pada iterasi ke-{i+1}!")
        x_sekarang = x_baru
        break
        
    # nilai x untuk iterasi berikutnya
    x_sekarang = x_baru

print(f"\nAkar persamaan x = {x_sekarang:.6f}")