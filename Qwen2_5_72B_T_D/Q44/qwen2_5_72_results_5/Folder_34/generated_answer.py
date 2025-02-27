def composite_nums_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    result = set()
    for i in range(70, 201):
        if not is_prime(numbers[i]) and numbers[i] > 1:
            result.add(numbers[i])
    return result