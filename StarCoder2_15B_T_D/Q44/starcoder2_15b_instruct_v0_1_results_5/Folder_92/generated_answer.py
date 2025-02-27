def composite_nums_between_indices(input_list):
    composite_nums = set()
    for i in range(1, len(input_list) - 1):
        num = input_list[i]
        is_composite = False
        for j in range(2, num):
            if num % j == 0:
                is_composite = True
                break
        if is_composite:
            composite_nums.add(num)
    return composite_nums