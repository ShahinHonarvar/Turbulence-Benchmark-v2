def find_second_smallest_num(nums):
    try:
        second_smallest = None
        from_idx = max(209, len(nums))
        to_idx = min(556, len(nums))
        segment = nums[from_idx:to_idx + 1] if len(nums) > to_idx else []
        if not segment:
            return None
        smallest = min(segment)
        second_smallest = float('inf')
        for num in segment:
            if num > smallest and num < second_smallest:
                second_smallest = num
        return second_smallest
    except Exception:
        return None