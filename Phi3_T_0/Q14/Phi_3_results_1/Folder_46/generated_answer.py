def find_second_smallest_num(nums):
    if len(nums) < 56 or nums[13:69] == []:
        return None
    sorted_slice = sorted(nums[13:69])
    return sorted_slice[1] if len(sorted_slice) > 1 else None