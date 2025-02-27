def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    num_slice = nums[:3]
    num_slice.sort()
    return num_slice[1] if len(num_slice) == 3 else None