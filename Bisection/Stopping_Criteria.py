import math

def f(x):
    """Fungsi dari persamaan x = cos(x)"""
    return x - math.cos(x)

# parameter awal
a = 0.5
b = 0.9

# stopping Criteria
toleransi_error = 0.02  # batas absolute error
max_iterasi = 5         # batas jumlah iterasi

print(f"{'Iterasi':<8} | {'a':<8} | {'b':<8} | {'Estimasi (c)':<15} | {'|Error|':<10}")
print("-" * 60)

iterasi_saat_ini = 1
error = (b - a) / 2

while iterasi_saat_ini <= max_iterasi and error >= toleransi_error:
    
    # estimasi akar (nilai tengah)
    c = (a + b) / 2
    
    # absolute error saat ini: (b-a)/2
    error = (b - a) / 2
    
    print(f"{iterasi_saat_ini:<8} | {a:<8.4f} | {b:<8.4f} | {c:<15.4f} | {error:<10.4f}")
    
    # interval a atau b untuk iterasi selanjutnya
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
        
    iterasi_saat_ini += 1

print("-" * 60)
print("\n--- KESIMPULAN ---")
print(f"Interval akhir yang mengandung akar : [{a:.3f}, {b:.2f}]")
print(f"Best estimate    : {c:.4f}")
print(f"Nilai Absolute Error saat berhenti  : {error:.4f}")