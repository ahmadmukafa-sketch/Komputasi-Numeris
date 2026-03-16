import numpy as np

def display_system(matrix, n):
    print("\nBentuk Persamaan Linear (Ax = b):")
    for i in range(n):
        line = "  "
        for j in range(n):
            sign = " + " if j > 0 and matrix[i, j] >= 0 else " "
            if j > 0 and matrix[i, j] < 0: sign = " - "
            val = abs(matrix[i, j])
            line += f"{sign}{val}x{j+1}"
        line += f" = {matrix[i, n]}"
        print(line)

def is_diagonally_dominant(A):
    n = A.shape[0]
    for i in range(n):
        sum_others = np.sum(np.abs(A[i, :])) - np.abs(A[i, i])
        if np.abs(A[i, i]) <= sum_others:
            return False
    return True

def make_diagonally_dominant(A, b):
    n = A.shape[0]
    A_new = np.zeros((n, n))
    b_new = np.zeros(n)
    baris_terpakai = [] 

    for i in range(n): 
        baris_ditemukan = False
        
        for j in range(n):
            if j in baris_terpakai:
                continue
            
            elemen_calon_diagonal = np.abs(A[j, i])
            jumlah_elemen_lain = np.sum(np.abs(A[j, :])) - elemen_calon_diagonal
            
            if elemen_calon_diagonal > jumlah_elemen_lain:
                A_new[i, :] = A[j, :]
                b_new[i] = b[j]
                baris_terpakai.append(j)
                baris_ditemukan = True
                break 
        
        if not baris_ditemukan:
            return A, b, False

    return A_new, b_new, True

def solve_gauss_seidel():
    print("=== Kalkulator Gauss-Seidel (Tanpa Itertools) ===")
    
    try:
        n = int(input("Masukkan dimensi matriks n (maks 5): "))
        if n > 5 or n < 1:
            print("Maksimal 5 ya.")
            return
    except ValueError:
        print("Input harus angka.")
        return

    #Input Matriks A dan Vektor b
    A_input = np.zeros((n, n))
    b_input = np.zeros(n)
    
    print(f"\nMasukkan elemen Matriks A ({n}x{n}):")
    for i in range(n):
        for j in range(n):
            A_input[i, j] = float(input(f"  A[{i+1},{j+1}]: "))
    
    print(f"\nMasukkan elemen Vektor b ({n}x1):")
    for i in range(n):
        b_input[i] = float(input(f"  b[{i+1}]: "))

    aug = np.hstack((A_input, b_input.reshape(-1, 1)))
    display_system(aug, n)
    
    #Pengecekan Diagonal Dominan
    print("\n--- ANALISIS DIAGONAL DOMINAN ---")
    if is_diagonally_dominant(A_input):
        print("Matriks sudah diagonal dominan. Bisa langsung dilanjutkan.")
    else:
        print("Matriks belum diagonal dominan. Mencoba menukar baris.")
        A_input, b_input, success = make_diagonally_dominant(A_input, b_input)
        
        if success:
            print("Berhasil menukar baris! Matriks sekarang diagonal dominan.")
            aug_new = np.hstack((A_input, b_input.reshape(-1, 1)))
            display_system(aug_new, n)
        else:
            print("GAGAL: Matriks tidak bisa menjadi diagonal dominan.")
            print("Sistem Persamaan Linear ini tidak bisa diselesaikan dengan metode Gauss-Seidel.")
            return

    print("\n--- PROSES ITERASI GAUSS-SEIDEL ---")
    maks_iterasi = 50
    toleransi = 1e-6
    x = np.zeros(n) 
    
    for k in range(maks_iterasi):
        x_lama = x.copy()
        
        for i in range(n):
            sum_ax = 0
            for j in range(n):
                if i != j:
                    sum_ax += A_input[i, j] * x[j]
            
            x[i] = (b_input[i] - sum_ax) / A_input[i, i]
        
        error = np.max(np.abs(x - x_lama))
        str_x = " | ".join([f"x{i+1}={x[i]:.4f}" for i in range(n)])
        print(f"Iterasi {k+1:2d}: {str_x} | Error: {error:.6f}")
        
        if error < toleransi:
            print(f"\nKonvergen pada iterasi ke-{k+1}!")
            break
    else:
        print(f"\nBatas iterasi maksimal ({maks_iterasi}) tercapai.")

    print("\n--- HASIL AKHIR ---")
    print("Solusi Sistem Persamaan:")
    for i in range(n):
        print(f"   x{i+1} = {round(x[i], 4)}")

if __name__ == "__main__":
    solve_gauss_seidel()