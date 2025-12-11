# Test af MergeSort_binary 
# Her måles der kørseltiden for selve algoritmen
# 3 input-typer : 
# - best cae : allerede sorteret
# - worst case : omvendt sorteret
# - random : tilfældeig rækkefølge

# størrelse 
# - 10 elementer 
# - 10000 elementer 

import random
import time
import math
import statistics
from typing import List, Callable, Dict, Any

# ---------- tidligere kode  ----------
def merge_sort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    left_half  = numbers[:mid]
    right_half = numbers[mid:]
    sorted_left  = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    return merge(sorted_left, sorted_right)

def merge(left: List[int], right: List[int]) -> List[int]:
    merged_list, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i]); i += 1
        else:
            merged_list.append(right[j]); j += 1
    merged_list.extend(left[i:])
    merged_list.extend(right[j:])
    return merged_list
# ----------------------------------------

def generate_input(size: int, case: str) -> List[int]:
    """Laver en liste med `size` elementer efter case-valget."""
    base = list(range(1, size + 1))          # 1..size
    if case == "best":
        return base                          # allerede sorteret
    if case == "worst":
        return base[::-1]                    # omvendt sorteret
    if case == "random":
        random.shuffle(base)
        return base
    raise ValueError("case skal være 'best', 'worst' eller 'random'")

def benchmark(fn: Callable[[List[int]], List[int]],
              data: List[int],
              runs: int = 5) -> float:
    """Kører fn `runs` gange og returnerer median-tiden i sekunder."""
    times: List[float] = []
    for _ in range(runs):
        dummy = data.copy()        # undgå side-effekter
        t0 = time.perf_counter()
        _ = fn(dummy)
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return statistics.median(times)

def pretty_table(results: Dict[str, Dict[str, float]]) -> None:
    """Udskriver en lille markdown-venlig tabel."""
    sizes = sorted({k[1] for k in results.keys()})
    cases = ["best", "random", "worst"]
    print("\nSammenligning (median-tid i ms)")
    print("| size  | best | random | worst |")
    print("|-------|-----:|-------:|------:|")
    for s in sizes:
        best   = results[("best",   s)] * 1000
        random = results[("random", s)] * 1000
        worst  = results[("worst",  s)] * 1000
        print(f"| {s:>5} | {best:6.3f} | {random:7.3f} | {worst:6.3f} |")

def main() -> None:
    sizes  = [10, 1_000]
    cases  = ["best", "worst", "random"]
    runs   = 7                       # nok til stabil median
    results: Dict[Tuple[str, int], float] = {}

    for size in sizes:
        print(f"\nTester størrelse {size}")
        for case in cases:
            data = generate_input(size, case)
            t = benchmark(merge_sort, data, runs=runs)
            results[(case, size)] = t
            print(f"  {case:6}  {t*1000:8.3f} ms")

    pretty_table(results)

    # Lille opsummering
    print("\nKonklusion:")
    for size in sizes:
        best  = results[("best",  size)]
        worst = results[("worst", size)]
        faktor = worst / best
        print(f"  {size} elem: worst / best ≈ {faktor:.2f}x "
              f"(teoretisk ≈ log₂({size}) ≈ {math.log2(size):.1f})")

if __name__ == "__main__":
    main()
