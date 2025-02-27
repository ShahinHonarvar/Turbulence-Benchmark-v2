def composite_nums_between_indices(numbers):
    composite_nums = set()
    for num in numbers:
        is_composite = False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_composite = True
                break
        if is_composite:
            composite_nums.add(num)
    return composite_nums