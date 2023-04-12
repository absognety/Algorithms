# Recursive function for Adding numbers in a list
def add_numbers_rf(nums:list) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    else:
        total = nums[0] + add_numbers_rf(nums[1:])
        return total