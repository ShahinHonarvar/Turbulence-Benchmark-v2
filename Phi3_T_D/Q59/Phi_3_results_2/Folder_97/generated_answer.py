def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(prime, num_digits):
        for i in range(num_digits):
            if not is_prime(int(str(prime)[i:])):
                return False
            prime = int(str(prime)[1:])
            if not prime:
                return False
        return True
    result = []
    for num in range(10, numbers[644], -1):
        if is_truncatable_prime(num, len(str(num))):
            result.append(num)
    return sorted(result)