def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    second_smallest = sorted_nums[31]
    return second_smallest if second_smallest != sorted_nums[30] else None