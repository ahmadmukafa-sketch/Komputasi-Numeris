import numpy as np

def display_system(matrix, n):
    """Menampilkan sistem persamaan dalam format Ax = b"""
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

def solve_gauss_jordan_with_inverse():
    print("=== Kalkulator Gauss-Jordan: SPL & Invers Matriks ===")
    
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

    #Bentuk Augmented Matrix untuk Invers [ A | I | b ]
    identity = np.eye(n)
    aug = np.hstack((A_input, identity, b_input.reshape(-1, 1)))

    display_system(np.hstack((A_input, b_input.reshape(-1, 1))), n)
    print("\nAugmented Matrix Awal [ A | I | b ]:")
    print(np.round(aug, 2))
    print("-" * 60)

    #Proses Gauss-Jordan
    is_singular = False
    for i in range(n):
        # Partial Pivoting
        max_row = np.argmax(np.abs(aug[i:, i])) + i
        aug[i], aug[max_row] = aug[max_row].copy(), aug[i].copy()
        
        if abs(aug[i, i]) < 1e-10:
            is_singular = True
            break #berhenti karena tidak bisa membagi dengan 0

        #normalisasi baris pivot
        pivot = aug[i, i]
        aug[i] = aug[i] / pivot

        #eliminasi kolom i
        for j in range(n):
            if i != j:
                factor = aug[j, i]
                aug[j] -= factor * aug[i]

    #Output Hasil
    if is_singular:
        print("\n--- ANALISIS ---")
        print("Determinan Matriks = 0.")
        print("1. Matriks TIDAK MEMILIKI INVERS.")
        
        # Cek tipe solusi SPL (No Solution vs Infinite)
        has_no_sol = False
        for i in range(n):
            if np.all(np.abs(aug[i, :n]) < 1e-10) and abs(aug[i, -1]) > 1e-10:
                has_no_sol = True
        
        if has_no_sol:
            print("2. SPL: Tidak memiliki solusi khusus.")
        else:
            print("2. SPL: Memiliki solusi tak hingga.")
    else:
        # Pisahkan Invers dan Solusi
        inverse_matrix = aug[:, n:2*n]
        solutions = aug[:, -1]

        print("\nMatriks Setelah Gauss-Jordan [ I | A^-1 | x ]:")
        print(np.round(aug, 4))

        print("\n--- HASIL AKHIR ---")
        print("1. Matriks Invers (A^-1):")
        print(np.round(inverse_matrix, 4))
        
        print("\n2. Solusi Sistem Persamaan:")
        for i in range(n):
            print(f"   x{i+1} = {round(solutions[i], 4)}")

if __name__ == "__main__":
    solve_gauss_jordan_with_inverse()