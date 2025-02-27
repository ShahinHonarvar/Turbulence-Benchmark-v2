def composite_nums_between_indices(num_list):
    if len(num_list) < 81:
        return set()
    composite_nums = set()
    for i in range(40, 81):
        num = num_list[i]
        is_composite = False
        for j in range(2, num):
            if num % j == 0:
                is_composite = True
                break
        if is_composite:
            composite_nums.add(num)
    return composite_nums