def find_second_largest_num(nums):
    sorted_nums = sorted(nums)
    second_largest = sorted_nums[-2]
    if 100 <= nums.index(second_largest) <= 200:
        return second_largest
    else:
        return None