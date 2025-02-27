def find_second_smallest_num(nums):
    try:
        return sorted(nums[5:8])[1]
    except IndexError:
        return None