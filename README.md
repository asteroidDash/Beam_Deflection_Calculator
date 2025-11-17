# Beam_Deflection_Calculator
This an innovative assignment for my course CS1205 (Programming In Python)
PROBLEM STATEMENT: 
BEAM DEFLECTION ANALYSIS USING PYTHON (MATPLOTLIB & SCIPY) 
 
Structural analysis is essential for predicting how beams deform under load. Manual 
calculation of beam deflection using classical equations is time-consuming and prone to error. 
This project aims to develop a Python-based computational model that calculates and plots 
the deflection and bending moment of a simply-supported beam under a central point load 
using Matplotlib and SciPy libraries. 
The model implements the Euler–Bernoulli beam theory, performing double numerical 
integration to compute deflection accurately and visualize structural behavior effectively. OBJECTIVE: 
• Model beam deflection by computing bending moment and curvature. 
• Numerically integrate curvature to find slope and deflection. 
• Apply boundary conditions for simply supported and cantilever beams. 
• Visualize deflection, supports, load position, and max deflection with plots. 
• Provide max deflection value and location for design validation. PROPOSED SOLUTION: 
The Python-based Beam Deflection Analysis program uses the Euler–Bernoulli theory to compute beam 
deformation under a central load. Numerical integration replaces manual formulas, making it suitable for 
any loading condition. 
WORKFLOW: 
• Input beam parameters: length (L), point load (P), Young's modulus (E), moment of inertia (I), load 
position (x_load), and beam type (simply supported or cantilever). 
• Compute bending moment M(x) using piecewise formulas for the point load. 
• Calculate curvature y′′(x)=M(x)E⋅Iy′′(x)=E⋅IM(x) at each position. 
• Numerically integrate curvature twice (e.g., trapezoidal rule) to get slope y′(x)y′(x) and 
deflection y(x)y(x). 
• Apply boundary conditions: for simply supported, y(0)=0, y(L)=0; for cantilever, y(0)=0, y′(0)=0 
• Plot deflected shape, supports, load position, and
