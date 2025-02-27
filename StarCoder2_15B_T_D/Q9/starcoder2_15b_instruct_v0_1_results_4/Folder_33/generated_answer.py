from index 667 to index 774, both inclusive. If no odd integers exist in the

def all_odd_ints_inclusive(nums):
    """
    This function takes a list of integers and returns the list of all odd integers
    specified range, an empty list is returned.
    """
    odd_ints = []
    for i in range(667, 775):
        if nums[i] % 2 == 1:
            odd_ints.append(nums[i])
    return odd_ints