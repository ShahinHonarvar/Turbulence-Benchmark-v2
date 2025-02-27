def find_second_smallest_num(numbers):
    start, end = (56, 82)
    if start > end or end >= len(numbers) or len(numbers) < end - start + 1:
        return None
    slice_nums = sorted(numbers[start:end + 1])
    return slice_nums[1] if len(slice_nums) > 1 else None