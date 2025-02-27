def composite_nums_between_indices(nums):

    def is_composite(num):
        if num <= 3:
            return num > 1
        if num % 2 == 0 or num % 3 == 0:
            return True
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return True
            i += 6
        return False
    start_index = 55
    end_index = 98
    if start_index > len(nums) or end_index > len(nums):
        return set()
    return {num for num in nums[start_index:end_index + 1] if is_composite(num)}