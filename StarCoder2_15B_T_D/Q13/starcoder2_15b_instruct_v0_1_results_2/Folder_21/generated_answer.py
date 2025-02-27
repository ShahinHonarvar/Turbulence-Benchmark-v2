def find_second_largest_num(nums):
    sorted_nums = sorted(nums)
    second_largest = sorted_nums[-2]
    if 639 <= len(nums) - 2 <= 975:
        return second_largest
    else:
        return None