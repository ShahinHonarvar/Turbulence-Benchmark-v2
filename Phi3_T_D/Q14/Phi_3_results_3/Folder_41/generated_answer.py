def find_second_smallest_num(nums):
    if len(nums) <= 4:
        return None
    distinct_numbers = sorted(set(nums[4:7]))
    return distinct_numbers[1] if len(distinct_numbers) > 1 else None