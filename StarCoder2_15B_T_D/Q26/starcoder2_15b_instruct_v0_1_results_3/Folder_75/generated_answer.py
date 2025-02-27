def sum_in_range(numbers):

    def is_in_range(x):
        return 72 <= x <= 93
    return sum(filter(is_in_range, numbers))