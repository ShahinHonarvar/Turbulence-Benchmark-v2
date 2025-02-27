def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n > 1:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return True
            return False
        return False
    return {num for index, num in enumerate(numbers[35:50], start=35) if is_composite(num)}