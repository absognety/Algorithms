# Recursive function for counting numbers in a list
def count_nums_rf(nums:list) -> int:
    """
    Parameters
    ----------
    nums : list
        Input entries in a list to be counted.
        
    Returns
    -------
    int
        Returns count of entries of a given list..
    """
    if not nums:
        return 0
    else:
        return (1 + count_nums_rf(nums[1:]))