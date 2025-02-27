def find_second_smallest_num(nums):
    distinct_nums = {num for num in nums[:3] if nums[:3].count(num) == 1}
    sorted_nums = sorted(distinct_nums)
    return sorted_nums[1] if len(sorted_nums) > 1 else None