import numpy as np
import time
import pandas as pd

def bubble_sort_no_escape(arr):
    input_size = len(arr)
    for i in range(input_size):
        for j in range(0, input_size - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Generate random integers function
def generate_random(n):
    random_arr = np.random.permutation(n)
    return random_arr


# Size of arrays to be generated
n = [10**3,2 * 10**3,3 * 10**3,4 * 10**3, 5 * 10**3,6 * 10**3,7 * 10**3,8 * 10**3]
num_trials = 10  # Number of trials for averaging

# Arrays for times to be stored in
best_case_results = []
worst_case_results = []
avg_case_results = []

# Looping through each input size
for size in n:
    # Best case (sorted array)
    random_arr = generate_random(size)
    best_case_arr = sorted(random_arr)
    start = time.time()
    bubble_sort_no_escape(best_case_arr)
    best_time = (time.time() - start) * 1000  # Convert to milliseconds

    # Worst case (reverse sorted array)
    worst_case_arr = sorted(random_arr, reverse=True)
    start = time.time()
    bubble_sort_no_escape(worst_case_arr)
    worst_time = (time.time() - start) * 1000  # Convert to milliseconds

    # Average case
    total_time = 0
    for _ in range(num_trials):
        random_arr = generate_random(size)
        start = time.time()
        bubble_sort_no_escape(random_arr)
        total_time += (time.time() - start) * 1000  # Convert to milliseconds
    avg_time = total_time / num_trials  # Calculate average time

    # Append results to lists
    best_case_results.append({'input': size, 'time': best_time})
    worst_case_results.append({'input': size, 'time': worst_time})
    avg_case_results.append({'input': size, 'time': avg_time})

# Saving to CSV
df_data_1 = pd.DataFrame(best_case_results)
df_data_1.to_csv('data_1.csv', index=False)

df_data_2 = pd.DataFrame(worst_case_results)
df_data_2.to_csv('data_2.csv', index=False)

df_data_3 = pd.DataFrame(avg_case_results)
df_data_3.to_csv('data_3.csv', index=False)

# CSV files have been created
print("File generation completed")
