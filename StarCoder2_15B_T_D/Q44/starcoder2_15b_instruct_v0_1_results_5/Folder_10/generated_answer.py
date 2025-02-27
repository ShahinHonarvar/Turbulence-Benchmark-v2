def composite_nums_between_indices(nums):
    composite_nums = set()
    for i, num in enumerate(nums):
        if num > 1:
            is_composite = False
            for j in range(2, num):
                if num % j == 0:
                    is_composite = True
                    break
            if is_composite and 37 <= i <= 51:
                composite_nums.add(num)
    return composite_nums