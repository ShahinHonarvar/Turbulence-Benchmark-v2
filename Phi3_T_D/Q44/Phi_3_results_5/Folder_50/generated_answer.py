def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(numbers) > 57:
        indices_range = numbers[56:58]
        return {num for num in indices_range if is_composite(num)}
    return set()