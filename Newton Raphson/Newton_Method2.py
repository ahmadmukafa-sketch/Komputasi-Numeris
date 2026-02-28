def f(x):
    return x**3 - x - 1

def df(x):
    return 3*x**2 - 1

x = 1.0             # x_0
maks_iterasi = 3    # berhenti setelah 3 iterasi
tol_x = 0.001       # batas selisih x
tol_f = 0.0001      # batas nilai fungsi

print(f"{'Iterasi':<8} | {'x_k':<12} | {'f(x_k)':<12} | {'|x_k+1 - x_k|':<15}")
print("-" * 55)

for k in range(1, maks_iterasi + 1):
    fx = f(x)
    
    if abs(fx) < tol_f:
        print(f"\nBerhenti: Kriteria |f(x_k)| < 0.0001 terpenuhi.")
        break
        
    dfx = df(x)
    if dfx == 0:
        print("\nTurunan bernilai nol! Program dihentikan.")
        break
        
    x_baru = x - (fx / dfx)
    selisih_x = abs(x_baru - x)
    
    print(f"{k:<8} | {x:<12.5f} | {fx:<12.5f} | {selisih_x:<15.5f}")
    
    if selisih_x < tol_x:
        print(f"\nBerhenti: Kriteria |x_k+1 - x_k| < 0.001 terpenuhi.")
        x = x_baru
        break
        
    x = x_baru

else:
    print(f"\nBerhenti: Kriteria maksimal {maks_iterasi} iterasi tercapai.")

print("-" * 55)
print(f"Estimasi akar terbaik: x = {x:.6f}")