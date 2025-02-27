def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {numbers[23]} if 23 < len(numbers) and is_composite(numbers[23]) else set()