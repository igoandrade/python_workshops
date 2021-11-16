"""
This script lists all the prime numbers less than a certain integer number.
"""
import time
import matplotlib.pyplot as plt

def get_primes(n):
    primes = list(range(2, n+1))
    
    i = 0
    while i < len(primes):
        primes = primes[:i+1] + [_ for _ in primes[i+1:] if ((_ % primes[i]) != 0)]
        i += 1
    return primes

def get_primes2(n):
    primes = [2]
    for i in range(3, n+1, 2):
        for p in primes:
            if i % p == 0 or p > i**(0.5):
                break
            primes.append(i)
    return primes
    

if __name__ == "__main__":
    N = list(range(100, 10001, 500))
    time_elapsed1 = []
    time_elapsed2 = []
    for n in N:
        start_time = time.perf_counter()
        get_primes(n)
        end_time1 = time.perf_counter() - start_time
        time_elapsed1.append(end_time1)
        start_time = time.perf_counter()
        get_primes2(n)
        end_time2 = time.perf_counter() - start_time
        time_elapsed2.append(end_time2)
        print(f"n: {n:>4d} time1: {end_time1:.5f} s time2: {end_time2:.5f} s")
    plt.plot(N, time_elapsed1, 'bo--', linewidth=1, markersize=2, label="Method 1")
    plt.plot(N, time_elapsed2, 'ro--', linewidth=1, markersize=2, label="Method 2")
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.grid(True, linestyle='dashed')
    plt.show()
        