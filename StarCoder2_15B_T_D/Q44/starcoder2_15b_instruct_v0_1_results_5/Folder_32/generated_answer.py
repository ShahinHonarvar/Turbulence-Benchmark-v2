def composite_nums_between_indices(lst):
    composite_nums = set()
    for num in lst:
        if num > 1:
            is_composite = False
            for i in range(2, num):
                if num % i == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_nums.add(num)
    return composite_nums