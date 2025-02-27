def composite_nums_between_indices(list_of_ints):
    composite_nums = set()
    for i, num in enumerate(list_of_ints):
        if i >= 35 and i <= 49:
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        composite_nums.add(num)
                        break
    return composite_nums