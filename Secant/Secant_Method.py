def f(x):
    return x**5 + x**3 + 3

x_min_1 = -1.0   # x_{i-1} (awalnya x_0)
x_i = -1.1       # x_i (awalnya x_1)
epsilon = 0.001  # error

print(f"{'Iterasi':<8} | {'x_{i-1}':<12} | {'x_i':<12} | {'x_{i+1}':<12} | {'|Error|':<12}")
print("-" * 65)

i = 1

while True:
    # nilai fungsi
    fx_i = f(x_i)
    fx_min_1 = f(x_min_1)
    
    # Rumus Metode Secant
    # x_{i+1} = x_i - f(x_i) * (x_i - x_{i-1}) / (f(x_i) - f(x_{i-1}))
    x_plus_1 = x_i - fx_i * (x_i - x_min_1) / (fx_i - fx_min_1)
    
    # stopping criteria
    # |x_{i+1} - x_i| < epsilon
    error = abs(x_plus_1 - x_i)
    
    print(f"{i:<8} | {x_min_1:<12.5f} | {x_i:<12.5f} | {x_plus_1:<12.5f} | {error:<12.5f}")
    
    # kondisi berhenti
    if error < epsilon:
        # Yes -> Stop
        break
        
    # No -> Update variabel untuk i = i + 1, lalu kembali ke atas
    x_min_1 = x_i
    x_i = x_plus_1
    i += 1

print("-" * 65)
print(f"x = {x_plus_1:.5f}")