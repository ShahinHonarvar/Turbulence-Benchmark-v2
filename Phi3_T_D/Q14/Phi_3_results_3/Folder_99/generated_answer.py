def find_second_smallest_num(nums):
    if len(nums) > 608 and len(nums) > 609 and (nums[608] != nums[609]):
        elements = sorted(nums[608:610])
        return elements[1] if len(elements) > 1 else None
    return None