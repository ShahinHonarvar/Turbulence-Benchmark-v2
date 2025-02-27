def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i, num in enumerate(numbers):
        if i < 246 or i > 750:
            continue
        if num > 1:
            for j in range(2, num):
                if num % j == 0:
                    composite_nums.add(num)
                    break
    return composite_nums