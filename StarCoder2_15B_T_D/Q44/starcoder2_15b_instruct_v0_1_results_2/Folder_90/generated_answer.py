def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i, num in enumerate(numbers):
        if i >= 333 and i <= 368:
            is_composite = False
            for j in range(2, num // 2 + 1):
                if num % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_numbers.add(num)
    return composite_numbers