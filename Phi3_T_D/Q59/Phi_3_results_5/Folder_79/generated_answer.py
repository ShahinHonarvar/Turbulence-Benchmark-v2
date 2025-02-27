def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[91]
    left_truncatable_primes = []
    for base_number in range(23, x):
        if not (str(base_number)[0] in '02468' or '0' in str(base_number)):
            temp = base_number
            while temp > 0:
                if not is_prime(temp):
                    break
                temp = temp // 10
            else:
                left_truncatable_primes.append(base_number)
    return left_truncatable_primes