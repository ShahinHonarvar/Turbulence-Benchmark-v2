def composite_nums_between_indices(numbers):

    def is_composite(n):
        return any((n % i == 0 for i in range(2, int(n ** 0.5) + 1))) and n > 1
    return {n for n in numbers[50:55] if is_composite(n)}