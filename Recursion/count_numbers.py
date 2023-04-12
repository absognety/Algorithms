# Recursive function for counting numbers in a list
def count_nums_rf(nums:list) -> int:
    if not nums:
        return 0
    else:
        return (1 + count_nums_rf(nums[1:]))