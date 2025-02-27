def find_second_largest_num(nums):
    if 40 <= len(nums) <= 200:
        sorted_nums = sorted(nums[40:201], reverse=True)
        unique_nums = list(dict.fromkeys(sorted_nums))
        if len(unique_nums) < 2:
            return None
        else:
            return unique_nums[1]
    else:
        return None