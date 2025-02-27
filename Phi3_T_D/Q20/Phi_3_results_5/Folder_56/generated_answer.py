def find_n_th_smallest_num(nums):
    if not 2 <= len(nums) <= 7:
        return None
    potential_elements = sorted(nums[2:8])
    if len(potential_elements) < 4:
        return None
    return potential_elements[3]