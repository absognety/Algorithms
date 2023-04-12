# Recursive function for quicksort algorithm
def quicksort_rf(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [e for e in arr[1:] if e <= pivot]
        greater_than_pivot = [e for e in arr[1:] if e > pivot]
        return quicksort_rf(less_than_pivot) + [pivot] + quicksort_rf(greater_than_pivot)