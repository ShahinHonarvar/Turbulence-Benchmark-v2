def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    result = set()
    for index in range(64, 67):
        if is_composite(numbers[index]):
            result.add(numbers[index])
    return result