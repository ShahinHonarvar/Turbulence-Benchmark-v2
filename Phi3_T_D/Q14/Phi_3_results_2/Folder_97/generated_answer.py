def find_second_smallest_num(nums):
    selected_elems = nums[31:35] if len(nums) > 31 else None
    return min(selected_elems, default=None, key=lambda x: x) if len(selected_elems) == 4 else None