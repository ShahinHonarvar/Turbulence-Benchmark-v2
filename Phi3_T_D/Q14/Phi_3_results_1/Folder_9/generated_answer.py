def find_second_smallest_num(nums):
    if not 70 <= len(nums) <= 200:
        return None
    unique_nums = {num for num in nums[70:200]}
    if len(unique_nums) < 2:
        return None
    return sorted(unique_nums)[1]