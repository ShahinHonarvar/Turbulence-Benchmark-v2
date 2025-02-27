def composite_nums_between_indices(lst):
    composite_nums = set()
    for num in lst:
        is_composite = False
        for divisor in range(2, num):
            if num % divisor == 0:
                is_composite = True
                break
        if is_composite:
            composite_nums.add(num)
    return composite_nums