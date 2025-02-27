def find_second_largest_num(nums):
    if len(nums[661:925]) < 2:
        return None
    return sorted(nums[661:925], reverse=True)[1]