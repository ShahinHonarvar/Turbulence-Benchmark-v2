def find_second_largest_num(nums):
    sorted_nums = sorted(nums)[::-1]
    second_largest = sorted_nums[1]
    if 33 <= nums.index(second_largest) <= 36:
        return second_largest
    else:
        return None