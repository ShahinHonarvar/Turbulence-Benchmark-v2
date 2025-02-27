def find_largest_num(nums):
    largest = max(nums)
    index = nums.index(largest)
    if 0 <= index <= 5:
        return largest
    else:
        return None