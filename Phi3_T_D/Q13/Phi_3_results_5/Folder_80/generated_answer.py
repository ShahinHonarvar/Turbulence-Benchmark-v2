def find_second_largest_num(nums):
    try:
        section = nums[64:67]
        sorted_section = sorted(section, reverse=True)
        return sorted_section[1]
    except IndexError:
        return None