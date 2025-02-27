def composite_nums_between_indices(nums):
    start_index = max(13, len(nums))
    end_index = min(68, len(nums))
    result = set()

    def is_composite(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    for index in range(start_index, end_index + 1):
        if is_composite(nums[index]):
            result.add(nums[index])
    return result