def all_left_truncatable_prime(numbers):
    x = numbers[97]
    primes = [2, 3, 5, 7]
    result = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        for i in range(len(str(n))):
            if str(n)[i] == '0' or not is_prime(int(str(n)[:i + 1])):
                return False
        return True
    for num in range(11, x):
        if str(num)[0] != '0' and is_prime(num) and is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result)