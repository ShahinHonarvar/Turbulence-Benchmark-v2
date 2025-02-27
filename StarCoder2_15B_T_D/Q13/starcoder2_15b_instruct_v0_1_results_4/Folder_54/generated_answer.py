def find_second_largest_num(nums):
    sorted_nums = sorted(nums)
    second_largest = sorted_nums[-2]
    return second_largest