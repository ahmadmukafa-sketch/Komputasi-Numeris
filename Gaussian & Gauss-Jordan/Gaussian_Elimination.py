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

def solve_linear_system_final():
    print("=== Kalkulator SPL Gaussian (Max 5x5) ===")
    
    #Input Konfigurasi
    try:
        n = int(input("Masukkan jumlah persamaan (n): "))
        if n > 5 or n < 1:
            print("Maksimal 5 persamaan.")
            return
        
        print("\nPilih Metode Eliminasi:")
        print("1. Upper Triangular")
        print("2. Lower Triangular")
        pilihan = input("Masukkan pilihan (1/2): ")
    except ValueError:
        print("Input harus berupa angka.")
        return

    #Input Koefisien Matriks [A|b]
    matrix = np.zeros((n, n + 1))
    print(f"\nMasukkan koefisien [A] dan hasil [b]:")
    for i in range(n):
        for j in range(n):
            matrix[i, j] = float(input(f"  A[{i+1},{j+1}]: "))
        matrix[i, n] = float(input(f"  Hasil b[{i+1}]: "))

    #Sebelum eliminasi
    display_system(matrix, n)
    
    print("\nAugmented Matrix Awal [A|b]:")
    print(matrix)
    print("-" * 40)

    is_singular = False

    #Proses Eliminasi
    if pilihan == '1':
        for i in range(n):
            max_row = np.argmax(np.abs(matrix[i:, i])) + i
            matrix[i], matrix[max_row] = matrix[max_row].copy(), matrix[i].copy()
            
            if abs(matrix[i, i]) < 1e-10:
                is_singular = True
                continue 

            for j in range(i + 1, n):
                factor = matrix[j, i] / matrix[i, i]
                matrix[j, i:] -= factor * matrix[i, i:]

    elif pilihan == '2':
        for i in range(n - 1, -1, -1):
            max_row = np.argmax(np.abs(matrix[:i+1, i]))
            matrix[i], matrix[max_row] = matrix[max_row].copy(), matrix[i].copy()

            if abs(matrix[i, i]) < 1e-10:
                is_singular = True
                continue

            for j in range(i - 1, -1, -1):
                factor = matrix[j, i] / matrix[i, i]
                matrix[j, :i+1] -= factor * matrix[i, :i+1]
                matrix[j, n] -= factor * matrix[i, n]
    
    #Hasil Eliminasi
    label = "Upper" if pilihan == '1' else "Lower"
    print(f"\nMatriks Hasil Eliminasi ({label} Triangular):")
    print(np.round(matrix, 4))

    #Analisis Solusi & Singularitas
    if is_singular:
        print("\n--- Hasil ---")
        print("Determinan matriks = 0 (Sistem Singular).")
        
        has_no_solution = False
        has_infinite_solution = False

        for i in range(n):
            all_zeros_A = np.all(np.abs(matrix[i, :n]) < 1e-10)
            zero_b = abs(matrix[i, n]) < 1e-10
            
            if all_zeros_A and not zero_b:
                has_no_solution = True
            elif all_zeros_A and zero_b:
                has_infinite_solution = True

        if has_no_solution:
            print("Sistem TIDAK MEMILIKI SOLUSI.")
            print("Ditemukan baris [0 0 ... | b] di mana b != 0.")
        elif has_infinite_solution:
            print("SOLUSI TAK HINGGA (Dependent).")
            print("Ditemukan baris [0 0 ... | 0].")
    else:
        # Substitusi
        x = np.zeros(n)
        if pilihan == '1':
            for i in range(n - 1, -1, -1):
                x[i] = (matrix[i, n] - np.dot(matrix[i, i+1:n], x[i+1:n])) / matrix[i, i]
        else:
            for i in range(n):
                x[i] = (matrix[i, n] - np.dot(matrix[i, :i], x[:i])) / matrix[i, i]
        
        print("\nSolusi Akhir:")
        for i in range(n):
            print(f"x{i+1} = {round(x[i], 4)}")

if __name__ == "__main__":
    solve_linear_system_final()