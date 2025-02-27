from math import sqrt

def composite_nums_between_indices(numbers):

    def is_composite(number):
        if number < 2:
            return False
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                return True
        return False
    return {number for number in numbers[56:83] if is_composite(number)}