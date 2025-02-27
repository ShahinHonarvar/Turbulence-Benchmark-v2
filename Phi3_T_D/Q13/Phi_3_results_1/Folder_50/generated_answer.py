def find_second_largest_num(numbers):
    sliced_numbers = numbers[70:85]
    unique_nums = set(sliced_numbers)
    if len(unique_nums) < 2:
        return None
    unique_nums.remove(max(unique_nums))
    return max(unique_nums)