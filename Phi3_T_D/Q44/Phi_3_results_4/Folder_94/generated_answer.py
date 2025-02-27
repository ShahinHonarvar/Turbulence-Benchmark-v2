def composite_nums_between_indices(numbers):

    def is_composite(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return True
        return False
    return {num for num in numbers[27:56] if is_composite(num)}