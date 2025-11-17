import numpy as np 
import matplotlib.pyplot as plt 
#SIMPLE BEAM DEFLECTION CALCULATOR (User Input) 
 
#USER INPUT 
print("Enter values for beam parameters:") 
 
L = float(input("Beam length, L (meters): ")) 
E = float(input("Young's modulus, E (GPa): ")) * 1e9  # Convert GPa to Pa 
I = float(input("Moment of inertia, I (m^4): ")) 
P = float(input("Point load, P (Newtons): ")) 
x_load = float(input("Position of point load from the left, x_load (meters): ")) 
beam_type = input("Beam type ('simply_supported' or 'cantilever'): ").strip() 
 
#DEFLECTION FUNCTIONS 
def deflection_simply_supported(x, L, E, I, P, a): 
    b = L - a 
    if x <= a: 
        y = -(P * b * x / (6 * E * I * L)) * (L ** 2 - b ** 2 - x ** 2) 
    else: 
        y = -(P * a * (L - x) / (6 * E * I * L)) * (2 * L * x - x ** 2 - a ** 2) 
    return y 
 
def deflection_cantilever(x, L, E, I, P): 
    y = -(P / (6 * E * I)) * (3 * L * x ** 2 - x ** 3) 
    return y 
 
#CALCULATION & PLOTTING 
x_values = np.linspace(0, L, 100) 
 
if beam_type == "simply_supported": 
    y_values = [deflection_simply_supported(x, L, E, I, P, x_load) for x in x_values] 
    title_text = 'Simply Supported Beam - Point Load' 
    support_x = [0, L] 
    support_y = [0, 0] 
elif beam_type == "cantilever": 
    y_values = [deflection_cantilever(x, L, E, I, P) for x in x_values] 
    title_text = 'Cantilever Beam - Point Load at Free End' 
    support_x = [0] 
    support_y = [0] 
else: 
    print("Invalid beam type. Please enter 'simply_supported' or 'cantilever'.") 
    exit(1) 
 
y_values = np.array(y_values) 
max_deflection = np.min(y_values) 
max_x = x_values[np.argmin(y_values)] 
 
#PLOTTING 
plt.figure(figsize=(12, 6)) 
plt.plot(x_values, np.zeros_like(x_values), 'k--', linewidth=1, label='Original Axis') 
plt.plot(x_values, y_values, 'b-', linewidth=2, label='Deflected Shape') 
plt.plot(support_x, support_y, 'rs', markersize=10, label='Support(s)/Fixed') 
 
if beam_type == "simply_supported": 
    plt.plot(x_load, 0, 'ro', markersize=8, label='Load Position') 
 
plt.plot(max_x, max_deflection, 'g*', markersize=15, label=f'Max Deflection: {max_deflection:.6f} m') 
plt.title(title_text, fontsize=14) 
plt.xlabel('Position Along Beam (m)') 
plt.ylabel('Deflection (m)') 
plt.grid(True, alpha=0.4) 
plt.legend(fontsize=10) 
plt.tight_layout() 
 
# Console output of results 
print("=" * 50) 
print(f"Beam Type: {beam_type}") 
print(f"Max Deflection: {max_deflection:.8f} m at x = {max_x:.4f} m") 
print("=" * 50) 
plt.show() 