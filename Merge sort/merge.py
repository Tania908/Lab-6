import numpy as np
import time
import pandas as pd

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

# Sizes of arrays to be tested
sizes = [10**2, 10**3, 2 * 10**3, 5 * 10**3, 8 * 10**3, 10**4, 
         2 * 10**4, 5 * 10**4, 8 * 10**4, 10**5, 2 * 10**5, 
         5 * 10**5, 8 * 10**5]

# Initialize results lists
best_case_times = []
worst_case_times = []
avg_case_times = []

# Measure performance for each case
for size in sizes:
    # Average case: random array
    random_arr = np.random.randint(0, 100000, size)
    start_time = time.time()
    merge_sort(random_arr)
    avg_case_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    avg_case_times.append(avg_case_time)

    # Best case: sorted array
    sorted_arr = sorted(random_arr)  # Create a sorted version of the random array
    start_time = time.time()
    merge_sort(sorted_arr)
    best_case_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    best_case_times.append(best_case_time)

    # Worst case: reverse sorted array
    reverse_sorted_arr = sorted(random_arr, reverse=True)  # Create a reverse sorted version
    start_time = time.time()
    merge_sort(reverse_sorted_arr)
    worst_case_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    worst_case_times.append(worst_case_time)

# Save results to CSV
df_best_results = pd.DataFrame({'Input Size': sizes, 'Best Case Time (ms)': best_case_times})
df_best_results.to_csv('data_1.csv', index=False)

df_worst_results = pd.DataFrame({'Input Size': sizes, 'Worst Case Time (ms)': worst_case_times})
df_worst_results.to_csv('data_2.csv', index=False)

df_avg_results = pd.DataFrame({'Input Size': sizes, 'Average Case Time (ms)': avg_case_times})
df_avg_results.to_csv('data_3.csv', index=False)



# CSV files have been created
print("File generation completed")
