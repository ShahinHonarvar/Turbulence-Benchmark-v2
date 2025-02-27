def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    second_largest = sorted_nums[1]
    return second_largest if 533 <= nums.index(second_largest) <= 605 else None