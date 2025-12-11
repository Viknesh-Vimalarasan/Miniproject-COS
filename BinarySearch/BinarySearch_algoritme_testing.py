
def binary_search (list, key):
    low = 0 
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if list[mid] == key:
            return mid 
        elif list[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return - 1

# Testing 
list = [1, 3, 6, 3, 5, 6, 4, 10, 22, 12, 23, 23, 15, 13, 18, 24, 28, 26, 30, 31, 34]
print(binary_search(list, 10))
print(binary_search(list, 18))

import random
import time
import math
import statistics
from typing import List, Callable, Dict, Any

    

def benchmark_search(fn: Callable[[List[int], int], int], data: List[int], key: int, runs: int = 5_000) -> float:
    times : List[float] = []
    for _ in range(runs):
        t0 = time.perf_counter()
        _ = fn(data, key) 
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return statistics.median(times) 


def main_search () -> None:
    sizes = [10, 1_000]
    runs = 5_000 
    print("\nBinary search tider (gennemsnit af 5000 kald)")
    print("| Size | first | middle | last | random |")
    print("|-----:|------:|-------:|------:|-------:|")
    for size in sizes:
        data = list(range(1, size + 1))
        t_first   = benchmark_search(binary_search, data, 1, runs=runs)
        t_middle  = benchmark_search(binary_search, data, size//2, runs=runs)
        t_last    = benchmark_search(binary_search, data, size, runs=runs)
        t_random  = benchmark_search(binary_search, data, random.randint(1, size), runs=runs)
        print(f"| {size:>4} | {t_first*1e6:6.1f} | {t_middle*1e6:7.1f} | {t_last*1e6:6.1f} | {t_random*1e6:7.1f} |")

    data = list(range(1, size + 1))
    key = {
        "first": 1,
        "last": size, 
        "middle": size // 2,
        "random": random.randint(1, size)
    }

