def find_second_smallest_num(numbers):
    sliced_nums = numbers[42:69]
    if len(set(sliced_nums)) < 2:
        return None
    sorted_nums = sorted(set(sliced_nums))
    return sorted_nums[1]