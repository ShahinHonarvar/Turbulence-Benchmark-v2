def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    composite_numbers = set()
    for i, num in enumerate(numbers):
        if is_composite(num) and 686 <= i <= 987:
            composite_numbers.add(num)
    return composite_numbers