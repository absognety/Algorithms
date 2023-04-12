# Recursive function for Adding numbers in a list
def add_numbers_rf(nums:list) -> int:
    """
    Parameters
    ----------
    nums : list
        Input entries in a list to be added

    Returns
    -------
    int
        Returns total/sum of entries of a given list.
    """
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    else:
        total = nums[0] + add_numbers_rf(nums[1:])
        return total
    
    
if __name__ == '__main__':
    print (add_numbers_rf([1,2,3,4,5,6]))