def find_second_largest_num(nums):
    index_begin, index_end = (661, 924)
    target_range = nums[index_begin:index_end + 1]
    if len(set(target_range)) < 2:
        return None
    largest = max(target_range)
    target_range.remove(largest)
    second_largest = max(target_range)
    return second_largest