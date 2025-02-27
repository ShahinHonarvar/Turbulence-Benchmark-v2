def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    try:
        return sorted_nums[1:52][1]
    except IndexError:
        return None