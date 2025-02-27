def find_second_largest_num(nums):
    valid_slice = nums[40:81]
    if len(valid_slice) < 2:
        return None
    sorted_nums = sorted(valid_slice, reverse=True)
    second_largest = sorted_nums[1]
    return second_largest