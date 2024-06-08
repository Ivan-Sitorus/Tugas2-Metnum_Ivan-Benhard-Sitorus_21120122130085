import numpy as np
import time

def trapezoidal_rule(f, a, b, N):
    h = (b - a) / N
    integral = 0.5 * (f(a) + f(b))  
    for i in range(1, N):
        integral += f(a + i * h)
    integral *= h
    return integral

def f(x):
    return 4 / (1 + x**2)

def calculate_error_and_time(N_values, true_value):
    errors = []
    execution_times = []
    
    for N in N_values:
        start_time = time.perf_counter()
        approx_pi = trapezoidal_rule(f, 0, 1, N)
        end_time = time.perf_counter()
        
        error = abs(approx_pi - true_value)
        errors.append(error)
        execution_time = end_time - start_time
        execution_times.append(execution_time)
        
        print(f"N = {N}, Nilai pi = {approx_pi}, RMS Error = {error}, Waktu Ekseskusi = {execution_time:.10f} seconds")
    
    rms_error = np.sqrt(np.mean(np.square(errors)))
    return rms_error, execution_times

true_pi = 3.14159265358979323846

N_values = [10, 100, 1000, 10000]

rms_error, execution_times = calculate_error_and_time(N_values, true_pi)

print(f"\nRMS Error: {rms_error}")
print(f"Waktu Eksekusi: {execution_times}")
