def find_second_smallest_num(numbers):
    sliced_nums = numbers[686:988]
    if len(sliced_nums) < 2:
        return None
    sorted_nums = sorted(sliced_nums)
    return sorted_nums[1]