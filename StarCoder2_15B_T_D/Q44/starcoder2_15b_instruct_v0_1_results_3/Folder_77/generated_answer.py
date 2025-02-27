def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i, num in enumerate(numbers):
        if i >= 667 and i <= 774:
            is_composite = False
            for j in range(2, num):
                if num % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_nums.add(num)
    return composite_nums