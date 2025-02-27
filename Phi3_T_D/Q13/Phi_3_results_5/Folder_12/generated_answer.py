def find_second_largest_num(nums):
    start, end = limit_range(nums)
    return find_second_highest_in_range(nums[start:end + 1])

def limit_range(nums):
    start, end = (max(14, 15 - len(nums)), min(64, len(nums) - 1))
    return (start, end)

def find_second_highest_in_range(nums):
    unique_nums = sorted(set(nums), reverse=True)
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]