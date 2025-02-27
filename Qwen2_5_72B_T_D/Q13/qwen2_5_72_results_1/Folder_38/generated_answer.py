def find_second_largest_num(nums):
    if len(nums) < 64:
        return None
    subset = nums[22:64]
    if len(set(subset)) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    while subset and subset[-1] == largest:
        subset.pop()
    if not subset:
        return None
    return max(subset)