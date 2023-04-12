# Recursive function for quicksort algorithm
def quicksort_rf(arr:list) -> list:
    """
    Parameters
    ----------
    arr : list
        Array to be sorted.

    Returns
    -------
    list
        sorted array.
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [e for e in arr[1:] if e <= pivot]
        greater_than_pivot = [e for e in arr[1:] if e > pivot]
        return quicksort_rf(less_than_pivot) + [pivot] + quicksort_rf(greater_than_pivot)
    
    
if __name__ == '__main__':
    print (quicksort_rf([1,10,-10,-1000,28,9,0,-1,-1.4,19199191]))