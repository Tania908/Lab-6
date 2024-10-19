import numpy as np
import time
import pandas as pd

# Generate random integers function
def generate_random(n):
    randomArr = np.random.permutation(n)
    return randomArr

def bubble_sort_with_escape(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, the array is sorted
        if not swapped:
            break
    return arr

# Size of arrays to be generated
input_sizes = [10**3, 2 * 10**3, 3 * 10**3, 4 * 10**3, 5 * 10**3,  6 * 10**3, 7 * 10**3, 8 * 10**3, 9 * 10**3, 10**4]

# Arrays for times to be stored in
best_case_results = []
worst_case_results = []
avg_case_results = []

# Looping through each input size
for i in input_sizes:
    # Generating random integers
    randomArr = generate_random(i)

    # Best case (sorted array)
    best_case_arr = sorted(randomArr.copy())
    start = time.time()
    bubble_sort_with_escape(best_case_arr)
    best_time = (time.time() - start) * 1000  # Convert to milliseconds

    # Worst case (reverse sorted array)
    worst_case_arr = sorted(randomArr.copy(), reverse=True)
    start = time.time()
    bubble_sort_with_escape(worst_case_arr)
    worst_time = (time.time() - start) * 1000  # Convert to milliseconds

    # Average case (random array)
    avg_case_arr = generate_random(i)
    start = time.time()
    bubble_sort_with_escape(avg_case_arr.copy())
    avg_time = (time.time() - start) * 1000  # Convert to milliseconds

    # Append results to lists
    best_case_results.append({'input': i, 'time': best_time})
    worst_case_results.append({'input': i, 'time': worst_time})
    avg_case_results.append({'input': i, 'time': avg_time})

# Saving to CSV
df_data_1 = pd.DataFrame(best_case_results)
df_data_1.to_csv('data_1.csv', index=False)

df_data_2 = pd.DataFrame(worst_case_results)
df_data_2.to_csv('data_2.csv', index=False)

df_data_3 = pd.DataFrame(avg_case_results)
df_data_3.to_csv('data_3.csv', index=False)

# CSV files have been created
print("File generation completed")

