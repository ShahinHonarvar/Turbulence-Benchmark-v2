def composite_nums_between_indices(nums):
    start_index = 56
    end_index = 57
    composite_nums = set()
    for i, num in enumerate(nums):
        if start_index <= i <= end_index:
            for j in range(2, num):
                if num % j == 0:
                    composite_nums.add(num)
                    break
    return composite_nums