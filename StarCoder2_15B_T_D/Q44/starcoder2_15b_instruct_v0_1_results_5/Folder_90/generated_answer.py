def composite_nums_between_indices(numbers):

    def is_composite(n):
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    composite_nums = set()
    for i, num in enumerate(numbers):
        if is_composite(num) and 333 <= i <= 368:
            composite_nums.add(num)
    return composite_nums