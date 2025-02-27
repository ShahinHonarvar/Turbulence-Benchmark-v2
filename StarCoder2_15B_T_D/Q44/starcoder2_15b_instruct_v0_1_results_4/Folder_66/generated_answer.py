def composite_nums_between_indices(lst):
    composite_nums = set()
    for i, num in enumerate(lst):
        if 62 <= i <= 63:
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        composite_nums.add(num)
                        break
    return composite_nums