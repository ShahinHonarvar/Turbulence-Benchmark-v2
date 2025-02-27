def all_right_truncatable_prime(numbers):
    x = numbers[41]
    right_truncatable_primes = []
    primes = {2, 3, 5, 7}

    def is_prime(number, primes_set):
        for prime in primes_set:
            if number % prime == 0:
                return False
        return True

    def right_truncatable(number, primes_set, primes_list):
        for digit in str(number)[::-1]:
            number = int(digit)
            if not is_prime(number, primes_set):
                return False
        primes_list.append(number)
        return True
    for num in range(x - 1, 10, -1):
        if right_truncatable(num, primes, right_truncatable_primes):
            primes_set = primes.copy()
            primes_set.add(num)
    return right_truncatable_primes[::-1]