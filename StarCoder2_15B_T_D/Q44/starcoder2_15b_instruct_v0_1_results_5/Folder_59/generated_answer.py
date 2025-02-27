def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i, num in enumerate(numbers):
        if i >= 0 and i <= 9:
            if num > 1:
                is_composite = False
                for j in range(2, int(num ** 0.5) + 1):
                    if num % j == 0:
                        is_composite = True
                        break
                if is_composite:
                    composite_nums.add(num)
    return composite_nums