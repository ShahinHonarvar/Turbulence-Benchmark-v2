def all_left_right_truncatable_prime(numbers):
    x = numbers[73]
    primes = [2, 3, 5, 7]
    result = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        for i in range(len(n_str) - 1, 0, -1):
            if not is_prime(int(n_str[:i])):
                return False
        return True
    for num in range(3, x + 1, 2):
        if num in primes:
            if is_left_right_truncatable(num):
                result.append(num)
        elif is_prime(num):
            primes.append(num)
            if is_left_right_truncatable(num):
                result.append(num)
    return sorted(result, reverse=True)