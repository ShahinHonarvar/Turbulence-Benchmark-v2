def composite_nums_between_indices(lst):
    composite_nums = set()
    for i, num in enumerate(lst):
        if num > 1 and i >= 55 and (i <= 98):
            for j in range(2, num):
                if num % j == 0:
                    composite_nums.add(num)
                    break
    return composite_nums