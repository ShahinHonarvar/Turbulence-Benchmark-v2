def find_second_smallest_num(nums):
    try:
        return sorted(nums[10:11])[1]
    except IndexError:
        return None