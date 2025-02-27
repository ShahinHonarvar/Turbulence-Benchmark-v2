def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if 6 < len(numbers):
        if is_composite(numbers[6]):
            return {numbers[6]}
        else:
            return set()
    else:
        return set()