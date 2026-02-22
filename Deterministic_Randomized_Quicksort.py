"""
Assignment 5 – Quicksort Implementation, Analysis, and Randomization
Author: Hoai Nam Tran
Course: MSCS-532 – Algorithms and Data Structures

-----------------------------------------------------------------------
Theoretical Complexity:

Deterministic Quicksort:
    Best Case:    O(n log n)
    Average Case: O(n log n)
    Worst Case:   O(n^2)

Randomized Quicksort:
    Expected Time: O(n log n)
    Worst Case:    O(n^2) (extremely unlikely)

Space Complexity:
    Average recursion depth: O(log n)
    Worst recursion depth:   O(n)
-----------------------------------------------------------------------
"""

import random
import time


# =========================================================
# 1. Deterministic Quicksort
# =========================================================

def partition(arr, low, high):
    # Choose pivot: In deterministic quicksort, choose the last element as the pivot.
    pivot = arr[high]

    # Mark the boundary between: elements <= pivot   |   elements > pivot
    i = low - 1

    # Rearrange elements
    for j in range(low, high):

        # If current element is less than or equal to pivot
        if arr[j] <= pivot:
            i += 1  # Move boundary forward
            arr[i], arr[j] = arr[j], arr[i]   # Swap smaller element into correct position

    # Place pivot in correct sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return pivot index
    return i + 1


def quicksort(arr, low, high):
    """
    RECURSIVE QUICKSORT FUNCTION
    This function applies divide-and-conquer:
        1. Partition array
        2. Recursively sort left side
        3. Recursively sort right side
    Base Case:
        If subarray has 0 or 1 element, it is already sorted.
    Parameters:
        arr  : list to be sorted
        low  : starting index
        high : ending index
    """
       
    # Base case condition    
    while low < high:
        # Partition array and get pivot index
        pi = partition(arr, low, high)

        # Recurse into smaller partition to keep stack shallow
        if (pi - low) < (high - pi):
            quicksort(arr, low, pi - 1) # Recursively sort elements smaller than pivot
            low = pi + 1
        else:
            quicksort(arr, pi + 1, high) #Recursively sort elements greater than pivot
            high = pi - 1


# =========================================================
# 2. Randomized Quicksort
# =========================================================

def randomized_partition(arr, low, high):
    """
    RANDOMIZED PARTITION
    Instead of always choosing the last element as pivot, we randomly select an element between low and high.
    Strategy:
        1. Pick random index
        2. Swap it with last element
        3. Call standard partition()
    """

    # Select random index within subarray
    random_index = random.randint(low, high)

    # Swap random element with last element (pivot position)
    arr[random_index], arr[high] = arr[high], arr[random_index]

    # Perform standard partition
    return partition(arr, low, high)


def randomized_quicksort(arr, low, high):
    """
    RANDOMIZED QUICKSORT
    Same recursive structure as deterministic version, but uses randomized pivot selection.
    """

    if low < high:

        # Partition using randomized pivot
        pi = randomized_partition(arr, low, high)

        # Recursively sort left partition
        randomized_quicksort(arr, low, pi - 1)

        # Recursively sort right partition
        randomized_quicksort(arr, pi + 1, high)


# =========================================================
# 3. Performance Testing
# =========================================================

def test_algorithm(sort_function, arr):

    start_time = time.time()

    # Execute sorting algorithm
    sort_function(arr, 0, len(arr) - 1)

    end_time = time.time()

    return end_time - start_time


def run_performance_tests():

    sizes = [1000, 5000, 10000]

    for size in sizes:

        print("\n===================================================")
        print(f"Input Size: {size}")
        print("===================================================")

        #Generate different input distributions
        random_data = [random.randint(0, 10000) for _ in range(size)]
        sorted_data = sorted(random_data)
        reverse_data = sorted(random_data, reverse=True)

        for dataset_name, dataset in [
            ("Random", random_data.copy()),
            ("Sorted", sorted_data.copy()),
            ("Reverse", reverse_data.copy())
        ]:

            # Measure deterministic version
            det_time = test_algorithm(quicksort, dataset.copy())

            # Measure randomized version
            rand_time = test_algorithm(randomized_quicksort, dataset.copy())

            print(
                f"{dataset_name} Data → "
                f"Deterministic: {det_time:.5f}s | "
                f"Randomized: {rand_time:.5f}s"
            )


# =========================================================
# Main Execution Block
# =========================================================

if __name__ == "__main__":

    # Demonstration with small example
    example_array = [10, 7, 8, 9, 1, 5]

    print("Original array:", example_array)

    quicksort(example_array, 0, len(example_array) - 1)

    print("Sorted array (Deterministic):", example_array)

    # Run empirical comparison
    run_performance_tests()
