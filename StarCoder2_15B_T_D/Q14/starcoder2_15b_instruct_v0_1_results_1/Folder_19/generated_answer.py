def find_second_smallest_num(nums):
    nums.sort()
    try:
        return nums[5]
    except IndexError:
        return None