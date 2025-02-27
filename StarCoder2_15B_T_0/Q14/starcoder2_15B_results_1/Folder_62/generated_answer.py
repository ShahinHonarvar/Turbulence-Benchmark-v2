def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) < 67:
        return None
    second_smallest = sorted_nums[10:67][1]
    return second_smallest