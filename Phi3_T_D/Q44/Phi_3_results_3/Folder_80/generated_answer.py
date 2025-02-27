def composite_nums_between_indices(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    composite_numbers_set = set()
    for i in range(62, 79):
        if not is_prime(numbers[i]):
            composite_numbers_set.add(numbers[i])
    return composite_numbers_set