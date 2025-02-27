def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    sorted_nums = sorted(numbers[:7], reverse=True)
    return sorted_nums[1] if len(set(sorted_nums[:7])) > 1 else None