def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num, primes):
        num_str = str(num)
        return all((is_prime(int(num_str[i:])) for i in range(len(num_str)))) and int(num_str) in primes
    primes = [2, 3, 5, 7]
    for num in range(11, numbers[87]):
        if is_prime(num) and is_left_truncatable_prime(num, primes):
            primes.append(num)
    return primes