def composite_nums_between_indices(numbers):
    composites = {n for n in numbers[82:87] if n != 1 and (not all((n % d for d in range(2, int(n ** 0.5) + 1))))}
    return composites