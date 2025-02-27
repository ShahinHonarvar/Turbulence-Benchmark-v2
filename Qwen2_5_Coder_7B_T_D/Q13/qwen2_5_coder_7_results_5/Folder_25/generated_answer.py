def find_second_largest_num(numbers):
    if len(numbers[29:94]) < 2:
        return None
    sorted_nums = sorted(numbers[29:94], reverse=True)
    return sorted_nums[1]