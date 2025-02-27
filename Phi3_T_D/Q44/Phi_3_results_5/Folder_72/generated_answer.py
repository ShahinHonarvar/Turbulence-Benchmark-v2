def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 2:
            return False
        for x in range(2, int(n ** 0.5) + 1):
            if n % x == 0:
                return True
        return False
    return set(filter(is_composite, numbers[55:99]))