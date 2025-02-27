def all_left_truncatable_prime(numbers):
    x = numbers[29]
    primes = [2, 3, 5, 7]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    result = []
    for num in range(2, x):
        if all((int(digit) != 0 for digit in str(num))) and is_prime(num) and is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)