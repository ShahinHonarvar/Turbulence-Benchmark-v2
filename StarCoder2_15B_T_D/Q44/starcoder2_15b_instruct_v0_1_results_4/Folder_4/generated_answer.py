def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i, num in enumerate(numbers):
        if i < 56 or i > 98:
            continue
        if num > 1:
            for j in range(2, num):
                if num % j == 0:
                    composite_numbers.add(num)
                    break
    return composite_numbers