def composite_nums_between_indices(nums):
    composite_nums = set()
    for i, num in enumerate(nums):
        for j in range(2, num):
            if num % j == 0:
                if 22 <= i <= 50:
                    composite_nums.add(num)
                break
    return composite_nums