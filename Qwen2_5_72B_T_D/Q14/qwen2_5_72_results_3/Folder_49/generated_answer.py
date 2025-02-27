def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 201:
        return None
    slice_nums = numbers[80:201]
    if len(slice_nums) < 2:
        return None
    unique_nums = list(set(slice_nums))
    unique_nums.sort()
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]