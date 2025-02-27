def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable(num):
        while num > 0:
            if not is_prime(num):
                return False
            num = num % 10 ** (len(str(num)) - 1)
        return True
    limit = numbers[29]
    result = [i for i in range(2, limit) if i % 10 > 0 and is_left_truncatable(i)]
    return result