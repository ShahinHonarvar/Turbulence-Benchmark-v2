def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    try:
        return sorted_nums[20:201][1]
    except IndexError:
        return None