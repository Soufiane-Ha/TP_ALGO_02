import time
import random
import csv
from typing import List, Tuple, Dict


def selection_sort(arr: List[int]) -> Tuple[List[int], int, int]:
    a = arr.copy()
    n = len(a)
    comparisons = 0
    swaps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    return a, comparisons, swaps

def bubble_sort(arr: List[int]) -> Tuple[List[int], int, int]:
    a = arr.copy()
    n = len(a)
    comparisons = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return a, comparisons, swaps

def insertion_sort_by_swaps(arr: List[int]) -> Tuple[List[int], int, int]:
    a = arr.copy()
    n = len(a)
    comparisons = 0
    swaps = 0
    for i in range(1, n):
        j = i
        while j > 0:
            comparisons += 1
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                swaps += 1
                j -= 1
            else:
                break
    return a, comparisons, swaps

def insertion_sort_by_shifts(arr: List[int]) -> Tuple[List[int], int, int]:

    a = arr.copy()
    n = len(a)
    comparisons = 0
    moves = 0
    for i in range(1, n):
        key = a[i]
        moves += 1  
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]  
                moves += 1
                j -= 1
            else:
                break
        a[j + 1] = key
        moves += 1
    return a, comparisons, moves

def generate_table(n: int, disposition: str) -> List[int]:
    """
    disposition: 'A' = ascending, 'D' = descending, 'C' = random (aléatoire)
    """
    if disposition == 'A':
        return list(range(n))
    elif disposition == 'D':
        return list(range(n - 1, -1, -1))
    elif disposition == 'C':
        lst = list(range(n))
        random.shuffle(lst)
        return lst
    else:
        raise ValueError("disposition must be 'A', 'D' or 'C'")

def run_experiments(
    sizes: List[int],
    dispositions: List[str] = ['A', 'D', 'C'],
    tests_per_size_random: int = 30,
    output_csv: str = "TP02_sort_results.csv"
) -> None:
    """
    Exécute les tests et sauvegarde un CSV contenant les moyennes :
    columns: algorithm,n,disposition,avg_time_s,avg_comparisons,avg_moves_or_swaps,runs
    """
    algorithms = {
        'selection': selection_sort,
        'bubble': bubble_sort,
        'insertion_swaps': insertion_sort_by_swaps,
        'insertion_shifts': insertion_sort_by_shifts
    }

    results = []

    for n in sizes:
        for disp in dispositions:
            runs = tests_per_size_random if disp == 'C' else 3
            agg: Dict[str, Dict[str, float]] = {
                name: {'time_s': 0.0, 'comparisons': 0.0, 'moves_or_swaps': 0.0}
                for name in algorithms.keys()
            }

            for run in range(runs):
                base = generate_table(n, disp)

                if disp == 'C':
                    arr = generate_table(n, 'C')
                else:
                    arr = base[:] 

                for name, func in algorithms.items():
                    t0 = time.perf_counter_ns()
                    _, comps, moves = func(arr)
                    t1 = time.perf_counter_ns()
                    agg[name]['time_s'] += (t1 - t0) / 1e9
                    agg[name]['comparisons'] += comps
                    agg[name]['moves_or_swaps'] += moves

            # save averages
            for name in algorithms.keys():
                results.append({
                    'algorithm': name,
                    'n': n,
                    'disposition': disp,
                    'avg_time_s': agg[name]['time_s'] / runs,
                    'avg_comparisons': agg[name]['comparisons'] / runs,
                    'avg_moves_or_swaps': agg[name]['moves_or_swaps'] / runs,
                    'runs': runs
                })

    fieldnames = ['algorithm', 'n', 'disposition', 'avg_time_s', 'avg_comparisons', 'avg_moves_or_swaps', 'runs']
    with open(output_csv, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)

    print(f"Results saved to: {output_csv}")

if __name__ == "__main__":
    sizes = [100, 200, 500, 1000, 10000, 1000000, 1000000000] 
    dispositions = ['A', 'D', 'C']
    tests_per_size_random = 30
    output_csv = "TP02_sort_results.csv"

    run_experiments(sizes, dispositions, tests_per_size_random, output_csv)
