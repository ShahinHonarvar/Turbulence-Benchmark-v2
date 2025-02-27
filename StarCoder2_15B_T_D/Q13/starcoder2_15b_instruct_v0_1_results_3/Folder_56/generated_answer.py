def find_second_largest_num(nums):
    largest = max(nums)
    nums.remove(largest)
    return max(nums) if nums else None