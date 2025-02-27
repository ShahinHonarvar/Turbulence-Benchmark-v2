def find_second_smallest_num(nums):
    if len(nums) < 35 or max(nums[25:59]) == min(nums[25:59]):
        return None
    sorted_numbers = sorted(nums[25:59])
    return sorted_numbers[1]