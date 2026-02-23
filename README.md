# Assignment 5 – Quicksort Implementation, Analysis, and Randomization

## Overview
This project implements and analyzes the Quicksort algorithm in two forms:
- Deterministic Quicksort (fixed pivot selection)
- Randomized Quicksort (random pivot selection)
The project also includes an empirical performance comparison across different input distributions.

## Implementation Details

The program includes:

### 1. Deterministic Quicksort
- Uses the last element as the pivot
- Efficient for random input
- Can degrade to worst-case \(O(n^2)\) for sorted data

### 2. Randomized Quicksort
- Selects pivot randomly
- Reduces probability of worst-case behavior
- Provides stable performance across datasets

### 3. Performance Testing
- Compares execution time on:
  - Random data
  - Sorted data
  - Reverse-sorted data

---

## Time Complexity

| Case        | Deterministic | Randomized |
|------------|--------------|------------|
| Best Case   | O(n log n)   | O(n log n) |
| Average     | O(n log n)   | O(n log n) |
| Worst Case  | O(n²)        | O(n²) (rare) |

---

## Space Complexity

- Average: O(log n)
- Worst: O(n)

---

## How to Run (Make sure Python 3 is installed on your system.)

python Deterministic_Randomized_Quicksort.py

## Example Output

Input Size: 1000

Random Data → Deterministic: 0.00095s | Randomized: 0.00122s

Sorted Data → Deterministic: 0.03734s | Randomized: 0.00110s

Reverse Data → Deterministic: 0.02631s | Randomized: 0.00140s

## Key Findings
Deterministic Quicksort performs well on random data.

It performs poorly on sorted and reverse-sorted inputs due to unbalanced partitions.

Randomized Quicksort provides consistent performance across all datasets.

Randomization significantly improves robustness.
